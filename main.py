import os
import glob
import uuid
import asyncio
import json
import re
import threading
import shutil
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

history_lock = threading.Lock()

# Create necessary directories
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)
os.makedirs("templates", exist_ok=True)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
DOWNLOAD_ROOT = os.path.abspath(DOWNLOAD_DIR)

HISTORY_FILE = "history.json"

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class URLRequest(BaseModel):
    url: str
    browser: str = "none"

class DownloadRequest(BaseModel):
    url: str
    format_id: str
    browser: str = "none"
    target_format: str = "default"
    is_playlist: bool = False

def save_history(title, target_format, filename):
    with history_lock:
        try:
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    history = json.load(f)
            else:
                history = []
            
            history.insert(0, {
                "title": title,
                "target_format": target_format,
                "filename": filename,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Keep only last 50
            history = history[:50]
            
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Failed to save history: {e}")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/api/history")
async def get_history():
    with history_lock:
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

@app.post("/api/info")
async def get_video_info(request: URLRequest):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'extract_flat': 'in_playlist',
        'noplaylist': True, # Downloads single video if URL has both video ID & playlist ID
    }
    
    if request.browser and request.browser.lower() != "none":
        ydl_opts['cookiesfrombrowser'] = (request.browser.lower(),)
        
    try:
        def fetch_info():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(request.url, download=False)
        
        info = await asyncio.to_thread(fetch_info)
        
        # Handle Playlists
        if info.get('_type') == 'playlist':
            entries = info.get('entries', [])
            return {
                "is_playlist": True,
                "title": info.get('title', 'Unknown Playlist'),
                "count": len(entries),
                "thumbnail": entries[0].get('thumbnails', [{}])[0].get('url') if entries and entries[0].get('thumbnails') else "",
                "formats": []
            }
        
        # Handle Single Videos & Social Media
        resolutions = {}
        for f in info.get('formats', []):
            if f.get('vcodec') != 'none':
                height = f.get('height')
                if height:
                    res_label = f"{height}p"
                    if f.get('acodec') != 'none':
                        resolutions[res_label] = f['format_id']
                    else:
                        if res_label not in resolutions:
                            resolutions[res_label] = f"{f['format_id']}+bestaudio/best"
                else:
                    # Non-YouTube platforms might not have height
                    format_note = f.get('format_note', '')
                    if format_note and format_note not in resolutions:
                        resolutions[format_note] = f['format_id']

        # Sort numeric resolutions if possible
        def get_res_val(k):
            match = re.search(r'(\d+)p', k)
            return int(match.group(1)) if match else 0
            
        sorted_res = sorted(resolutions.keys(), key=get_res_val, reverse=True)
        available_formats = []
        for res in sorted_res:
            label = f"Video: {res}"
            if res == "1440p": label = "Video: 1440p (2K)"
            elif res == "2160p": label = "Video: 2160p (4K)"
            elif res == "2880p": label = "Video: 2880p (5K)"
            elif res == "4320p": label = "Video: 4320p (8K)"
            available_formats.append({'id': resolutions[res], 'label': label})
        
        # Fallback if no specific formats parsed (e.g., TikTok/Instagram)
        if not available_formats:
            available_formats.append({'id': 'bestvideo+bestaudio/best', 'label': 'Best Quality (Video + Audio)'})
            
        available_formats.append({'id': 'bestaudio/best', 'label': 'Audio Only (Best Quality)'})

        return {
            "is_playlist": False,
            "title": info.get('title', 'Unknown Title'),
            "thumbnail": info.get('thumbnail', ''),
            "formats": available_formats
        }
    except Exception as e:
        error_msg = str(e)
        if "database is locked" in error_msg.lower() or "permission denied" in error_msg.lower():
            raise HTTPException(status_code=400, detail="Browser database is locked. Please close your browser to use cookies, or try downloading without cookies.")
        raise HTTPException(status_code=400, detail=error_msg)

