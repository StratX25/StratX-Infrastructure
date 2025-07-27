import requests
import csv
import os
from datetime import datetime

token = os.environ.get("GITHUB_TOKEN")
owner = "StratX25"
repo = "StratX-Infrastructure"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

urls = {
    "views": f"https://api.github.com/repos/{owner}/{repo}/traffic/views",
    "clones": f"https://api.github.com/repos/{owner}/{repo}/traffic/clones",
    "referrers": f"https://api.github.com/repos/{owner}/{repo}/traffic/popular/referrers"
}

def fetch(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()

data = {k: fetch(v) for k, v in urls.items()}
log_file = "logs/metrics.csv"
os.makedirs("logs", exist_ok=True)
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Views (Unique)", "Views (Total)", "Clones (Unique)", "Clones (Total)", "Top Referrers"])

with open(log_file, "a", newline="") as f:
    writer = csv.writer(f)
    top_refs = ", ".join([r["referrer"] for r in data["referrers"][:3]]) if data["referrers"] else "N/A"
    writer.writerow([timestamp, data["views"]["uniques"], data["views"]["count"], data["clones"]["uniques"], data["clones"]["count"], top_refs])
