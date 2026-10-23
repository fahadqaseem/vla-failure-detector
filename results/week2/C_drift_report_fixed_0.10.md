# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_drift_natural | progress | 16 of 46 (10 to 22) | 26 / 4 |  | +88 (42) | 59 of 743 (0.079) | 25 of 27 | 0.083 of 472 / 0.074 of 271 |
| results/week2/C_drift_natural | safe | 22 of 46 (15 to 29) | 23 / 1 | +6 (-2 to +14) | +8 (45) | 108 of 743 (0.145) | 25 of 27 | 0.093 of 472 / 0.236 of 271 |
| results/week2/C_drift_natural | mlp | 13 of 46 (7 to 19) | 27 / 6 | -3 (-11 to +5) | +44 (40) | 73 of 743 (0.098) | 15 of 27 | 0.051 of 472 / 0.181 of 271 |
| results/week2/C_drift_natural | combined | 27 of 46 (20 to 33) | 16 / 3 | +11 (+2 to +20) | -40 (43) | 317 of 743 (0.427) | 24 of 27 | 0.345 of 472 / 0.568 of 271 |
| results/week2/C_drift_natural | mlp_cusum | 13 of 46 (7 to 19) | 27 / 6 | -3 (-11 to +5) | +44 (40) | 72 of 743 (0.097) | 15 of 27 | 0.051 of 472 / 0.177 of 271 |
| results/week2/C_drift_natural | combined_cusum | 22 of 46 (16 to 29) | 21 / 3 | +6 (-2 to +14) | +0 (43) | 314 of 743 (0.423) | 24 of 27 | 0.343 of 472 / 0.561 of 271 |
| results/week2/C_drift_pooled | progress | 16 of 46 (10 to 22) | 26 / 4 |  | +88 (42) | 68 of 743 (0.092) | 25 of 27 | 0.097 of 472 / 0.081 of 271 |
| results/week2/C_drift_pooled | safe | 16 of 46 (10 to 22) | 29 / 1 | +0 (-7 to +7) | +24 (45) | 60 of 743 (0.081) | 25 of 27 | 0.051 of 472 / 0.133 of 271 |
| results/week2/C_drift_pooled | mlp | 10 of 46 (5 to 16) | 28 / 8 | -6 (-14 to +2) | +48 (38) | 37 of 743 (0.050) | 11 of 27 | 0.023 of 472 / 0.096 of 271 |
| results/week2/C_drift_pooled | combined | 23 of 46 (17 to 30) | 20 / 3 | +7 (-1 to +15) | -8 (43) | 227 of 743 (0.306) | 22 of 27 | 0.231 of 472 / 0.435 of 271 |
| results/week2/C_drift_pooled | mlp_cusum | 10 of 46 (5 to 16) | 28 / 8 | -6 (-14 to +2) | +48 (38) | 38 of 743 (0.051) | 13 of 27 | 0.023 of 472 / 0.100 of 271 |
| results/week2/C_drift_pooled | combined_cusum | 21 of 46 (14 to 28) | 22 / 3 | +5 (-3 to +13) | +8 (43) | 224 of 743 (0.301) | 23 of 27 | 0.235 of 472 / 0.417 of 271 |
