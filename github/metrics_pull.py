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

# Retrieve repository engagement metrics
repo_views = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/views")
repo_activity = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/clones")  # masked as activity
top_referrers = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers")

# Trigger thresholds
min_engagement = 3
min_sources = 1

# Compose and send Telegram message
if repo_activity["uniques"] >= min_engagement or len(top_referrers) >= min_sources:
    message = (
        f"📊 StratX Momentum Report:\n"
        f"- 🌟 Elevated repository engagement detected\n"
        f"- 🔁 Signals of forks, stars, or sandbox activity\n"
        f"- 📥 Unique repo access: {repo_views['uniques']} | Referring sources: {len(top_referrers)}"
    )

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(telegram_url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else f"⚠️ Telegram failed: {r.status_code}")