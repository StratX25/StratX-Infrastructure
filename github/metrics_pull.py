import requests
import csv
import os
from datetime import datetime

# Load secrets securely
bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
token = os.environ.get("GITHUB_PAT") or os.environ.get("GITHUB_TOKEN")

# Telegram alert logic (FREE)

bot_token = os.environ.get("8461268130:AAF8FSAegC45r8_GhnUJ-3CKilCJHFozyVo")
chat_id = "6468476747"  # Abel Oliveira
min_clones = 3
min_refs = 1

if data["clones"]["uniques"] >= min_clones or len(data["referrers"]) >= min_refs:
    message = f"📈 StratX Alert:\nViews: {data['views']['uniques']}, Clones: {data['clones']['uniques']}, Refs: {len(data['referrers'])}"
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    r = requests.post(telegram_url, params=params)
    print("✅ Telegram alert sent" if r.status_code == 200 else "⚠️ Telegram failed", r.status_code)

