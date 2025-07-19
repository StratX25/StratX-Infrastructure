# 🧠 StratX Global Simulation – Summary (50,000 tx)

| Metric                      | Value                     |
|-----------------------------|---------------------------|
| Total Transactions          | 50,000                    |
| Global Regions Simulated    | US, EU, APAC, LATAM, MENA |
| Sanctions Blocks            | 2,586                     |
| Sovereign Fallbacks         | 1,903                     |
| Estimated Bundles Formed    | ~12,500                   |
| Avg Bundle Size             | ~4 tx                     |
| Avg Route Score             | ~0.51                     |
| Avg Latency                 | 62ms                      |
| Max Latency                 | 147ms                     |
| Total Simulation Time       | ~3m 20s                   |
| Estimated Throughput        | ~250 tx/sec               |
| SHA256 Hash (Log Verified)  | dfe7910a4a4d69f8f0bc3b6971071a8b545fae67b77c21749337dc82aa9f8d26 |

---

### 🔍 Notes:
- Logs reflect realistic fallback + sanctions behavior under simulated routing stress
- StratX policy engine deduplicated and rerouted in accordance with compliance thresholds
- RouteScore > 0.85 triggered review, fallback, or block
- Logs are available in [/proof/logs_batch_global_verified.txt](../proof/logs_batch_global_verified.txt)
