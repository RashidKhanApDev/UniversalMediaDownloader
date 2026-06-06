@echo off
echo Stopping Universal Media Downloader Server...
taskkill /F /IM uvicorn.exe /T 2>nul
taskkill /F /IM node.exe /T 2>nul
echo Server stopped successfully.
pause
