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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr50 | progress | 12 of 91 (6 to 18) | 39 / 40 |  | +200 (51) | 27 of 1071 (0.025) | 13 of 17 | 0.030 of 472 / 0.022 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s0 | 9 of 91 (4 to 15) | 35 / 47 | -3 (-10 to +4) | +128 (44) | 8 of 1071 (0.007) | 2 of 17 | 0.004 of 472 / 0.010 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s1 | 9 of 91 (4 to 15) | 40 / 42 | -3 (-10 to +5) | +112 (49) | 12 of 1071 (0.011) | 2 of 17 | 0.002 of 472 / 0.018 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s2 | 8 of 91 (3 to 14) | 37 / 46 | -4 (-11 to +3) | +112 (45) | 21 of 1071 (0.020) | 2 of 17 | 0.025 of 472 / 0.015 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s3 | 10 of 91 (5 to 16) | 37 / 44 | -2 (-10 to +6) | +112 (47) | 49 of 1071 (0.046) | 2 of 17 | 0.074 of 472 / 0.023 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_s4 | 7 of 91 (3 to 12) | 38 / 46 | -5 (-12 to +2) | +128 (45) | 46 of 1071 (0.043) | 1 of 17 | 0.085 of 472 / 0.010 of 599 |
| data/clock/oft_thr50 | gru_phys_ttp_ens | 11 of 91 (5 to 17) | 40 / 40 | -1 (-9 to +7) | +104 (51) | 17 of 1071 (0.016) | 3 of 17 | 0.011 of 472 / 0.020 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s0 | 14 of 91 (8 to 21) | 56 / 21 | +2 (-2 to +6) | +144 (70) | 19 of 1071 (0.018) | 13 of 17 | 0.019 of 472 / 0.017 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s1 | 16 of 91 (9 to 23) | 54 / 21 | +4 (-1 to +10) | +128 (70) | 23 of 1071 (0.021) | 13 of 17 | 0.017 of 472 / 0.025 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s2 | 12 of 91 (6 to 18) | 56 / 23 | +0 (-4 to +4) | +140 (68) | 20 of 1071 (0.019) | 13 of 17 | 0.019 of 472 / 0.018 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s3 | 16 of 91 (9 to 23) | 55 / 20 | +4 (-1 to +10) | +128 (71) | 36 of 1071 (0.034) | 13 of 17 | 0.047 of 472 / 0.023 of 599 |
| data/clock/oft_thr50 | or_progress_ttp_s4 | 12 of 91 (6 to 18) | 58 / 21 | +0 (-4 to +4) | +144 (70) | 25 of 1071 (0.023) | 13 of 17 | 0.032 of 472 / 0.017 of 599 |
| data/clock/oft_thr50 | or_progress_ens | 13 of 91 (7 to 20) | 56 / 22 | +1 (-3 to +5) | +128 (69) | 19 of 1071 (0.018) | 13 of 17 | 0.017 of 472 / 0.018 of 599 |
