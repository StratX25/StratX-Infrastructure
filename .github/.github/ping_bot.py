import requests
import os

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
message = "✅ StratX Bot is live. Engagement tracker online."

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
params = {"chat_id": chat_id, "text": message}

r = requests.post(url, params=params)
print("✅ Verification message sent!" if r.status_code == 200 else f"❌ Telegram error: {r.status_code}")