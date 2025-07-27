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

# --- Telegram Alert Logic ---
min_clones = 3
min_refs = 1

# Later in your script (after data collection logic)
# Make sure this is placed AFTER your data object has been defined

if data["clones"]["uniques"] >= min_clones or len(data["referrers"]) >= min_refs:
    message = f"📈 StratX Alert:\\nViews: {data['views']['uniques']}, Clones: {data['clones']['uniques']}, Refs: {len(data['referrers'])}"
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(telegram_url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else f"⚠️ Telegram failed: {r.status_code}")
