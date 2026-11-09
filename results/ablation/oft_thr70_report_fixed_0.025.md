# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr70/merged | progress | 0.048 | -108 (68) | 22 of 91 (14 to 30) | 0.025 | -156 (50) | 13 of 91 (7 to 20) |
| data/ablation/oft/thr70/merged | gru_phys_ttp | 0.018 | -80 (61) | 22 of 91 (14 to 30) | 0.007 | -96 (56) | 16 of 91 (9 to 23) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_goal | 0.159 | -112 (31) | 5 of 91 (1 to 9) | 0.156 | -120 (28) | 4 of 91 (1 to 8) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_pose | 0.031 | -104 (65) | 18 of 91 (11 to 26) | 0.009 | -120 (59) | 15 of 91 (8 to 22) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_contact | 0.013 | -80 (56) | 17 of 91 (10 to 25) | 0.007 | -120 (47) | 10 of 91 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr70/merged | progress | 13 of 91 (7 to 20) | 37 / 41 |  | +156 (50) | 27 of 1071 (0.025) | 25 of 35 | 0.030 of 472 / 0.022 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp | 16 of 91 (9 to 23) | 40 / 35 | +3 (-5 to +12) | +96 (56) | 8 of 1071 (0.007) | 4 of 35 | 0.000 of 472 / 0.013 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_goal | 4 of 91 (1 to 8) | 24 / 63 | -9 (-17 to -1) | +120 (28) | 167 of 1071 (0.156) | 0 of 35 | 0.104 of 472 / 0.197 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_pose | 15 of 91 (8 to 22) | 44 / 32 | +2 (-6 to +10) | +120 (59) | 10 of 1071 (0.009) | 4 of 35 | 0.011 of 472 / 0.008 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_contact | 10 of 91 (5 to 16) | 37 / 44 | -3 (-11 to +5) | +120 (47) | 8 of 1071 (0.007) | 5 of 35 | 0.000 of 472 / 0.013 of 599 |
