<div align="center">
<br>
<h3>👨‍💻 Dev by <b>Rashid Khan Ap</b> <img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Twitter_Verified_Badge.svg" width="20" align="center"></h3>
<img src="https://capsule-render.vercel.app/api?type=waving&color=0ba360&height=250&section=header&text=Universal%20Media%20Downloader&fontSize=60&fontColor=ffffff&desc=Sleek.%20Fast.%20Premium.&descSize=25&descColor=e0e0e0" width="100%">

<br><br>

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![NodeJS](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)]()
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br><br>

<a href="https://colab.research.google.com/github/RashidKhanApDev/UniversalMediaDownloader/blob/main/UniversalMediaDownloader.ipynb" target="_blank">
  <img src="https://img.shields.io/badge/🔥_RUN_IN_GOOGLE_COLAB-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" width="450" alt="Open In Colab"/>
</a>

<br><br>

<a href="https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/RashidKhanApDev/UniversalMediaDownloader.git" target="_blank">
  <img src="https://img.shields.io/badge/☁️_OPEN_IN_CLOUD_SHELL-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" width="450" alt="Open In Cloud Shell"/>
</a>

<br><br>

> *Say goodbye to intrusive ads and slow downloads. Experience the premium way to fetch your favorite media content locally or on the cloud.*

</div>

---

