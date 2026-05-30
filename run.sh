#!/bin/bash
echo "Starting Youtube Downloader Setup..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install Python 3."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "==================================================="
echo "📱 TO ACCESS FROM YOUR ANDROID PHONE / LOCAL NETWORK:"
echo "Ensure your phone and PC are connected to the same Wi-Fi."
echo "Find your Local IP Address below and type it into your phone's browser like so: http://YOUR_IP_ADDRESS:8000"
echo "==================================================="
hostname -I || ipconfig getifaddr en0 || echo "IP could not be automatically determined. Run 'ip a' or 'ifconfig'."
echo "==================================================="
echo ""

# Run the server
echo "Starting server and generating public link..."
python3 run_server.py
