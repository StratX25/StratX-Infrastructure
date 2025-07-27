import requests
import csv
import os
from datetime import datetime

# Load environment variables
bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
token = os.environ.get("PATTY")

# Repository details
owner = "StratX25"
repo = "StratX-Infrastructure"

# GitHub API headers
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to retrieve GitHub API data
def fetch(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()

# Retrieve repository metrics
views = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/views")
clones = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/clones")
referrers = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers")

# Trigger thresholds
min_clones = 3
min_refs = 1

# Compose and send Telegram message
if clones["uniques"] >= min_clones or len(referrers) >= min_refs:
    message = (
        f"📊 StratX Momentum Report:\n"
        f"- 🌟 Repo activity spike detected\n"
        f"- 🔁 Increased forks, stargazing & developer interest\n"
        f"- 📥 Unique repo access: {views['uniques']} | Top referrers: {len(referrers)}"
    )

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(telegram_url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else f"⚠️ Telegram failed: {r.status_code}")