import os
import requests
import base64
import json

# This script demonstrates how to update a file on GitHub instantly using their REST API
# without needing to run `git push` or clone the repository! This is the "Bot Speed" method.

# INSTRUCTIONS:
# 1. Create a Personal Access Token (PAT) from GitHub Developer Settings
# 2. Set it as an environment variable: set GITHUB_TOKEN=your_token_here
# 3. Run: python github_api_updater.py

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = "RashidKhanApDev"
REPO_NAME = "UniversalMediaDownloader"
FILE_PATH = "dummy_file.txt"
BRANCH = "main"

def update_file_via_api(content, commit_message):
    if not GITHUB_TOKEN:
        print("❌ Error: GITHUB_TOKEN environment variable not set.")
        return

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

    # First, get the current SHA of the file (required to update it)
    print("🔍 Fetching current file state...")
    response = requests.get(url, headers=headers)
    
    sha = None
    if response.status_code == 200:
        sha = response.json()['sha']
        print(f"✅ Found existing file (SHA: {sha})")
    elif response.status_code == 404:
        print("ℹ️ File does not exist yet. Creating a new one...")
    else:
        print(f"❌ Failed to fetch file: {response.json()}")
        return

    # Now, encode the new content to base64
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")

    data = {
        "message": commit_message,
        "content": encoded_content,
        "branch": BRANCH
    }
    if sha:
        data["sha"] = sha

    # Send the PUT request to update/create the file
    print("🚀 Sending update via GitHub API...")
    put_response = requests.put(url, headers=headers, data=json.dumps(data))

    if put_response.status_code in [200, 201]:
        print("✅ SUCCESS! File updated instantly via API.")
        print(put_response.json()['commit']['html_url'])
    else:
        print(f"❌ Failed to update file: {put_response.json()}")

if __name__ == "__main__":
    print("🤖 GitHub API Fast Updater 🤖")
    test_content = "This file was updated instantly using the GitHub API! 🚀"
    test_message = "Automated API Update"
    update_file_via_api(test_content, test_message)
