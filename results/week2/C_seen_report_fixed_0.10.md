# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_seen_rescue | progress | 16 of 46 (10 to 22) | 26 / 4 |  | +88 (42) | 68 of 743 (0.092) | 25 of 27 | 0.097 of 472 / 0.081 of 271 |
| results/week2/C_seen_rescue | mlp_rescue | 13 of 46 (7 to 19) | 29 / 4 | -3 (-11 to +4) | +36 (42) | 58 of 743 (0.078) | 18 of 27 | 0.042 of 472 / 0.140 of 271 |
| results/week2/C_seen_rescue | combined_rescue | 14 of 46 (8 to 20) | 27 / 5 | -2 (-10 to +6) | +40 (41) | 104 of 743 (0.140) | 18 of 27 | 0.095 of 472 / 0.218 of 271 |
| results/week2/C_seen_rescue | mlp_rescue_cusum | 12 of 46 (6 to 18) | 32 / 2 | -4 (-11 to +3) | +40 (44) | 54 of 743 (0.073) | 18 of 27 | 0.042 of 472 / 0.125 of 271 |
| results/week2/C_seen_rescue | combined_rescue_cusum | 11 of 46 (6 to 17) | 29 / 6 | -5 (-12 to +2) | +40 (40) | 99 of 743 (0.133) | 18 of 27 | 0.093 of 472 / 0.203 of 271 |
| results/week2/C_seen_memory | progress | 16 of 46 (10 to 22) | 26 / 4 |  | +88 (42) | 68 of 743 (0.092) | 25 of 27 | 0.097 of 472 / 0.081 of 271 |
| results/week2/C_seen_memory | gru | 15 of 46 (9 to 21) | 26 / 5 | -1 (-8 to +6) | +56 (41) | 78 of 743 (0.105) | 16 of 27 | 0.055 of 472 / 0.192 of 271 |
| results/week2/C_seen_memory | conv | 15 of 46 (9 to 21) | 26 / 5 | -1 (-9 to +7) | +24 (41) | 72 of 743 (0.097) | 20 of 27 | 0.042 of 472 / 0.192 of 271 |
| results/week2/C_seen_memory | gru_cusum | 16 of 46 (10 to 22) | 25 / 5 | +0 (-7 to +7) | +56 (41) | 80 of 743 (0.108) | 18 of 27 | 0.064 of 472 / 0.185 of 271 |
| results/week2/C_seen_memory | conv_cusum | 14 of 46 (8 to 20) | 27 / 5 | -2 (-10 to +6) | +32 (41) | 70 of 743 (0.094) | 22 of 27 | 0.047 of 472 / 0.177 of 271 |
