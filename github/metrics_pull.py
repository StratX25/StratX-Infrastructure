import requests
import csv
import os
from datetime import datetime

# Load secrets from GitHub Actions
bot_token = os.environ.get("BOT_TOKEN")         # Telegram bot token (from secret)
chat_id = os.environ.get("CHAT_ID")             # Telegram chat ID (from secret)
token = os.environ.get("PATTY")                 # GitHub PAT (from secret)

# Define repo info
owner = "StratX25"
repo = "StratX-Infrastructure"

# GitHub API headers
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# --- Fetch GitHub Traffic Data ---
def fetch(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()

# Grab traffic data from GitHub
data = {
    "views": fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/views"),
    "clones": fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/clones"),
    "referrers": fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers")
}

# --- Telegram Alert Logic (safe and secure) ---
min_clones = 3
min_refs = 1

if data["clones"]["uniques"] >= min_clones or len(data["referrers"]) >= min_refs:
    message = f"📈 StratX Alert:\\nViews: {data['views']['uniques']}, Clones: {data['clones']['uniques']}, Refs: {len(data['referrers'])}"
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(telegram_url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else f"⚠️ Telegram failed: {r.status_code}")
