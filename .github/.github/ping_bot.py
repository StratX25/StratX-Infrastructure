import requests
import os

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
message = "🚀 StratX Bot Triggered: Tracker is now active"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
params = {"chat_id": chat_id, "text": message}

r = requests.post(url, params=params)
print("✅ Message sent!" if r.status_code == 200 else f"❌ Error: {r.status_code}")