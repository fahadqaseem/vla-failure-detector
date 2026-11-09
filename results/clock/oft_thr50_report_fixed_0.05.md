# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/oft_thr50 | progress | 0.048 | -140 (70) | 17 of 91 (10 to 25) | 0.025 | -200 (51) | 12 of 91 (6 to 19) |
| data/clock/oft_thr50 | gru_phys_ttp_s0 | 0.054 | -128 (48) | 10 of 91 (5 to 16) | 0.007 | -128 (44) | 9 of 91 (4 to 15) |
| data/clock/oft_thr50 | gru_phys_ttp_s1 | 0.030 | -100 (60) | 13 of 91 (7 to 20) | 0.011 | -112 (49) | 9 of 91 (4 to 15) |
| data/clock/oft_thr50 | gru_phys_ttp_s2 | 0.079 | -96 (55) | 12 of 91 (6 to 18) | 0.020 | -112 (45) | 8 of 91 (3 to 14) |
| data/clock/oft_thr50 | gru_phys_ttp_s3 | 0.069 | -104 (50) | 12 of 91 (6 to 19) | 0.046 | -112 (47) | 10 of 91 (5 to 16) |
| data/clock/oft_thr50 | gru_phys_ttp_s4 | 0.054 | -120 (49) | 9 of 91 (4 to 15) | 0.043 | -128 (45) | 7 of 91 (2 to 12) |
| data/clock/oft_thr50 | gru_phys_ttp_ens | 0.055 | -96 (55) | 12 of 91 (6 to 19) | 0.016 | -104 (51) | 11 of 91 (5 to 17) |
| data/clock/oft_thr50 | or_progress_ttp_s0 | 0.042 | -128 (72) | 17 of 91 (10 to 24) | 0.018 | -144 (70) | 14 of 91 (8 to 21) |
| data/clock/oft_thr50 | or_progress_ttp_s1 | 0.042 | -96 (79) | 19 of 91 (12 to 27) | 0.021 | -128 (70) | 16 of 91 (9 to 23) |
| data/clock/oft_thr50 | or_progress_ttp_s2 | 0.051 | -112 (74) | 17 of 91 (10 to 24) | 0.019 | -140 (68) | 12 of 91 (6 to 18) |
| data/clock/oft_thr50 | or_progress_ttp_s3 | 0.088 | -96 (74) | 21 of 91 (13 to 29) | 0.034 | -128 (71) | 16 of 91 (9 to 23) |
| data/clock/oft_thr50 | or_progress_ttp_s4 | 0.072 | -128 (73) | 16 of 91 (9 to 23) | 0.023 | -144 (70) | 12 of 91 (6 to 18) |
| data/clock/oft_thr50 | or_progress_ens | 0.044 | -104 (74) | 19 of 91 (12 to 27) | 0.018 | -128 (69) | 13 of 91 (7 to 20) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr50 | progress | 17 of 91 (10 to 24) | 53 / 21 |  | +140 (70) | 51 of 1071 (0.048) | 16 of 17 | 0.049 of 472 / 0.047 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s0 | 10 of 91 (5 to 16) | 38 / 43 | -7 (-15 to +1) | +128 (48) | 58 of 1071 (0.054) | 2 of 17 | 0.108 of 472 / 0.012 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s1 | 13 of 91 (7 to 20) | 47 / 31 | -4 (-13 to +5) | +100 (60) | 32 of 1071 (0.030) | 5 of 17 | 0.021 of 472 / 0.037 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s2 | 12 of 91 (6 to 18) | 43 / 36 | -5 (-13 to +2) | +96 (55) | 85 of 1071 (0.079) | 4 of 17 | 0.121 of 472 / 0.047 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s3 | 12 of 91 (6 to 18) | 38 / 41 | -5 (-14 to +4) | +104 (50) | 74 of 1071 (0.069) | 4 of 17 | 0.108 of 472 / 0.038 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s4 | 9 of 91 (4 to 15) | 40 / 42 | -8 (-17 to +0) | +120 (49) | 58 of 1071 (0.054) | 2 of 17 | 0.104 of 472 / 0.015 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_ens | 12 of 91 (6 to 19) | 43 / 36 | -5 (-13 to +3) | +96 (55) | 59 of 1071 (0.055) | 3 of 17 | 0.081 of 472 / 0.035 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s0 | 17 of 91 (10 to 24) | 55 / 19 | +0 (-6 to +6) | +128 (72) | 45 of 1071 (0.042) | 14 of 17 | 0.055 of 472 / 0.032 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s1 | 19 of 91 (12 to 27) | 60 / 12 | +2 (-4 to +8) | +96 (79) | 45 of 1071 (0.042) | 15 of 17 | 0.038 of 472 / 0.045 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s2 | 17 of 91 (10 to 24) | 57 / 17 | +0 (-6 to +6) | +112 (74) | 55 of 1071 (0.051) | 15 of 17 | 0.064 of 472 / 0.042 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s3 | 21 of 91 (13 to 29) | 53 / 17 | +4 (-3 to +11) | +96 (74) | 94 of 1071 (0.088) | 16 of 17 | 0.140 of 472 / 0.047 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s4 | 16 of 91 (9 to 23) | 57 / 18 | -1 (-7 to +5) | +128 (73) | 77 of 1071 (0.072) | 15 of 17 | 0.125 of 472 / 0.030 of 599 |
| data/clock/oft_thr50 | or_progress_ens | 19 of 91 (12 to 27) | 55 / 17 | +2 (-4 to +8) | +104 (74) | 47 of 1071 (0.044) | 15 of 17 | 0.047 of 472 / 0.042 of 599 |
