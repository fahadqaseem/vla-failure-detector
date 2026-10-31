# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/seen | progress | 0.046 | -104 (76) | 28 of 102 (19 to 37) | 0.026 | -128 (58) | 18 of 102 (11 to 26) |
| data/week3_reg/thr80/seen | gru_phys | 0.040 | +0 (95) | 49 of 102 (39 to 59) | 0.021 | -24 (89) | 35 of 102 (26 to 44) |
| data/week3_reg/thr80/seen | gru_phys_frac | 0.047 | +0 (96) | 52 of 102 (42 to 62) | 0.023 | -32 (89) | 35 of 102 (26 to 45) |
| data/week3_reg/thr80/seen | gru_phys_ttp | 0.054 | +0 (97) | 51 of 102 (41 to 61) | 0.023 | -32 (87) | 37 of 102 (28 to 47) |
| data/week3_reg/thr80/seen | gru_robot | 0.044 | -40 (94) | 38 of 102 (29 to 48) | 0.020 | -60 (84) | 29 of 102 (20 to 38) |
| data/week3_reg/thr80/seen | gru_robotobj1 | 0.050 | -24 (93) | 38 of 102 (29 to 48) | 0.021 | -40 (87) | 31 of 102 (22 to 40) |
| data/week3_reg/thr80/seen | gru_robotobj2 | 0.042 | -24 (94) | 38 of 102 (29 to 48) | 0.024 | -48 (88) | 30 of 102 (21 to 39) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/seen | progress | 28 of 102 (19 to 37) | 48 / 26 |  | +104 (76) | 49 of 1071 (0.046) | 33 of 39 | 0.049 of 472 / 0.043 of 599 |
| data/week3_reg/thr80/seen | gru_phys | 49 of 102 (39 to 59) | 46 / 7 | +21 (+11 to +31) | +0 (95) | 43 of 1071 (0.040) | 17 of 39 | 0.021 of 472 / 0.055 of 599 |
| data/week3_reg/thr80/seen | gru_phys_frac | 52 of 102 (42 to 62) | 44 / 6 | +24 (+13 to +35) | +0 (96) | 50 of 1071 (0.047) | 27 of 39 | 0.030 of 472 / 0.060 of 599 |
| data/week3_reg/thr80/seen | gru_phys_ttp | 51 of 102 (41 to 61) | 46 / 5 | +23 (+12 to +34) | +0 (97) | 58 of 1071 (0.054) | 18 of 39 | 0.028 of 472 / 0.075 of 599 |
| data/week3_reg/thr80/seen | gru_robot | 38 of 102 (28 to 48) | 56 / 8 | +10 (+0 to +20) | +40 (94) | 47 of 1071 (0.044) | 18 of 39 | 0.025 of 472 / 0.058 of 599 |
| data/week3_reg/thr80/seen | gru_robotobj1 | 38 of 102 (29 to 48) | 55 / 9 | +10 (-1 to +21) | +24 (93) | 54 of 1071 (0.050) | 15 of 39 | 0.021 of 472 / 0.073 of 599 |
| data/week3_reg/thr80/seen | gru_robotobj2 | 38 of 102 (29 to 48) | 56 / 8 | +10 (-1 to +21) | +24 (94) | 45 of 1071 (0.042) | 16 of 39 | 0.017 of 472 / 0.062 of 599 |
