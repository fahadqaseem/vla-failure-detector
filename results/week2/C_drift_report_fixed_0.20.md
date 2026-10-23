# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_drift_natural | progress | 16 of 46 (10 to 22) | 28 / 2 |  | +60 (44) | 98 of 743 (0.132) | 26 of 27 | 0.146 of 472 / 0.107 of 271 |
| results/week2/C_drift_natural | safe | 31 of 46 (25 to 37) | 14 / 1 | +15 (+7 to +23) | -128 (45) | 179 of 743 (0.241) | 25 of 27 | 0.176 of 472 / 0.354 of 271 |
| results/week2/C_drift_natural | mlp | 21 of 46 (15 to 28) | 21 / 4 | +5 (-3 to +13) | +4 (42) | 135 of 743 (0.182) | 17 of 27 | 0.112 of 472 / 0.303 of 271 |
| results/week2/C_drift_natural | combined | 35 of 46 (29 to 40) | 9 / 2 | +19 (+11 to +27) | -100 (44) | 419 of 743 (0.564) | 24 of 27 | 0.475 of 472 / 0.720 of 271 |
| results/week2/C_drift_natural | mlp_cusum | 19 of 46 (13 to 26) | 23 / 4 | +3 (-5 to +11) | +12 (42) | 135 of 743 (0.182) | 18 of 27 | 0.119 of 472 / 0.292 of 271 |
| results/week2/C_drift_natural | combined_cusum | 33 of 46 (27 to 39) | 11 / 2 | +17 (+9 to +24) | -100 (44) | 413 of 743 (0.556) | 24 of 27 | 0.466 of 472 / 0.712 of 271 |
| results/week2/C_drift_pooled | progress | 16 of 46 (10 to 22) | 28 / 2 |  | +60 (44) | 98 of 743 (0.132) | 26 of 27 | 0.146 of 472 / 0.107 of 271 |
| results/week2/C_drift_pooled | safe | 27 of 46 (20 to 34) | 18 / 1 | +11 (+3 to +19) | -40 (45) | 132 of 743 (0.178) | 25 of 27 | 0.123 of 472 / 0.273 of 271 |
| results/week2/C_drift_pooled | mlp | 17 of 46 (11 to 23) | 23 / 6 | +1 (-7 to +9) | +16 (40) | 95 of 743 (0.128) | 16 of 27 | 0.076 of 472 / 0.218 of 271 |
| results/week2/C_drift_pooled | combined | 33 of 46 (27 to 39) | 11 / 2 | +17 (+9 to +25) | -92 (44) | 348 of 743 (0.468) | 24 of 27 | 0.379 of 472 / 0.624 of 271 |
| results/week2/C_drift_pooled | mlp_cusum | 15 of 46 (9 to 21) | 26 / 5 | -1 (-9 to +7) | +16 (41) | 92 of 743 (0.124) | 16 of 27 | 0.074 of 472 / 0.210 of 271 |
| results/week2/C_drift_pooled | combined_cusum | 32 of 46 (26 to 38) | 12 / 2 | +16 (+9 to +23) | -52 (44) | 351 of 743 (0.472) | 24 of 27 | 0.392 of 472 / 0.613 of 271 |
