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
        "Google Colab does not allow auto-running for security reasons. Please click the **Play (▶️)** button below to start the server. \n",
        "A popup will appear with your link once it's ready!"
      ],
      "metadata": {"id": "md1"}
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {"id": "code1"},
      "outputs": [],
      "source": [
        "!git clone https://github.com/RashidKhanApDev/YoutubeDownloader.git > /dev/null 2>&1\n",
        "%cd YoutubeDownloader\n",
        "!pip install -r requirements.txt > /dev/null 2>&1\n",
        "!npm install -g localtunnel > /dev/null 2>&1\n",
        "\n",
        "import subprocess\n",
        "import time\n",
        "import urllib.request\n",
        "from IPython.display import display, Javascript\n",
        "\n",
        "print(\"Starting Server... Please wait a moment...\")\n",
        "subprocess.Popen([\"python\", \"-m\", \"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)\n",
        "time.sleep(3)\n",
        "\n",
        "print(\"Generating Public Link...\")\n",
        "lt_process = subprocess.Popen([\"npx\", \"localtunnel\", \"--port\", \"8000\"], stdout=subprocess.PIPE, text=True)\n",
        "\n",
        "url = \"\"\n",
        "for line in lt_process.stdout:\n",
        "    if \"your url is\" in line.lower():\n",
        "        url = line.split(\"is\")[-1].strip()\n",
        "        break\n",
        "\n",
        "ip = urllib.request.urlopen(\"https://ipv4.icanhazip.com\").read().decode(\"utf8\").strip()\n",
        "\n",
        "print(\"\\n=============================================\")\n",
        "print(\"✅ SERVER IS READY!\")\n",
        "print(\"👉 Link:\", url)\n",
        "print(\"👉 Password:\", ip)\n",
        "print(\"=============================================\\n\")\n",
        "\n",
        "js_code = f\"\"\"\n",
        "const copyText = 'Link: {url}   |   Password: {ip}';\n",
        "prompt('✅ Server is Ready! Copy your Public Link & Password from below:', copyText);\n",
        "\"\"\"\n",
        "display(Javascript(js_code))\n",
        "\n",
        "# Keep tunnel alive\n",
        "lt_process.wait()\n"
      ]
    }
  ]
}

with open('YoutubeDownloader.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
