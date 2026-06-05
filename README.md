<div align="center">

<img src="https://raw.githubusercontent.com/google/material-design-icons/master/png/av/music_video/materialicons/48dp/2x/baseline_music_video_black_48dp.png" width="100" alt="Logo">

# 🎥 Ultimate YouTube Downloader 🚀
**A sleek, high-performance, and professionally designed web application to download YouTube videos in maximum quality.**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![NodeJS](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br>

<a href="https://colab.research.google.com/github/RashidKhanApDev/YoutubeDownloader/blob/main/YoutubeDownloader.ipynb" target="_blank">
  <img src="https://img.shields.io/badge/🔥_RUN_IN_GOOGLE_COLAB-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" width="400" alt="Open In Colab"/>
</a>

<br><br>

> *Say goodbye to intrusive ads and slow downloads. Experience the premium way to fetch your favorite YouTube content locally or on the cloud.*

</div>

---

## 🌟 Overview & Description

Welcome to the **Ultimate YouTube Downloader**! This modern, responsive web application is built on top of the lightning-fast **FastAPI** framework and powered by the robust `yt-dlp` library. 

Whether you are looking to save a quick audio track for your playlist or download a stunning cinematic video in pristine 4K or 8K resolution, this tool has you covered. Designed with a gorgeous, interactive **Glassmorphism UI**, it guarantees a seamless and visually pleasing user experience while maintaining blazing-fast backend performance. 

---

## ✨ Premium Features

| 🎥 Extreme High-Resolution | 🎵 Audio-Only Extraction | ⚡ Dynamic Resolution |
| :---: | :---: | :---: |
| Seamlessly download videos in 1080p, 1440p (2K), 2160p (4K), and up to 8K. | Extract crystal-clear MP3/M4A audio effortlessly with a single click. | Automatically detects and lists all available formats and resolutions. |

| 🎨 Modern Aesthetic | 🚀 Fast & Lightweight | ☁️ Cloud Ready |
| :---: | :---: | :---: |
| Beautiful, responsive, and intuitive Glassmorphism interface. | Powered by FastAPI for asynchronous, non-blocking execution. | One-click deployment to Google Colab via Cloudflare Tunnels. |

---

## 🛠️ Tech Stack & Architecture

We utilized multiple industry-standard languages and frameworks to deliver this premium experience.

### 🐍 Python (Backend API)
```python
from fastapi import FastAPI
import yt_dlp

app = FastAPI(title="YouTube Downloader API")

@app.get("/api/info")
async def get_video_info(url: str):
    # Asynchronously fetch video metadata
    pass
```

### 🟨 JavaScript (Frontend Logic)
```javascript
async function fetchDownloadUrl(videoId) {
    const response = await fetch(`/api/download?id=${videoId}`);
    const data = await response.json();
    return data.download_url;
}
```

### 🟧 HTML (Structure)
```html
<div class="glass-container">
    <h1>YouTube Downloader</h1>
    <input type="text" placeholder="Paste YouTube Link Here...">
    <button class="btn-primary">Fetch Video</button>
</div>
```

### 🟦 CSS (Glassmorphism Styling)
```css
.glass-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}
```

### ⚙️ JSON (Configuration)
```json
{
  "app_name": "YoutubeDownloader",
  "version": "3.0.0",
  "author": "Rashid Khan",
  "license": "MIT"
}
```

---

## 📥 Installation & Setup

Before installing the tool locally, please ensure your system has **Python 3.8+**, **FFmpeg**, and **Node.js**.

### 💻 Command Line Setup (Bash)
```bash
# Clone the repository
git clone https://github.com/RashidKhanApDev/YoutubeDownloader.git
cd YoutubeDownloader

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 How to Run the Server Locally

### 🪟 Windows (PowerShell)
```powershell
# Execute the PowerShell script for optimized startup
.\run.ps1
```

### 🐧 Linux / macOS (Bash)
```bash
# Make script executable and run
chmod +x run.sh
./run.sh
```

### 🐳 Docker Configuration (YAML)
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./downloads:/app/downloads
```

---

## 🇮🇳 ചെറുവിവരണം (Malayalam Summary)

ഈ ടൂൾ ഉപയോഗിച്ച് നിങ്ങൾക്ക് YouTube വീഡിയോകളും ഓഡിയോകളും വളരെ എളുപ്പത്തിൽ ഏറ്റവും ഉയർന്ന ക്വാളിറ്റിയിൽ (2K, 4K ഉൾപ്പെടെ) ഡൗൺലോഡ് ചെയ്യാവുന്നതാണ്. ഇത് വളരെ ലളിതവും, അതിവേഗത്തിൽ പ്രവർത്തിക്കുന്നതും, ലോകോത്തര പ്രീമിയം ഡിസൈനോടുകൂടിയതുമാണ് (Glassmorphism UI). 

ഏറ്റവും മുകളിലുള്ള വലിയ **"RUN IN GOOGLE COLAB"** ബട്ടണിൽ ക്ലിക്ക് ചെയ്താൽ, നിങ്ങളുടെ ഫോണിൽ നിന്നോ കമ്പ്യൂട്ടറിൽ നിന്നോ യാതൊരുവിധ ഇൻസ്റ്റാളേഷനും ഇല്ലാതെ തന്നെ നേരിട്ട് ക്ലൗഡ് വഴി നിങ്ങൾക്ക് ഈ ടൂൾ ഉപയോഗിക്കാവുന്നതാണ്. 

നിങ്ങളുടെ സ്വന്തം കമ്പ്യൂട്ടറിൽ (Windows, Ubuntu, Kali Linux തുടങ്ങിയവയിൽ) ഇത് ഇൻസ്റ്റാൾ ചെയ്യാനും ഉപയോഗിക്കാനും വളരെ എളുപ്പമാണ്. ഇതിൽ യാതൊരുവിധ പരസ്യങ്ങളുമില്ല, തികച്ചും സുരക്ഷിതമായി നിങ്ങൾക്ക് ആവശ്യമുള്ള വീഡിയോകൾ ഡൗൺലോഡ് ചെയ്തെടുക്കാം.

---

<div align="center">
  <b>Built with ❤️ using Modern Web Technologies</b><br>
  <i>MIT License. Strictly intended for personal and educational use.</i>
</div>
