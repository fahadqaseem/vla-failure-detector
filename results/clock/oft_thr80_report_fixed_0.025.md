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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/oft_thr80 | progress | 16 of 120 (9 to 24) | 54 / 50 |  | +156 (70) | 27 of 1071 (0.025) | 15 of 19 | 0.030 of 472 / 0.022 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s0 | 18 of 120 (11 to 26) | 47 / 55 | +2 (-8 to +12) | +88 (65) | 13 of 1071 (0.012) | 3 of 19 | 0.002 of 472 / 0.020 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s1 | 24 of 120 (15 to 33) | 52 / 44 | +8 (-2 to +19) | +56 (76) | 15 of 1071 (0.014) | 4 of 19 | 0.002 of 472 / 0.023 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s2 | 23 of 120 (15 to 32) | 48 / 49 | +7 (-3 to +18) | +48 (71) | 15 of 1071 (0.014) | 3 of 19 | 0.002 of 472 / 0.023 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s3 | 20 of 120 (12 to 28) | 55 / 45 | +4 (-6 to +14) | +88 (75) | 33 of 1071 (0.031) | 4 of 19 | 0.008 of 472 / 0.048 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_s4 | 22 of 120 (14 to 31) | 47 / 51 | +6 (-4 to +16) | +72 (69) | 26 of 1071 (0.024) | 4 of 19 | 0.006 of 472 / 0.038 of 599 |
| data/clock/oft_thr80 | gru_phys_ttp_ens | 22 of 120 (14 to 31) | 51 / 47 | +6 (-4 to +16) | +64 (73) | 20 of 1071 (0.019) | 4 of 19 | 0.006 of 472 / 0.028 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s0 | 22 of 120 (14 to 30) | 72 / 26 | +6 (-1 to +13) | +120 (94) | 20 of 1071 (0.019) | 16 of 19 | 0.021 of 472 / 0.017 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s1 | 27 of 120 (18 to 36) | 75 / 18 | +11 (+3 to +19) | +88 (102) | 23 of 1071 (0.021) | 16 of 19 | 0.019 of 472 / 0.023 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s2 | 24 of 120 (15 to 33) | 74 / 22 | +8 (+1 to +15) | +96 (98) | 26 of 1071 (0.024) | 16 of 19 | 0.025 of 472 / 0.023 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s3 | 24 of 120 (16 to 33) | 77 / 19 | +8 (+1 to +15) | +104 (101) | 32 of 1071 (0.030) | 16 of 19 | 0.025 of 472 / 0.033 of 599 |
| data/clock/oft_thr80 | or_progress_ttp_s4 | 24 of 120 (16 to 33) | 76 / 20 | +8 (+1 to +15) | +104 (100) | 23 of 1071 (0.021) | 16 of 19 | 0.021 of 472 / 0.022 of 599 |
| data/clock/oft_thr80 | or_progress_ens | 24 of 120 (16 to 33) | 78 / 18 | +8 (+1 to +15) | +96 (102) | 24 of 1071 (0.022) | 16 of 19 | 0.023 of 472 / 0.022 of 599 |
