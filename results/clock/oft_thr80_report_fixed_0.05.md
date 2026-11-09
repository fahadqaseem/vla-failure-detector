# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/oft_thr80 | progress | 0.048 | -104 (91) | 30 of 120 (21 to 40) | 0.025 | -156 (70) | 16 of 120 (9 to 24) |
| data/clock/oft_thr80 | gru_phys_ttp_s0 | 0.025 | -76 (78) | 22 of 120 (14 to 30) | 0.012 | -88 (65) | 18 of 120 (11 to 26) |
| data/clock/oft_thr80 | gru_phys_ttp_s1 | 0.021 | -48 (83) | 27 of 120 (18 to 36) | 0.014 | -56 (76) | 24 of 120 (16 to 33) |
| data/clock/oft_thr80 | gru_phys_ttp_s2 | 0.022 | -56 (80) | 25 of 120 (16 to 34) | 0.014 | -48 (71) | 23 of 120 (15 to 32) |
| data/clock/oft_thr80 | gru_phys_ttp_s3 | 0.060 | -64 (79) | 24 of 120 (15 to 33) | 0.031 | -88 (75) | 20 of 120 (12 to 28) |
| data/clock/oft_thr80 | gru_phys_ttp_s4 | 0.031 | -64 (78) | 26 of 120 (17 to 35) | 0.024 | -72 (69) | 22 of 120 (14 to 30) |
| data/clock/oft_thr80 | gru_phys_ttp_ens | 0.024 | -56 (83) | 25 of 120 (16 to 34) | 0.019 | -64 (73) | 22 of 120 (14 to 30) |
| data/clock/oft_thr80 | or_progress_ttp_s0 | 0.038 | -88 (105) | 30 of 120 (21 to 39) | 0.019 | -120 (94) | 22 of 120 (14 to 30) |
| data/clock/oft_thr80 | or_progress_ttp_s1 | 0.041 | -56 (107) | 36 of 120 (26 to 46) | 0.021 | -88 (102) | 27 of 120 (18 to 36) |
| data/clock/oft_thr80 | or_progress_ttp_s2 | 0.035 | -60 (106) | 35 of 120 (26 to 45) | 0.024 | -96 (98) | 24 of 120 (15 to 33) |
| data/clock/oft_thr80 | or_progress_ttp_s3 | 0.053 | -88 (106) | 33 of 120 (24 to 43) | 0.030 | -104 (101) | 24 of 120 (16 to 33) |
| data/clock/oft_thr80 | or_progress_ttp_s4 | 0.049 | -72 (105) | 34 of 120 (24 to 44) | 0.021 | -104 (100) | 24 of 120 (16 to 33) |
| data/clock/oft_thr80 | or_progress_ens | 0.045 | -60 (106) | 34 of 120 (24 to 44) | 0.022 | -96 (102) | 24 of 120 (16 to 33) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr80 | progress | 30 of 120 (21 to 40) | 61 / 29 |  | +104 (91) | 51 of 1071 (0.048) | 18 of 19 | 0.049 of 472 / 0.047 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s0 | 22 of 120 (14 to 31) | 56 / 42 | -8 (-19 to +3) | +76 (78) | 27 of 1071 (0.025) | 3 of 19 | 0.006 of 472 / 0.040 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s1 | 27 of 120 (18 to 36) | 56 / 37 | -3 (-14 to +8) | +48 (83) | 23 of 1071 (0.021) | 5 of 19 | 0.013 of 472 / 0.028 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s2 | 25 of 120 (16 to 34) | 55 / 40 | -5 (-16 to +6) | +56 (80) | 24 of 1071 (0.022) | 4 of 19 | 0.019 of 472 / 0.025 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s3 | 24 of 120 (16 to 33) | 55 / 41 | -6 (-17 to +5) | +64 (79) | 64 of 1071 (0.060) | 4 of 19 | 0.025 of 472 / 0.087 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s4 | 26 of 120 (17 to 35) | 52 / 42 | -4 (-15 to +6) | +64 (78) | 33 of 1071 (0.031) | 4 of 19 | 0.008 of 472 / 0.048 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_ens | 25 of 120 (16 to 34) | 58 / 37 | -5 (-16 to +6) | +56 (83) | 26 of 1071 (0.024) | 5 of 19 | 0.006 of 472 / 0.038 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s0 | 30 of 120 (21 to 39) | 75 / 15 | +0 (-9 to +8) | +88 (105) | 41 of 1071 (0.038) | 18 of 19 | 0.032 of 472 / 0.043 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s1 | 36 of 120 (26 to 46) | 71 / 13 | +6 (-3 to +15) | +56 (107) | 44 of 1071 (0.041) | 18 of 19 | 0.040 of 472 / 0.042 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s2 | 35 of 120 (25 to 45) | 71 / 14 | +5 (-4 to +14) | +60 (106) | 38 of 1071 (0.035) | 18 of 19 | 0.032 of 472 / 0.038 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s3 | 33 of 120 (24 to 43) | 73 / 14 | +3 (-6 to +12) | +88 (106) | 57 of 1071 (0.053) | 18 of 19 | 0.038 of 472 / 0.065 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s4 | 34 of 120 (24 to 44) | 71 / 15 | +4 (-5 to +13) | +72 (105) | 53 of 1071 (0.049) | 18 of 19 | 0.036 of 472 / 0.060 of 599 |
| data/clock/oft_thr80 | or_progress_ens | 34 of 120 (24 to 44) | 72 / 14 | +4 (-5 to +13) | +60 (106) | 48 of 1071 (0.045) | 18 of 19 | 0.038 of 472 / 0.050 of 599 |
