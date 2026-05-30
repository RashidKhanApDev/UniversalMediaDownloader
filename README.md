# Youtube Downloader

A modern, responsive web application for downloading YouTube videos in high quality (including 2K and 4K) using FastAPI and `yt-dlp`.

## Features
- Dynamic resolution fetching
- Support for 2K and 4K downloads (requires FFmpeg)
- Audio-only downloads
- Beautiful Glassmorphism UI

## Prerequisites
- **Python 3.8+**
- **FFmpeg** (Required for merging video and audio streams for 1080p+ formats)
- **Node.js** (Required for `yt-dlp` to extract YouTube's ciphered formats)

## How to Run

### On Windows (PowerShell or Command Prompt)
Simply run one of the following scripts:
- **`run.bat`** (For Command Prompt)
- **`run.ps1`** (For PowerShell)

*Note: If PowerShell prevents execution, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` first.*

### On Linux / Ubuntu / macOS (Terminal)
1. Make the script executable:
   ```bash
   chmod +x run.sh
   ```
2. Run the script:
   ```bash
   ./run.sh
   ```

The application will automatically install dependencies in an isolated virtual environment and start locally at `http://localhost:8000`.
