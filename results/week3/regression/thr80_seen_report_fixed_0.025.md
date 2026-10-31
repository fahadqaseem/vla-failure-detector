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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/seen | progress | 18 of 102 (11 to 26) | 40 / 44 |  | +128 (58) | 28 of 1071 (0.026) | 28 of 39 | 0.032 of 472 / 0.022 of 599 |
| data/week3_reg/thr80/seen | gru_phys | 35 of 102 (26 to 44) | 54 / 13 | +17 (+6 to +28) | +24 (89) | 23 of 1071 (0.021) | 16 of 39 | 0.006 of 472 / 0.033 of 599 |
| data/week3_reg/thr80/seen | gru_phys_frac | 35 of 102 (26 to 44) | 54 / 13 | +17 (+7 to +27) | +32 (89) | 25 of 1071 (0.023) | 18 of 39 | 0.013 of 472 / 0.032 of 599 |
| data/week3_reg/thr80/seen | gru_phys_ttp | 37 of 102 (28 to 47) | 50 / 15 | +19 (+8 to +30) | +32 (87) | 25 of 1071 (0.023) | 14 of 39 | 0.011 of 472 / 0.033 of 599 |
| data/week3_reg/thr80/seen | gru_robot | 29 of 102 (20 to 38) | 55 / 18 | +11 (+1 to +21) | +60 (84) | 21 of 1071 (0.020) | 16 of 39 | 0.013 of 472 / 0.025 of 599 |
| data/week3_reg/thr80/seen | gru_robotobj1 | 31 of 102 (22 to 40) | 56 / 15 | +13 (+3 to +23) | +40 (87) | 22 of 1071 (0.021) | 13 of 39 | 0.004 of 472 / 0.033 of 599 |
| data/week3_reg/thr80/seen | gru_robotobj2 | 30 of 102 (21 to 39) | 58 / 14 | +12 (+2 to +22) | +48 (88) | 26 of 1071 (0.024) | 14 of 39 | 0.006 of 472 / 0.038 of 599 |
