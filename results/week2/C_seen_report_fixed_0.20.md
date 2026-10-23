# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_seen_rescue | progress | 16 of 46 (10 to 22) | 28 / 2 |  | +60 (44) | 98 of 743 (0.132) | 26 of 27 | 0.146 of 472 / 0.107 of 271 |
| results/week2/C_seen_rescue | mlp_rescue | 21 of 46 (15 to 28) | 23 / 2 | +5 (-3 to +13) | +8 (44) | 121 of 743 (0.163) | 18 of 27 | 0.102 of 472 / 0.269 of 271 |
| results/week2/C_seen_rescue | combined_rescue | 24 of 46 (17 to 30) | 21 / 1 | +8 (+0 to +16) | +0 (45) | 156 of 743 (0.210) | 21 of 27 | 0.146 of 472 / 0.321 of 271 |
| results/week2/C_seen_rescue | mlp_rescue_cusum | 19 of 46 (13 to 26) | 25 / 2 | +3 (-4 to +11) | +16 (44) | 122 of 743 (0.164) | 18 of 27 | 0.102 of 472 / 0.273 of 271 |
| results/week2/C_seen_rescue | combined_rescue_cusum | 17 of 46 (11 to 24) | 28 / 1 | +1 (-6 to +9) | +16 (45) | 160 of 743 (0.215) | 21 of 27 | 0.148 of 472 / 0.332 of 271 |
| results/week2/C_seen_memory | progress | 16 of 46 (10 to 22) | 28 / 2 |  | +60 (44) | 98 of 743 (0.132) | 26 of 27 | 0.146 of 472 / 0.107 of 271 |
| results/week2/C_seen_memory | gru | 21 of 46 (15 to 28) | 20 / 5 | +5 (-3 to +13) | +0 (41) | 136 of 743 (0.183) | 22 of 27 | 0.106 of 472 / 0.317 of 271 |
| results/week2/C_seen_memory | conv | 25 of 46 (19 to 32) | 19 / 2 | +9 (+2 to +17) | -4 (44) | 143 of 743 (0.192) | 25 of 27 | 0.112 of 472 / 0.332 of 271 |
| results/week2/C_seen_memory | gru_cusum | 18 of 46 (12 to 25) | 23 / 5 | +2 (-6 to +10) | +32 (41) | 136 of 743 (0.183) | 22 of 27 | 0.114 of 472 / 0.303 of 271 |
| results/week2/C_seen_memory | conv_cusum | 24 of 46 (18 to 31) | 20 / 2 | +8 (+1 to +15) | -4 (44) | 143 of 743 (0.192) | 25 of 27 | 0.112 of 472 / 0.332 of 271 |
