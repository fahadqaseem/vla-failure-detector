# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr50/merged | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| data/ablation/oft/thr50/merged | gru_phys_ttp | 0.054 | -120 (49) | 11 of 81 (5 to 17) | 0.007 | -120 (45) | 10 of 81 (5 to 16) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_goal | 0.097 | -140 (22) | 1 of 81 (0 to 3) | 0.053 | -176 (21) | 0 of 81 (0 to 0) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_pose | 0.048 | -160 (30) | 4 of 81 (1 to 8) | 0.048 | -160 (28) | 4 of 81 (1 to 8) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_contact | 0.038 | -64 (43) | 12 of 81 (6 to 18) | 0.008 | -72 (40) | 11 of 81 (5 to 17) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr50/merged | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp | 11 of 81 (5 to 17) | 38 / 32 | -6 (-14 to +2) | +120 (49) | 58 of 1071 (0.054) | 2 of 31 | 0.108 of 472 / 0.012 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_goal | 1 of 81 (0 to 3) | 21 / 59 | -16 (-23 to -9) | +140 (22) | 104 of 1071 (0.097) | 0 of 31 | 0.061 of 472 / 0.125 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_pose | 4 of 81 (1 to 8) | 26 / 51 | -13 (-21 to -6) | +160 (30) | 51 of 1071 (0.048) | 1 of 31 | 0.104 of 472 / 0.003 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_contact | 12 of 81 (6 to 19) | 31 / 38 | -5 (-12 to +2) | +64 (43) | 41 of 1071 (0.038) | 3 of 31 | 0.061 of 472 / 0.020 of 599 |
