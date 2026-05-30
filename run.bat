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

echo Starting server...
uvicorn main:app --host localhost --port 8000 --reload
pause
