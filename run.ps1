Write-Host "Starting Youtube Downloader Setup..." -ForegroundColor Cyan

if (!(Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "Starting server and generating public link..." -ForegroundColor Green
python run_server.py
