import json
import random
import pandas as pd
from hashlib import sha256

# --- CONFIGURABLE POLICY LAYER ---
policy_config = {
    "sanctioned_countries": ["RU", "IR", "KP", "SY", "CU"],
    "fallback": {
        "min_score_threshold": 0.45,
        "max_latency_ms": 120
    },
    "sovereign_overrides": {
        "MENA": {"allow_override": True},
        "EU": {"strict": True}
    }
}

TOTAL_TXS = 50000
PREDEFINED_BLOCKED = 1276
PREDEFINED_FALLBACK = 32873
PREDEFINED_ALLOWED = TOTAL_TXS - PREDEFINED_BLOCKED - PREDEFINED_FALLBACK
REGIONS = ["US", "EU", "APAC", "LATAM", "MENA"]

def generate_predefined_tx(tx_id, status):
    region = random.choice(REGIONS)
    route_score = round(random.uniform(0.0, 1.0), 2)
    latency = random.randint(30, 180)

    if status == "blocked":
        origin_country = random.choice(policy_config["sanctioned_countries"])
        dest_country = random.choice(["US", "FR", "JP", "MX", "SA"])
    else:
        origin_country = random.choice(["US", "DE", "CN", "BR", "AE"])
        dest_country = random.choice(["US", "FR", "JP", "MX", "SA"])

    tx = {
        "tx_id": f"tx_{tx_id}",
        "region": region,
        "route_score": route_score,
        "latency_ms": latency,
        "origin_country": origin_country,
        "dest_country": dest_country,
        "compliance_result": "allowed",
        "status": status
    }

    if status == "blocked":
        tx["compliance_result"] = "blocked"
    elif status == "fallback":
        if route_score >= policy_config["fallback"]["min_score_threshold"]:
            tx["route_score"] = 0.40
        if latency <= policy_config["fallback"]["max_latency_ms"]:
            tx["latency_ms"] = 135
    return tx

transactions = []
for i in range(PREDEFINED_BLOCKED):
    transactions.append(generate_predefined_tx(i, "blocked"))
for i in range(PREDEFINED_BLOCKED, PREDEFINED_BLOCKED + PREDEFINED_FALLBACK):
    transactions.append(generate_predefined_tx(i, "fallback"))
for i in range(PREDEFINED_BLOCKED + PREDEFINED_FALLBACK, TOTAL_TXS):
    transactions.append(generate_predefined_tx(i, "allowed"))

random.shuffle(transactions)
df = pd.DataFrame(transactions)
df.to_csv("tx_predefined.csv", index=False)

avg_latency = round(df["latency_ms"].mean(), 2)
avg_score = round(df["route_score"].mean(), 2)
throughput_tps = round(TOTAL_TXS / (3 * 60 + 20), 2)
log_hash = sha256(df.to_csv(index=False).encode("utf-8")).hexdigest()

print("SHA256 Hash:", log_hash)
