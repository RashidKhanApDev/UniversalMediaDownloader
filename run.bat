@echo off
set PYTHONIOENCODING=utf-8
echo Starting Universal Media Downloader Setup...

IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting server and generating public link...
python run_server.py
pause
