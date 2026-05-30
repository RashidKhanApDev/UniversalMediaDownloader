<div align="center" style="background: linear-gradient(135deg, #0ba360 0%, #3cba92 100%); padding: 40px; border-radius: 15px; color: white; margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
  
<h1 style="color: white; border-bottom: none; margin-bottom: 20px;">🎥 Ultimate YouTube Downloader 🚀</h1>

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br>
<p style="font-size: 1.1em;"><i>A sleek, high-performance, and professionally designed web application to download YouTube videos in maximum quality.</i></p>

</div>

---

## 🌟 Overview & Description

Welcome to the **Ultimate YouTube Downloader**! This modern, responsive web application is built on top of the lightning-fast **FastAPI** framework and powered by the robust `yt-dlp` library. 

Whether you are looking to save a quick audio track for your playlist or download a stunning cinematic video in pristine 4K or 8K resolution, this tool has you covered. Designed with a gorgeous, interactive **Glassmorphism UI**, it guarantees a seamless and visually pleasing user experience while maintaining blazing-fast backend performance. Say goodbye to intrusive ads and slow downloads—this is your premium, all-in-one solution for fetching YouTube content locally!

## ✨ Key Features
- **🎥 Extreme High-Resolution Support**: Seamlessly download videos in 1080p, 1440p (2K), 2160p (4K), and even up to 8K.
- **🎵 Audio-Only Extraction**: Extract crystal-clear MP3/M4A audio effortlessly with a single click.
- **⚡ Dynamic Resolution Fetching**: Automatically detects and lists all available formats and resolutions for any given video URL.
- **🎨 Modern Aesthetic**: Beautiful, responsive, and intuitive Glassmorphism interface that feels premium.
- **🚀 Fast & Lightweight**: Powered by FastAPI for asynchronous, non-blocking backend execution.

---

## 🛠️ Prerequisites

Before installing the tool, please ensure your system has the following dependencies installed:
- **Python 3.8 or higher**: Required for running the FastAPI backend server.
- **FFmpeg**: Essential for merging high-quality video and audio streams together.
- **Node.js**: Required by `yt-dlp` for efficiently extracting ciphered YouTube signatures.

---

## 📥 Installation: Step-by-Step

Follow these simple steps to install the tool on your machine:

1. **Clone the Repository** (Or download the ZIP and extract it):
   ```bash
   git clone https://github.com/your-username/YoutubeDownloader.git
   cd YoutubeDownloader
   ```

2. **Create a Virtual Environment** (Highly Recommended to prevent dependency conflicts):
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows**: `venv\Scripts\activate`
   - **Linux / macOS**: `source venv/bin/activate`

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Tool

This application is cross-platform and can be run across various environments using our automated scripts or manual commands. Once the server is running, open your web browser and navigate to:  
👉 **`http://localhost:8000`**

### 🪟 Windows (Command Prompt - CMD)
You can directly execute the provided batch script to handle everything automatically:
```cmd
run.bat
```
*(Alternatively, you can manually run: `uvicorn main:app --reload`)*

### 🪟 Windows (PowerShell)
Execute the PowerShell script for an optimized startup:
```powershell
.\run.ps1
```
> **Note**: If your PowerShell execution policy blocks the script, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` as Administrator first, then try again.

### 🐧 Ubuntu / Debian
For standard Linux distributions, use the bash script:
1. Make the script executable:
   ```bash
   chmod +x run.sh
   ```
2. Start the server:
   ```bash
   ./run.sh
   ```

### 🐉 Kali Linux
Kali Linux uses a similar architecture to Ubuntu. You can simply use the terminal to run the script. First, ensure your dependencies are installed, then run the app:
```bash
sudo apt update && sudo apt install python3 ffmpeg nodejs
chmod +x run.sh
./run.sh
```

---

## 🇮🇳 ചെറുവിവരണം (Malayalam Summary)

ഈ ടൂൾ ഉപയോഗിച്ച് നിങ്ങൾക്ക് YouTube വീഡിയോകളും ഓഡിയോകളും വളരെ എളുപ്പത്തിൽ ഹൈ ക്വാളിറ്റിയിൽ (2K, 4K ഉൾപ്പെടെ) ഡൗൺലോഡ് ചെയ്യാവുന്നതാണ്. ഇത് വളരെ ലളിതവും വേഗതയേറിയതും മികച്ച ഡിസൈനോടുകൂടിയതുമാണ്. 

നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ (Windows, Ubuntu, Kali Linux തുടങ്ങിയവയിൽ) ഇത് ഇൻസ്റ്റാൾ ചെയ്യാനും ഉപയോഗിക്കാനും വളരെ എളുപ്പമാണ്. ഇതിൽ യാതൊരുവിധ പരസ്യങ്ങളുമില്ല, തികച്ചും സുരക്ഷിതമായി നിങ്ങൾക്ക് ആവശ്യമുള്ള വീഡിയോകൾ ഡൗൺലോഡ് ചെയ്തെടുക്കാം.

---

## 📄 License & Disclaimer
This project is open-source and available under the **MIT License**. It is strictly intended for personal and educational use. Please respect the copyright of the content creators when downloading videos.

<div align="center">
  <i>Built with ❤️ for content creators and viewers alike.</i>
</div>