@app.post("/api/download")
async def download_video(request: DownloadRequest):
    file_id = str(uuid.uuid4())
    target = request.target_format.lower()
    
    if request.is_playlist:
        # For playlists, download into a folder and ZIP it
        playlist_dir = os.path.join(DOWNLOAD_DIR, file_id)
        os.makedirs(playlist_dir, exist_ok=True)
        output_template = os.path.join(playlist_dir, "%(playlist_index)s - %(title)s.%(ext)s")
    else:
        output_template = os.path.join(DOWNLOAD_DIR, f"{file_id}.%(ext)s")
    
    ydl_opts = {
        'format': request.format_id,
        'outtmpl': output_template,
        'quiet': True,
        'noplaylist': not request.is_playlist, # enforce single video rule
    }
    
    if request.is_playlist:
        ydl_opts['playlistend'] = 100 # limit to 100 items to prevent exhaustion
    
    if request.browser and request.browser.lower() != "none":
        ydl_opts['cookiesfrombrowser'] = (request.browser.lower(),)

    postprocessors = []

    if target in ['mp3', 'wav', 'flac', 'm4a']:
        # Extract audio
        ydl_opts['format'] = 'bestaudio/best'
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': target if target != 'default' else 'mp3',
            'preferredquality': '192',
        })
    elif target in ['mp4', 'mkv']:
        # Video conversion
        ydl_opts['merge_output_format'] = target
        postprocessors.append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': target,
        })
    else:
        # Default
        if not request.is_playlist:
            ydl_opts['merge_output_format'] = 'mp4'

    if postprocessors:
        ydl_opts['postprocessors'] = postprocessors

    try:
        def download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(request.url, download=True)
                return info.get('title', 'Media')

        title = await asyncio.to_thread(download)
        
        if request.is_playlist:
            # Create a zip archive of the downloaded directory
            zip_path = os.path.join(DOWNLOAD_DIR, file_id)
            await asyncio.to_thread(shutil.make_archive, zip_path, 'zip', playlist_dir)
            
            # Clean up raw folder
            await asyncio.to_thread(shutil.rmtree, playlist_dir, ignore_errors=True)
            
            filename = f"{file_id}.zip"
            await asyncio.to_thread(save_history, title, "ZIP (Playlist)", filename)
        else:
            # Find the downloaded file for single video
            files = glob.glob(os.path.join(DOWNLOAD_DIR, f"{file_id}.*"))
            valid_files = [f for f in files if not f.endswith('.part') and not f.endswith('.ytdl')]
            if not valid_files:
                raise HTTPException(status_code=500, detail="Downloaded file not found or download failed to merge correctly")
                
            filename = os.path.basename(valid_files[0])
            await asyncio.to_thread(save_history, title, target if target != "default" else "mp4", filename)
        
        return {
            "download_url": f"/api/file/{filename}",
            "title": title
        }
    except Exception as e:
        error_msg = str(e)
        if "database is locked" in error_msg.lower() or "permission denied" in error_msg.lower():
            raise HTTPException(status_code=400, detail="Browser database is locked. Please close your browser to use cookies, or try downloading without cookies.")
        raise HTTPException(status_code=400, detail=error_msg)

@app.get("/api/file/{filename}")
async def get_file(filename: str, title: str = "download"):
    if (
        not filename
        or filename in (".", "..")
        or filename != os.path.basename(filename)
        or not re.fullmatch(r"[\w\s\-\.\(\)\[\]]+", filename)
    ):
        raise HTTPException(status_code=400, detail="Invalid file name")

    file_path = os.path.abspath(os.path.join(DOWNLOAD_ROOT, filename))
    if os.path.commonpath([DOWNLOAD_ROOT, file_path]) != DOWNLOAD_ROOT:
        raise HTTPException(status_code=400, detail="Invalid file path")
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    ext = os.path.splitext(filename)[1]
    safe_title = re.sub(r'[^\w\s\-\(\)\[\]]', '', title).strip()
    if not safe_title:
        safe_title = "download"
    download_name = f"{safe_title}{ext}"
    
    return FileResponse(path=file_path, filename=download_name, media_type='application/octet-stream')
