Write-Host "Starting Youtube Downloader Setup..." -ForegroundColor Cyan

if (!(Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "`n===================================================" -ForegroundColor Cyan
Write-Host "📱 TO ACCESS FROM YOUR ANDROID PHONE / LOCAL NETWORK:" -ForegroundColor Green
Write-Host "Ensure your phone and PC are connected to the same Wi-Fi."
Write-Host "Find your IPv4 Address below and type it into your phone's browser like so: http://YOUR_IP_ADDRESS:8000" -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan
ipconfig | findstr IPv4
Write-Host "===================================================`n" -ForegroundColor Cyan

Write-Host "Starting server and generating public link..." -ForegroundColor Green
python run_server.py
