# StratX Core Simulator

This repository simulates the compliance and fallback logic of a sovereign-grade routing infrastructure using predefined transaction outcomes to test accuracy and enforcement integrity.

## 🔍 Key Features

- 50,000 total transactions simulated
- 1,276 predefined non-compliant (blocked) transactions
- 32,873 predefined fallback-triggering transactions
- 15,851 predefined compliant (allowed) transactions
- SHA256 hash verification for log integrity
- Modular policy system using JSON configuration

## 📂 Files

- `stratx_simulator.py` — Main simulation engine
- `example_policy.json` — Editable policy rule set
- `tx_predefined.csv` — Output of all simulated transactions
- `docs/execution_report.md` — Full execution summary
- `NOTICE.md` — IP protection and licensing terms

## 📄 Output Sample

| Metric            | Value     |
|-------------------|-----------|
| Avg. Latency      | 128.59 ms |
| Avg. Route Score  | 0.38      |
| Throughput        | 250 tx/s  |
| SHA256 Log Hash   | `84337b9e...de898` |

## 🔒 IP Notice

This repo contains simulated logic only. It does **not** reflect the proprietary routing core of the StratX system and is for demonstration purposes only.
