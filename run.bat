@echo off
echo Starting Youtube Downloader Setup...

IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ===================================================
echo 📱 TO ACCESS FROM YOUR ANDROID PHONE / LOCAL NETWORK:
echo Ensure your phone and PC are connected to the same Wi-Fi.
echo Find your IPv4 Address below and type it into your phone's browser like so: http://YOUR_IP_ADDRESS:8000
echo ===================================================
ipconfig | findstr IPv4
echo ===================================================
echo.
echo Starting server and generating public link...
python run_server.py
pause