## 📑 Table of Contents
1. [🌟 Overview & Description](#-overview--description)
2. [✨ Premium Features](#-premium-features)
3. [🏗️ Architecture & Flow](#️-architecture--flow)
4. [🛠️ Tech Stack Showcase](#️-tech-stack-showcase)
5. [📂 Project Structure](#-project-structure)
6. [📥 Installation & Setup](#-installation--setup)
7. [🇮🇳 ചെറുവിവരണം (Malayalam)](#-ചെറുവിവരണം-malayalam-summary)

---

## 🌟 Overview & Description

<div align="center">
  <img src="https://opengraph.githubassets.com/1/RashidKhanApDev/UniversalMediaDownloader" width="100%" alt="Universal Media Downloader Preview" style="border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); margin-top: 20px; margin-bottom: 20px;">
</div>

Welcome to the **Universal Media Downloader**! This modern, responsive web application is built on top of the lightning-fast **FastAPI** framework and powered by the robust `yt-dlp` library. 

Whether you are looking to save a quick audio track for your playlist or download a stunning cinematic video in pristine **4K or 8K resolution**, this tool has you covered. Designed with a gorgeous, interactive **Glassmorphism UI**, it guarantees a seamless and visually pleasing user experience while maintaining blazing-fast backend performance. 

---

## ✨ Premium Features

| 🎥 Extreme High-Resolution | 🎵 Audio-Only Extraction | ⚡ Dynamic Resolution |
| :---: | :---: | :---: |
| Seamlessly download videos in 1080p, 1440p (2K), 2160p (4K), and up to 8K. | Extract crystal-clear MP3/M4A audio effortlessly with a single click. | Automatically detects and lists all available formats and resolutions. |

| 🎨 Modern Aesthetic | 🚀 Fast & Lightweight | ☁️ Cloud Ready |
| :---: | :---: | :---: |
| Beautiful, responsive, and intuitive Glassmorphism interface. | Powered by FastAPI for asynchronous, non-blocking execution. | One-click deployment to Google Colab via Cloudflare Tunnels. |

---

## 🏗️ Architecture & Flow

Our system architecture is designed for speed, reliability, and security. Below is the visual representation of how data flows through our ecosystem:

```mermaid
graph TD;
    %% Styling
    classDef ui fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:white;
    classDef api fill:#1e293b,stroke:#10b981,stroke-width:2px,color:white;
    classDef engine fill:#334155,stroke:#f59e0b,stroke-width:2px,color:white;
    classDef external fill:#1e293b,stroke:#ef4444,stroke-width:2px,color:white;

    %% Nodes
    A[🖥️ Premium Glassmorphism UI]:::ui
    B{🌐 FastAPI Router}:::api
    C((🧠 Universal Multi-Platform Engine)):::engine
    D[📺 Social Media APIs <br/> Instagram, TikTok, Facebook, etc.]:::external
    E{📚 Playlist Detector}:::engine
    F[[📦 ZIP Archiver]]:::api
    G[[🎬 FFmpeg Audio/Video Merger]]:::api
    H[🌍 Local / Cloud Download]:::ui

    %% Connections
    A -->|1. Submit Media URL| B
    B -->|2. Analyze Request| C
    C -->|3. Fetch Media Metadata| D
    D -->|4. Return Data Streams| C
    C -->|5. Single Video or Playlist?| E
    E -->|Single Video| G
    E -->|Playlist / Multi-Video| F
    G -->|Merged Media| H
    F -->|Zipped Collection| H
```

---

## 📂 Project Structure

A clean, organized, and scalable directory layout ensures maximum developer productivity:

```bash
📦 UniversalMediaDownloader
 ┣ 📂 templates/           # Frontend UI Assets
 ┃ ┗ 📜 index.html         # Premium Glassmorphism View
 ┣ 📂 downloads/           # Secure Output Directory
 ┣ 📜 main.py              # Application Core (FastAPI)
 ┣ 📜 run_server.py        # Cross-platform Process Manager
 ┣ 📜 create_colab.py      # Cloud Generation Engine
 ┣ 📜 UniversalMediaDownloader.ipynb # Auto-generated Notebook
 ┣ 📜 requirements.txt     # Dependency Definitions
 ┣ 📜 run.bat              # Windows Automation Script
 ┣ 📜 run.sh               # Linux Automation Script
 ┗ 📜 README.md            # Project Documentation
```

---

## 🛠️ Tech Stack Showcase

We utilized multiple industry-standard languages and frameworks to deliver this premium experience.

### ⚙️ JSON (Configuration)
```json
{
  "app_name": "UniversalMediaDownloader",
  "version": "3.5.0",
  "author": "Rashid Khan",
  "license": "MIT"
}
```

### 🐍 Python (Backend API)
```python
from fastapi import FastAPI
import yt_dlp

app = FastAPI(title="Universal Media Downloader API")

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
    <h1>Universal Media Downloader</h1>
    <input type="text" placeholder="Paste Media Link Here...">
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

### 🟦 TypeScript (Next-Gen UI Typing)
```typescript
interface VideoDetails {
    id: string;
    title: string;
    resolutions: Array<string>;
    duration: number;
}
```

### 🐹 Go (High-Speed Microservice Concept)
```go
package main
import "fmt"

func fetchVideoMeta(id string) {
    fmt.Printf("Fetching high-speed metadata for %s...", id)
}
```

### 🗄️ SQL (Future Analytics Schema)
```sql
CREATE TABLE IF NOT EXISTS downloads (
    id UUID PRIMARY KEY,
    video_url VARCHAR(255) NOT NULL,
    quality VARCHAR(10) NOT NULL,
    download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 🐳 Dockerfile (Advanced Containerization)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🦀 Rust (High-Performance Core Concept)
```rust
fn process_stream(buffer: &[u8]) -> Result<(), &'static str> {
    println!("Processing {} bytes of ultra-fast video stream", buffer.len());
    Ok(())
}
```

### 📝 Markdown (Documentation Standards)
```markdown
> **Developer Note**: All architectural decisions follow strict industry standards.
```

### 📜 TOML (Modern Python Config)
```toml
[tool.poetry]
name = "UniversalMediaDownloader"
version = "3.5.0"
description = "Premium Universal Media Downloader with Glassmorphism UI"
authors = ["Rashid Khan <admin@example.com>"]
```

---

## 📥 Installation & Setup

Before installing the tool locally, please ensure your system has **Python 3.8+**, **FFmpeg**, and **Node.js**.

### 💻 Command Line Setup (Bash)
```bash
# Clone the repository
git clone https://github.com/RashidKhanApDev/UniversalMediaDownloader.git
cd UniversalMediaDownloader

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

### ☁️ Google Cloud Shell
```bash
# Cloud Shell comes pre-installed with requirements. Just run:
chmod +x run.sh
./run.sh
# Then click "Web Preview" -> "Preview on port 8000" in the top right corner!
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

ഈ ടൂൾ ഉപയോഗിച്ച് നിങ്ങൾക്ക് എല്ലാ സോഷ്യൽ മീഡിയ വീഡിയോകളും (Instagram, Facebook, Twitter, YouTube ഉൾപ്പെടെ) ഓഡിയോകളും വളരെ എളുപ്പത്തിൽ ഏറ്റവും ഉയർന്ന ക്വാളിറ്റിയിൽ (2K, 4K ഉൾപ്പെടെ) ഡൗൺലോഡ് ചെയ്യാവുന്നതാണ്. ഇത് വളരെ ലളിതവും, അതിവേഗത്തിൽ പ്രവർത്തിക്കുന്നതും, ലോകോത്തര പ്രീമിയം ഡിസൈനോടുകൂടിയതുമാണ് (Glassmorphism UI). 

ഏറ്റവും മുകളിലുള്ള വലിയ **"RUN IN GOOGLE COLAB"** ബട്ടണിൽ ക്ലിക്ക് ചെയ്താൽ, നിങ്ങളുടെ ഫോണിൽ നിന്നോ കമ്പ്യൂട്ടറിൽ നിന്നോ യാതൊരുവിധ ഇൻസ്റ്റാളേഷനും ഇല്ലാതെ തന്നെ നേരിട്ട് ക്ലൗഡ് വഴി നിങ്ങൾക്ക് ഈ ടൂൾ ഉപയോഗിക്കാവുന്നതാണ്. 

നിങ്ങളുടെ സ്വന്തം കമ്പ്യൂട്ടറിൽ (Windows, Ubuntu, Kali Linux തുടങ്ങിയവയിൽ) ഇത് ഇൻസ്റ്റാൾ ചെയ്യാനും ഉപയോഗിക്കാനും വളരെ എളുപ്പമാണ്. ഇതിൽ യാതൊരുവിധ പരസ്യങ്ങളുമില്ല, തികച്ചും സുരക്ഷിതമായി നിങ്ങൾക്ക് ആവശ്യമുള്ള വീഡിയോകൾ ഡൗൺലോഡ് ചെയ്തെടുക്കാം.

---

<div align="center">
  <h3>👨‍💻 Dev by <b>Rashid Khan Ap</b> <img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Twitter_Verified_Badge.svg" width="20" align="center"></h3>
  <b>Built with ❤️ using Modern Web Technologies</b><br>
  <i>MIT License. Strictly intended for personal and educational use.</i>
</div>
