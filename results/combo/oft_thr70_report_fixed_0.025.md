# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr70/merged | progress | 0.048 | -108 (68) | 22 of 91 (14 to 30) | 0.025 | -156 (50) | 13 of 91 (7 to 20) |
| data/combo/oft/thr70/merged | gru_phys_ttp | 0.017 | -84 (60) | 21 of 91 (14 to 29) | 0.007 | -96 (57) | 16 of 91 (9 to 24) |
| data/combo/oft/thr70/merged | or_progress_ttp | 0.034 | -92 (80) | 26 of 91 (18 to 35) | 0.019 | -128 (74) | 21 of 91 (14 to 29) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr70/merged | progress | 13 of 91 (7 to 20) | 37 / 41 |  | +156 (50) | 27 of 1071 (0.025) | 25 of 35 | 0.030 of 472 / 0.022 of 599 |
| data/combo/oft/thr70/merged | gru_phys_ttp | 16 of 91 (10 to 23) | 41 / 34 | +3 (-5 to +12) | +96 (57) | 7 of 1071 (0.007) | 4 of 35 | 0.000 of 472 / 0.012 of 599 |
| data/combo/oft/thr70/merged | or_progress_ttp | 21 of 91 (14 to 29) | 53 / 17 | +8 (+3 to +14) | +128 (74) | 20 of 1071 (0.019) | 24 of 35 | 0.023 of 472 / 0.015 of 599 |
