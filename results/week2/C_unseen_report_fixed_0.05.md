# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_unseen_rescue | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue | 2 of 46 (0 to 5) | 12 / 32 | -9 (-15 to -3) | +128 (14) | 7 of 743 (0.009) | 1 of 27 | 0.008 of 472 / 0.011 of 271 |
| results/week2/C_unseen_rescue | combined_rescue | 4 of 46 (1 to 8) | 4 / 38 | -7 (-14 to +0) | -16 (8) | 89 of 743 (0.120) | 2 of 27 | 0.091 of 472 / 0.170 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue_cusum | 4 of 46 (1 to 8) | 25 / 17 | -7 (-13 to -2) | +88 (29) | 11 of 743 (0.015) | 9 of 27 | 0.011 of 472 / 0.022 of 271 |
| results/week2/C_unseen_rescue | combined_rescue_cusum | 4 of 46 (1 to 8) | 9 / 33 | -7 (-14 to +0) | +64 (13) | 18 of 743 (0.024) | 5 of 27 | 0.023 of 472 / 0.026 of 271 |
| results/week2/C_unseen_memory | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/C_unseen_memory | gru | 12 of 46 (6 to 18) | 23 / 11 | +1 (-5 to +7) | +80 (35) | 67 of 743 (0.090) | 9 of 27 | 0.061 of 472 / 0.140 of 271 |
| results/week2/C_unseen_memory | conv | 8 of 46 (3 to 13) | 26 / 12 | -3 (-9 to +3) | +112 (34) | 87 of 743 (0.117) | 10 of 27 | 0.085 of 472 / 0.173 of 271 |
| results/week2/C_unseen_memory | gru_cusum | 11 of 46 (6 to 17) | 21 / 14 | +0 (-5 to +5) | +96 (32) | 57 of 743 (0.077) | 8 of 27 | 0.064 of 472 / 0.100 of 271 |
| results/week2/C_unseen_memory | conv_cusum | 12 of 46 (6 to 18) | 23 / 11 | +1 (-5 to +7) | +88 (35) | 58 of 743 (0.078) | 16 of 27 | 0.072 of 472 / 0.089 of 271 |
