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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr70 | progress | 21 of 105 (13 to 29) | 58 / 26 |  | +112 (79) | 51 of 1071 (0.048) | 18 of 19 | 0.049 of 472 / 0.047 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s0 | 17 of 105 (10 to 25) | 46 / 42 | -4 (-13 to +5) | +88 (63) | 19 of 1071 (0.018) | 4 of 19 | 0.006 of 472 / 0.027 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s1 | 20 of 105 (13 to 28) | 53 / 32 | -1 (-11 to +9) | +80 (73) | 31 of 1071 (0.029) | 4 of 19 | 0.013 of 472 / 0.042 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s2 | 18 of 105 (11 to 26) | 49 / 38 | -3 (-13 to +7) | +80 (67) | 26 of 1071 (0.024) | 3 of 19 | 0.013 of 472 / 0.033 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s3 | 19 of 105 (12 to 27) | 51 / 35 | -2 (-13 to +9) | +80 (70) | 58 of 1071 (0.054) | 5 of 19 | 0.025 of 472 / 0.077 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_s4 | 18 of 105 (11 to 26) | 49 / 38 | -3 (-13 to +7) | +88 (67) | 26 of 1071 (0.024) | 4 of 19 | 0.004 of 472 / 0.040 of 599 |
| data/clock/oft_thr70 | gru_phys_ttp_ens | 19 of 105 (12 to 27) | 51 / 35 | -2 (-12 to +8) | +80 (70) | 26 of 1071 (0.024) | 4 of 19 | 0.008 of 472 / 0.037 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s0 | 22 of 105 (14 to 30) | 67 / 16 | +1 (-6 to +8) | +104 (89) | 36 of 1071 (0.034) | 17 of 19 | 0.034 of 472 / 0.033 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s1 | 25 of 105 (17 to 34) | 69 / 11 | +4 (-4 to +12) | +88 (94) | 45 of 1071 (0.042) | 18 of 19 | 0.038 of 472 / 0.045 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s2 | 23 of 105 (15 to 31) | 68 / 14 | +2 (-6 to +10) | +96 (91) | 43 of 1071 (0.040) | 17 of 19 | 0.036 of 472 / 0.043 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s3 | 28 of 105 (19 to 37) | 61 / 16 | +7 (-2 to +16) | +88 (89) | 67 of 1071 (0.063) | 18 of 19 | 0.047 of 472 / 0.075 of 599 |
| data/clock/oft_thr70 | or_progress_ttp_s4 | 25 of 105 (17 to 34) | 67 / 13 | +4 (-4 to +12) | +96 (92) | 43 of 1071 (0.040) | 17 of 19 | 0.032 of 472 / 0.047 of 599 |
| data/clock/oft_thr70 | or_progress_ens | 26 of 105 (18 to 35) | 67 / 12 | +5 (-3 to +13) | +88 (93) | 41 of 1071 (0.038) | 17 of 19 | 0.034 of 472 / 0.042 of 599 |
