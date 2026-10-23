# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_unseen_rescue | progress | 15 of 46 (9 to 21) | 27 / 4 |  | +92 (42) | 67 of 743 (0.090) | 25 of 27 | 0.097 of 472 / 0.077 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue | 3 of 46 (0 to 6) | 19 / 24 | -12 (-18 to -6) | +104 (22) | 17 of 743 (0.023) | 3 of 27 | 0.023 of 472 / 0.022 of 271 |
| results/week2/C_unseen_rescue | combined_rescue | 5 of 46 (1 to 9) | 3 / 38 | -10 (-17 to -3) | -120 (8) | 102 of 743 (0.137) | 2 of 27 | 0.112 of 472 / 0.181 of 271 |
| results/week2/C_unseen_rescue | mlp_rescue_cusum | 5 of 46 (1 to 9) | 30 / 11 | -10 (-16 to -5) | +80 (35) | 33 of 743 (0.044) | 9 of 27 | 0.038 of 472 / 0.055 of 271 |
| results/week2/C_unseen_rescue | combined_rescue_cusum | 7 of 46 (3 to 12) | 18 / 21 | -8 (-14 to -2) | +128 (25) | 43 of 743 (0.058) | 9 of 27 | 0.059 of 472 / 0.055 of 271 |
| results/week2/C_unseen_memory | progress | 15 of 46 (9 to 21) | 27 / 4 |  | +92 (42) | 67 of 743 (0.090) | 25 of 27 | 0.097 of 472 / 0.077 of 271 |
| results/week2/C_unseen_memory | gru | 16 of 46 (10 to 23) | 22 / 8 | +1 (-6 to +8) | +44 (38) | 127 of 743 (0.171) | 11 of 27 | 0.129 of 472 / 0.244 of 271 |
| results/week2/C_unseen_memory | conv | 15 of 46 (9 to 21) | 23 / 8 | +0 (-7 to +7) | +80 (38) | 117 of 743 (0.157) | 14 of 27 | 0.125 of 472 / 0.214 of 271 |
| results/week2/C_unseen_memory | gru_cusum | 14 of 46 (8 to 20) | 24 / 8 | -1 (-9 to +6) | +92 (38) | 103 of 743 (0.139) | 12 of 27 | 0.125 of 472 / 0.162 of 271 |
| results/week2/C_unseen_memory | conv_cusum | 15 of 46 (9 to 21) | 25 / 6 | +0 (-7 to +7) | +76 (40) | 110 of 743 (0.148) | 19 of 27 | 0.144 of 472 / 0.155 of 271 |
