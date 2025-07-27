import requests
import os
from datetime import datetime

# Load secrets from GitHub
bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
token = os.environ.get("PATTY")

# Repo details
owner = "StratX25"
repo = "StratX-Infrastructure"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch GitHub metrics
def fetch(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()

views = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/views")
activity = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/clones")
referrers = fetch(f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers")

# Trigger conditions
min_engagement = 3
min_sources = 1

# Telegram message
if activity["uniques"] >= min_engagement or len(referrers) >= min_sources:
    message = (
        f"📊 StratX Momentum Report:\n"
        f"- 🌟 Elevated repository engagement detected\n"
        f"- 🔁 Signals of forks, stars, or sandbox activity\n"
        f"- 📥 Unique repo access: {views['uniques']} | Referring sources: {len(referrers)}"
    )

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else f"⚠️ Telegram failed: {r.status_code}")
