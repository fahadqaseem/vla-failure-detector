# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/C_seen_rescue | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/C_seen_rescue | mlp_rescue | 7 of 46 (3 to 12) | 33 / 6 | -4 (-11 to +3) | +72 (40) | 27 of 743 (0.036) | 11 of 27 | 0.019 of 472 / 0.066 of 271 |
| results/week2/C_seen_rescue | combined_rescue | 9 of 46 (4 to 14) | 32 / 5 | -2 (-9 to +5) | +56 (41) | 46 of 743 (0.062) | 14 of 27 | 0.032 of 472 / 0.114 of 271 |
| results/week2/C_seen_rescue | mlp_rescue_cusum | 5 of 46 (1 to 9) | 34 / 7 | -6 (-12 to +0) | +72 (39) | 25 of 743 (0.034) | 11 of 27 | 0.019 of 472 / 0.059 of 271 |
| results/week2/C_seen_rescue | combined_rescue_cusum | 8 of 46 (3 to 13) | 30 / 8 | -3 (-9 to +3) | +64 (38) | 46 of 743 (0.062) | 14 of 27 | 0.036 of 472 / 0.107 of 271 |
| results/week2/C_seen_memory | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/C_seen_memory | gru | 11 of 46 (6 to 17) | 29 / 6 | +0 (-8 to +8) | +64 (40) | 39 of 743 (0.052) | 13 of 27 | 0.028 of 472 / 0.096 of 271 |
| results/week2/C_seen_memory | conv | 10 of 46 (5 to 16) | 30 / 6 | -1 (-9 to +7) | +48 (40) | 37 of 743 (0.050) | 14 of 27 | 0.021 of 472 / 0.100 of 271 |
| results/week2/C_seen_memory | gru_cusum | 9 of 46 (4 to 15) | 30 / 7 | -2 (-9 to +5) | +64 (39) | 36 of 743 (0.048) | 15 of 27 | 0.028 of 472 / 0.085 of 271 |
| results/week2/C_seen_memory | conv_cusum | 10 of 46 (5 to 16) | 30 / 6 | -1 (-9 to +7) | +48 (40) | 40 of 743 (0.054) | 15 of 27 | 0.025 of 472 / 0.103 of 271 |
