import json
nb = {
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {"provenance": []},
    "kernelspec": {"name": "python3", "display_name": "Python 3"}
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# YoutubeDownloader - Free Cloud Version\n",
        "Run this cell to start the server on Google's free cloud! Once it finishes, click the **localtunnel link** and enter the **Endpoint IP** as the password."
      ],
      "metadata": {"id": "md1"}
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {"id": "code1"},
      "outputs": [],
      "source": [
        "!git clone https://github.com/RashidKhanApDev/YoutubeDownloader.git\n",
        "%cd YoutubeDownloader\n",
        "!pip install -r requirements.txt\n",
        "!npm install -g localtunnel\n",
        "import subprocess, time, urllib.request\n",
        "print(\"\\n--- STARTING SERVER ---\")\n",
        "subprocess.Popen([\"python\", \"-m\", \"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"])\n",
        "time.sleep(3)\n",
        "ip = urllib.request.urlopen(\"https://ipv4.icanhazip.com\").read().decode(\"utf8\").strip()\n",
        "print(\"\\n=============================================\")\n",
        "print(\"👉 YOUR ENDPOINT IP (Password for Localtunnel):\", ip)\n",
        "print(\"=============================================\\n\")\n",
        "!npx localtunnel --port 8000"
      ]
    }
  ]
}
with open('YoutubeDownloader.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
