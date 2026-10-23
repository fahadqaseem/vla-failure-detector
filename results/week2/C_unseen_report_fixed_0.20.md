# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_unseen_rescue | progress | 17 of 46 (11 to 24) | 27 / 2 |  | +40 (44) | 116 of 743 (0.156) | 26 of 27 | 0.184 of 472 / 0.107 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue | 11 of 46 (6 to 17) | 27 / 8 | -6 (-14 to +2) | +52 (38) | 146 of 743 (0.197) | 11 of 27 | 0.157 of 472 / 0.266 of 271 |
| results/week2/C_unseen_rescue | combined_rescue | 14 of 46 (8 to 20) | 30 / 2 | -3 (-10 to +4) | +56 (44) | 146 of 743 (0.197) | 17 of 27 | 0.169 of 472 / 0.244 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue_cusum | 12 of 46 (6 to 18) | 30 / 4 | -5 (-13 to +2) | +48 (42) | 134 of 743 (0.180) | 13 of 27 | 0.155 of 472 / 0.225 of 271 |
| results/week2/C_unseen_rescue | combined_rescue_cusum | 11 of 46 (6 to 17) | 30 / 5 | -6 (-12 to +0) | +72 (41) | 114 of 743 (0.153) | 18 of 27 | 0.159 of 472 / 0.144 of 271 |
| results/week2/C_unseen_memory | progress | 17 of 46 (11 to 24) | 27 / 2 |  | +40 (44) | 116 of 743 (0.156) | 26 of 27 | 0.184 of 472 / 0.107 of 271 |
| results/week2/C_unseen_memory | gru | 20 of 46 (14 to 27) | 23 / 3 | +3 (-4 to +11) | +16 (43) | 206 of 743 (0.277) | 13 of 27 | 0.227 of 472 / 0.365 of 271 |
| results/week2/C_unseen_memory | conv | 20 of 46 (14 to 27) | 24 / 2 | +3 (-5 to +11) | +44 (44) | 175 of 743 (0.236) | 19 of 27 | 0.193 of 472 / 0.310 of 271 |
| results/week2/C_unseen_memory | gru_cusum | 21 of 46 (15 to 28) | 23 / 2 | +4 (-4 to +12) | +20 (44) | 190 of 743 (0.256) | 19 of 27 | 0.214 of 472 / 0.328 of 271 |
| results/week2/C_unseen_memory | conv_cusum | 19 of 46 (13 to 26) | 24 / 3 | +2 (-6 to +10) | +40 (43) | 182 of 743 (0.245) | 24 of 27 | 0.210 of 472 / 0.306 of 271 |
