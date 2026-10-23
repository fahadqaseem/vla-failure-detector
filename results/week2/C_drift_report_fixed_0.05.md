# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_drift_natural | progress | 11 of 46 (6 to 17) | 26 / 9 |  | +136 (37) | 32 of 743 (0.043) | 23 of 27 | 0.047 of 472 / 0.037 of 271 |
| results/week2/C_drift_natural | safe | 16 of 46 (10 to 22) | 29 / 1 | +5 (-2 to +12) | +24 (45) | 55 of 743 (0.074) | 25 of 27 | 0.044 of 472 / 0.125 of 271 |
| results/week2/C_drift_natural | mlp | 9 of 46 (4 to 15) | 29 / 8 | -2 (-9 to +5) | +68 (38) | 33 of 743 (0.044) | 11 of 27 | 0.021 of 472 / 0.085 of 271 |
| results/week2/C_drift_natural | combined | 23 of 46 (17 to 30) | 20 / 3 | +12 (+4 to +20) | -8 (43) | 215 of 743 (0.289) | 20 of 27 | 0.222 of 472 / 0.406 of 271 |
| results/week2/C_drift_natural | mlp_cusum | 9 of 46 (4 to 15) | 29 / 8 | -2 (-9 to +5) | +68 (38) | 32 of 743 (0.043) | 11 of 27 | 0.021 of 472 / 0.081 of 271 |
| results/week2/C_drift_natural | combined_cusum | 21 of 46 (14 to 28) | 22 / 3 | +10 (+2 to +18) | +8 (43) | 212 of 743 (0.285) | 21 of 27 | 0.218 of 472 / 0.402 of 271 |
| results/week2/C_drift_pooled | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/C_drift_pooled | safe | 13 of 46 (7 to 19) | 31 / 2 | +2 (-5 to +9) | +48 (44) | 33 of 743 (0.044) | 24 of 27 | 0.023 of 472 / 0.081 of 271 |
| results/week2/C_drift_pooled | mlp | 4 of 46 (1 to 8) | 34 / 8 | -7 (-13 to -1) | +84 (38) | 19 of 743 (0.026) | 7 of 27 | 0.013 of 472 / 0.048 of 271 |
| results/week2/C_drift_pooled | combined | 19 of 46 (13 to 26) | 23 / 4 | +8 (-1 to +16) | +16 (42) | 152 of 743 (0.205) | 18 of 27 | 0.148 of 472 / 0.303 of 271 |
| results/week2/C_drift_pooled | mlp_cusum | 5 of 46 (1 to 9) | 33 / 8 | -6 (-12 to +0) | +84 (38) | 16 of 743 (0.022) | 9 of 27 | 0.013 of 472 / 0.037 of 271 |
| results/week2/C_drift_pooled | combined_cusum | 17 of 46 (11 to 24) | 25 / 4 | +6 (-2 to +14) | +16 (42) | 151 of 743 (0.203) | 18 of 27 | 0.148 of 472 / 0.299 of 271 |
