import subprocess
import threading
import sys
import time

def start_tunnel():
    print("\n[Tunnel] Starting LocalTunnel to generate a public link...")
    try:
        # Use shell=True on Windows to resolve 'npx' from PATH
        use_shell = sys.platform.startswith('win')
        process = subprocess.Popen(
            ['npx', 'localtunnel', '--port', '8000'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            shell=use_shell
        )
        
        for line in process.stdout:
            if "your url is" in line.lower():
                url = line.split("is")[-1].strip()
                print("\n" + "="*60)
                print("🌍 PUBLIC INTERNET LINK GENERATED SUCCESSFULLY!")
                print(f"👉 Link: {url}")
                print("Send this link to your friends anywhere in the world!")
                print("="*60 + "\n")
            else:
                pass
    except Exception as e:
        print(f"\n[Tunnel Error] Failed to start LocalTunnel: {e}")
        print("[Tunnel Error] Make sure Node.js is installed.")

if __name__ == "__main__":
    # Start the tunnel in a background thread
    tunnel_thread = threading.Thread(target=start_tunnel, daemon=True)
    tunnel_thread.start()
    
    # Wait a brief moment to ensure logs don't overlap too much
    time.sleep(1)
    
    # Start the FastAPI server using Uvicorn
    print("\n🚀 Starting Youtube Downloader Server...\n")
    try:
        # Use sys.executable to ensure it uses the virtual environment's python correctly
        # This prevents FileNotFoundError on Windows when looking for 'uvicorn'
        subprocess.run([sys.executable, '-m', 'uvicorn', 'main:app', '--host', 'localhost', '--port', '8000', '--reload'])
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\n[Server Error] Failed to start Uvicorn: {e}")
