# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/ablation/pi05/thr50/merged | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| data/ablation/pi05/thr50/merged | gru_phys_ttp | 0.009 | +96 (15) | 9 of 27 (4 to 14) | 0.005 | +64 (15) | 8 of 27 (4 to 13) |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_goal | 0.001 | +116 (2) | 2 of 27 (0 to 5) | 0.001 | +40 (1) | 1 of 27 (0 to 3) |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_pose | 0.012 | -32 (18) | 9 of 27 (4 to 14) | 0.006 | -32 (15) | 7 of 27 (3 to 12) |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_contact | 0.012 | +40 (17) | 9 of 27 (4 to 14) | 0.011 | +56 (15) | 8 of 27 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/ablation/pi05/thr50/merged | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| data/ablation/pi05/thr50/merged | gru_phys_ttp | 8 of 27 (4 to 13) | 7 / 12 | +6 (+1 to +11) | -64 (15) | 5 of 928 (0.005) | 1 of 7 | 0.004 of 475 / 0.007 of 453 |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_goal | 1 of 27 (0 to 3) | 0 / 26 | -1 (-3 to +0) | -40 (1) | 1 of 928 (0.001) | 0 of 7 | 0.000 of 475 / 0.002 of 453 |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_pose | 7 of 27 (3 to 12) | 8 / 12 | +5 (+0 to +10) | +32 (15) | 6 of 928 (0.006) | 0 of 7 | 0.002 of 475 / 0.011 of 453 |
| data/ablation/pi05/thr50/merged | gru_phys_ttp_no_contact | 8 of 27 (4 to 13) | 7 / 12 | +6 (+1 to +11) | -56 (15) | 10 of 928 (0.011) | 1 of 7 | 0.006 of 475 / 0.015 of 453 |
