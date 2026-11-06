# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr80/merged | progress | 0.048 | -96 (74) | 29 of 102 (20 to 38) | 0.025 | -144 (57) | 17 of 102 (10 to 25) |
| data/combo/oft/thr80/merged | gru_phys_ttp | 0.025 | -48 (76) | 26 of 102 (18 to 35) | 0.012 | -80 (63) | 20 of 102 (12 to 28) |
| data/combo/oft/thr80/merged | or_progress_ttp | 0.038 | -72 (92) | 31 of 102 (22 to 40) | 0.019 | -96 (84) | 24 of 102 (16 to 33) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr80/merged | progress | 29 of 102 (20 to 38) | 45 / 28 |  | +96 (74) | 51 of 1071 (0.048) | 35 of 39 | 0.049 of 472 / 0.047 of 599 |
| data/combo/oft/thr80/merged | gru_phys_ttp | 26 of 102 (17 to 35) | 50 / 26 | -3 (-13 to +7) | +48 (76) | 27 of 1071 (0.025) | 8 of 39 | 0.006 of 472 / 0.040 of 599 |
| data/combo/oft/thr80/merged | or_progress_ttp | 31 of 102 (22 to 40) | 61 / 10 | +2 (-5 to +9) | +72 (92) | 41 of 1071 (0.038) | 33 of 39 | 0.032 of 472 / 0.043 of 599 |
