# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/seen/merged | progress | 0.046 | -104 (76) | 28 of 102 (19 to 37) | 0.026 | -128 (58) | 18 of 102 (11 to 26) |
| data/realistic/oft/thr80/seen/merged | gru_phys_ttp | 0.054 | +0 (97) | 51 of 102 (41 to 61) | 0.023 | -32 (87) | 37 of 102 (28 to 47) |
| data/realistic/oft/thr80/seen/merged | gru_robot_ttp | 0.047 | -40 (92) | 33 of 102 (24 to 42) | 0.022 | -56 (87) | 27 of 102 (19 to 36) |
| data/realistic/oft/thr80/seen/merged | gru_robotcontact_ttp | 0.047 | -24 (96) | 41 of 102 (31 to 51) | 0.021 | -36 (90) | 30 of 102 (21 to 39) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/seen/merged | progress | 28 of 102 (19 to 37) | 48 / 26 |  | +104 (76) | 49 of 1071 (0.046) | 33 of 39 | 0.049 of 472 / 0.043 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_phys_ttp | 51 of 102 (41 to 61) | 46 / 5 | +23 (+12 to +34) | +0 (97) | 58 of 1071 (0.054) | 18 of 39 | 0.028 of 472 / 0.075 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_robot_ttp | 33 of 102 (24 to 42) | 59 / 10 | +5 (-5 to +15) | +40 (92) | 50 of 1071 (0.047) | 17 of 39 | 0.034 of 472 / 0.057 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_robotcontact_ttp | 41 of 102 (31 to 50) | 55 / 6 | +13 (+2 to +23) | +24 (96) | 50 of 1071 (0.047) | 16 of 39 | 0.025 of 472 / 0.063 of 599 |
