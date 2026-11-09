# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/oft_thr70 | progress | 0.048 | -112 (79) | 21 of 105 (13 to 29) | 0.025 | -156 (58) | 12 of 105 (6 to 19) |
| data/clock/oft_thr70 | gru_phys_ttp_s0 | 0.018 | -88 (63) | 17 of 105 (10 to 25) | 0.007 | -96 (58) | 12 of 105 (6 to 19) |
| data/clock/oft_thr70 | gru_phys_ttp_s1 | 0.029 | -80 (73) | 20 of 105 (13 to 28) | 0.014 | -88 (66) | 15 of 105 (9 to 22) |
| data/clock/oft_thr70 | gru_phys_ttp_s2 | 0.024 | -80 (67) | 18 of 105 (11 to 26) | 0.015 | -96 (63) | 14 of 105 (8 to 21) |
| data/clock/oft_thr70 | gru_phys_ttp_s3 | 0.054 | -80 (70) | 19 of 105 (12 to 27) | 0.028 | -88 (65) | 17 of 105 (10 to 25) |
| data/clock/oft_thr70 | gru_phys_ttp_s4 | 0.024 | -88 (67) | 18 of 105 (11 to 26) | 0.015 | -96 (60) | 14 of 105 (8 to 21) |
| data/clock/oft_thr70 | gru_phys_ttp_ens | 0.024 | -80 (70) | 19 of 105 (12 to 27) | 0.014 | -88 (64) | 16 of 105 (9 to 24) |
| data/clock/oft_thr70 | or_progress_ttp_s0 | 0.034 | -104 (89) | 22 of 105 (14 to 30) | 0.019 | -136 (81) | 16 of 105 (9 to 24) |
| data/clock/oft_thr70 | or_progress_ttp_s1 | 0.042 | -88 (94) | 25 of 105 (17 to 34) | 0.025 | -120 (87) | 19 of 105 (12 to 27) |
| data/clock/oft_thr70 | or_progress_ttp_s2 | 0.040 | -96 (91) | 23 of 105 (15 to 32) | 0.025 | -120 (85) | 17 of 105 (10 to 25) |
| data/clock/oft_thr70 | or_progress_ttp_s3 | 0.063 | -88 (89) | 28 of 105 (19 to 37) | 0.033 | -104 (86) | 22 of 105 (14 to 30) |
| data/clock/oft_thr70 | or_progress_ttp_s4 | 0.040 | -96 (92) | 25 of 105 (17 to 34) | 0.021 | -120 (85) | 17 of 105 (10 to 25) |
| data/clock/oft_thr70 | or_progress_ens | 0.038 | -88 (93) | 26 of 105 (18 to 35) | 0.023 | -120 (85) | 19 of 105 (12 to 27) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr70 | progress | 12 of 105 (6 to 19) | 46 / 47 |  | +156 (58) | 27 of 1071 (0.025) | 15 of 19 | 0.030 of 472 / 0.022 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s0 | 12 of 105 (6 to 18) | 46 / 47 | +0 (-8 to +8) | +96 (58) | 8 of 1071 (0.007) | 1 of 19 | 0.000 of 472 / 0.013 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s1 | 15 of 105 (8 to 22) | 51 / 39 | +3 (-5 to +11) | +88 (66) | 15 of 1071 (0.014) | 2 of 19 | 0.002 of 472 / 0.023 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s2 | 14 of 105 (8 to 21) | 49 / 42 | +2 (-6 to +10) | +96 (63) | 16 of 1071 (0.015) | 2 of 19 | 0.002 of 472 / 0.025 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s3 | 17 of 105 (10 to 25) | 48 / 40 | +5 (-4 to +14) | +88 (65) | 30 of 1071 (0.028) | 5 of 19 | 0.006 of 472 / 0.045 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s4 | 14 of 105 (8 to 21) | 46 / 45 | +2 (-7 to +11) | +96 (60) | 16 of 1071 (0.015) | 1 of 19 | 0.002 of 472 / 0.025 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_ens | 16 of 105 (9 to 23) | 48 / 41 | +4 (-4 to +13) | +88 (64) | 15 of 1071 (0.014) | 2 of 19 | 0.002 of 472 / 0.023 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s0 | 16 of 105 (9 to 23) | 65 / 24 | +4 (+0 to +9) | +136 (81) | 20 of 1071 (0.019) | 15 of 19 | 0.023 of 472 / 0.015 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s1 | 19 of 105 (12 to 27) | 68 / 18 | +7 (+2 to +13) | +120 (87) | 27 of 1071 (0.025) | 15 of 19 | 0.023 of 472 / 0.027 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s2 | 17 of 105 (10 to 25) | 68 / 20 | +5 (+0 to +10) | +120 (85) | 27 of 1071 (0.025) | 15 of 19 | 0.023 of 472 / 0.027 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s3 | 22 of 105 (14 to 30) | 64 / 19 | +10 (+4 to +17) | +104 (86) | 35 of 1071 (0.033) | 15 of 19 | 0.021 of 472 / 0.042 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s4 | 17 of 105 (10 to 24) | 68 / 20 | +5 (+0 to +10) | +120 (85) | 23 of 1071 (0.021) | 15 of 19 | 0.021 of 472 / 0.022 of 599 |
| data/clock/oft_thr70 | or_progress_ens | 19 of 105 (12 to 27) | 66 / 20 | +7 (+2 to +13) | +120 (85) | 25 of 1071 (0.023) | 15 of 19 | 0.023 of 472 / 0.023 of 599 |
