import os
import glob
import uuid
import asyncio
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

# Create necessary directories
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)
os.makedirs("templates", exist_ok=True)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class URLRequest(BaseModel):
    url: str

class DownloadRequest(BaseModel):
    url: str
    format_id: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/api/info")
async def get_video_info(request: URLRequest):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'noplaylist': True,
    }
    try:
        def fetch_info():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(request.url, download=False)
        
        info = await asyncio.to_thread(fetch_info)
        
        resolutions = {}
        for f in info.get('formats', []):
            if f.get('vcodec') != 'none':
                height = f.get('height')
                if height:
                    res_label = f"{height}p"
                    # Prefer formats that already have audio, else combine with bestaudio
                    if f.get('acodec') != 'none':
                        resolutions[res_label] = f['format_id']
                    else:
                        if res_label not in resolutions:
                            resolutions[res_label] = f"{f['format_id']}+bestaudio"

        sorted_res = sorted(resolutions.keys(), key=lambda x: int(x.replace('p', '')), reverse=True)
        available_formats = []
        for res in sorted_res:
            label = f"Video: {res}"
            if res == "1440p":
                label = "Video: 1440p (2K)"
            elif res == "2160p":
                label = "Video: 2160p (4K)"
            elif res == "2880p":
                label = "Video: 2880p (5K)"
            elif res == "4320p":
                label = "Video: 4320p (8K)"
            available_formats.append({'id': resolutions[res], 'label': label})
        
        available_formats.append({'id': 'bestaudio', 'label': 'Audio Only (Best Quality)'})

        return {
            "title": info.get('title', 'Unknown Title'),
            "thumbnail": info.get('thumbnail', ''),
            "formats": available_formats
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/download")
async def download_video(request: DownloadRequest):
    file_id = str(uuid.uuid4())
    output_template = os.path.join(DOWNLOAD_DIR, f"{file_id}.%(ext)s")
    
    ydl_opts = {
        'format': request.format_id,
        'outtmpl': output_template,
        'quiet': True,
        'noplaylist': True,
        'merge_output_format': 'mp4',
    }
    
    try:
        def download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(request.url, download=True)
                return info.get('title', 'video')

        title = await asyncio.to_thread(download)
        
        # Find the downloaded file
        files = glob.glob(os.path.join(DOWNLOAD_DIR, f"{file_id}.*"))
        if not files:
            raise HTTPException(status_code=500, detail="Downloaded file not found")
            
        filename = os.path.basename(files[0])
        
        return {
            "download_url": f"/api/file/{filename}",
            "title": title
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/file/{filename}")
async def get_file(filename: str, title: str = "download"):
    filename = os.path.basename(filename)
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    ext = os.path.splitext(filename)[1]
    # Sanitize title for filename
    safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    if not safe_title:
        safe_title = "download"
    download_name = f"{safe_title}{ext}"
    
    return FileResponse(path=file_path, filename=download_name, media_type='application/octet-stream')
