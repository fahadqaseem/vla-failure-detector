# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr80/merged | progress | 0.048 | -96 (74) | 29 of 102 (20 to 38) | 0.025 | -144 (57) | 17 of 102 (10 to 25) |
| data/combo/oft/thr80/merged | gru_phys_ttp | 0.025 | -48 (76) | 26 of 102 (18 to 35) | 0.012 | -80 (63) | 20 of 102 (12 to 28) |
| data/combo/oft/thr80/merged | or_progress_ttp | 0.038 | -72 (92) | 31 of 102 (22 to 40) | 0.019 | -96 (84) | 24 of 102 (16 to 33) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr80/merged | progress | 17 of 102 (10 to 24) | 40 / 45 |  | +144 (57) | 27 of 1071 (0.025) | 28 of 39 | 0.030 of 472 / 0.022 of 599 |
| data/combo/oft/thr80/merged | gru_phys_ttp | 20 of 102 (12 to 28) | 43 / 39 | +3 (-7 to +13) | +80 (63) | 13 of 1071 (0.012) | 7 of 39 | 0.002 of 472 / 0.020 of 599 |
| data/combo/oft/thr80/merged | or_progress_ttp | 24 of 102 (16 to 32) | 60 / 18 | +7 (+2 to +13) | +96 (84) | 20 of 1071 (0.019) | 28 of 39 | 0.021 of 472 / 0.017 of 599 |
