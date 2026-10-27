# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/seen_surprise | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_surprise | mlp_phys | 0.046 | -72 (72) | 15 of 81 (8 to 22) | 0.027 | -120 (55) | 7 of 81 (3 to 12) |
| pnr_probe/results/seen_surprise | mlp_phys_cusum | 0.047 | -72 (73) | 15 of 81 (8 to 22) | 0.023 | -128 (51) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_surprise | gru_phys | 0.052 | -76 (80) | 18 of 81 (11 to 26) | 0.026 | -96 (75) | 15 of 81 (9 to 22) |
| pnr_probe/results/seen_surprise | gru_phys_cusum | 0.035 | -80 (65) | 14 of 81 (8 to 21) | 0.011 | -96 (37) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_csd | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_csd | mlp_phys | 0.049 | -48 (77) | 25 of 81 (17 to 33) | 0.021 | -80 (65) | 14 of 81 (8 to 21) |
| pnr_probe/results/seen_csd | mlp_phys_cusum | 0.046 | -56 (63) | 16 of 81 (9 to 23) | 0.019 | -80 (47) | 8 of 81 (3 to 14) |
| pnr_probe/results/seen_csd | gru_phys | 0.038 | -104 (73) | 12 of 81 (6 to 19) | 0.023 | -140 (64) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_csd | gru_phys_cusum | 0.049 | -104 (72) | 15 of 81 (8 to 22) | 0.023 | -120 (65) | 9 of 81 (4 to 15) |
| pnr_probe/results/seen_ttc | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_ttc | mlp_phys | 0.011 | -144 (5) | 2 of 81 (0 to 5) | 0.000 | none | 0 of 81 (0 to 0) |
| pnr_probe/results/seen_ttc | mlp_phys_cusum | 0.038 | -96 (24) | 5 of 81 (1 to 10) | 0.022 | -104 (19) | 3 of 81 (0 to 7) |
| pnr_probe/results/seen_ttc | gru_phys | 0.050 | -96 (70) | 18 of 81 (11 to 26) | 0.025 | -96 (61) | 12 of 81 (6 to 19) |
| pnr_probe/results/seen_ttc | gru_phys_cusum | 0.045 | -80 (41) | 10 of 81 (5 to 16) | 0.019 | -88 (27) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_micro | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_micro | mlp_phys | 0.054 | -120 (57) | 15 of 81 (8 to 22) | 0.023 | -184 (35) | 7 of 81 (3 to 12) |
| pnr_probe/results/seen_micro | mlp_phys_cusum | 0.042 | -184 (45) | 10 of 81 (5 to 16) | 0.015 | -216 (25) | 4 of 81 (1 to 8) |
| pnr_probe/results/seen_micro | gru_phys | 0.051 | -132 (68) | 18 of 81 (11 to 26) | 0.024 | -168 (49) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_micro | gru_phys_cusum | 0.051 | -152 (54) | 13 of 81 (7 to 20) | 0.021 | -184 (27) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_bio | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_bio | mlp_phys | 0.045 | -56 (76) | 21 of 81 (13 to 29) | 0.022 | -80 (66) | 14 of 81 (8 to 21) |
| pnr_probe/results/seen_bio | mlp_phys_cusum | 0.043 | -56 (63) | 18 of 81 (11 to 26) | 0.019 | -76 (42) | 8 of 81 (3 to 14) |
| pnr_probe/results/seen_bio | gru_phys | 0.053 | -96 (73) | 15 of 81 (9 to 22) | 0.022 | -132 (60) | 6 of 81 (2 to 11) |
| pnr_probe/results/seen_bio | gru_phys_cusum | 0.049 | -96 (68) | 11 of 81 (5 to 17) | 0.021 | -136 (58) | 8 of 81 (3 to 14) |
| pnr_probe/results/seen_bioplus | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_bioplus | mlp_phys | 0.049 | -52 (74) | 21 of 81 (13 to 29) | 0.020 | -80 (62) | 13 of 81 (7 to 20) |
| pnr_probe/results/seen_bioplus | mlp_phys_cusum | 0.045 | -64 (68) | 17 of 81 (10 to 24) | 0.019 | -80 (52) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_bioplus | gru_phys | 0.041 | -80 (75) | 17 of 81 (10 to 24) | 0.020 | -104 (70) | 10 of 81 (5 to 16) |
| pnr_probe/results/seen_bioplus | gru_phys_cusum | 0.037 | -84 (74) | 16 of 81 (9 to 23) | 0.016 | -96 (63) | 9 of 81 (4 to 15) |
| pnr_probe/results/seen_t1 | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_t1 | mlp_phys | 0.057 | -40 (69) | 20 of 81 (13 to 28) | 0.025 | -60 (58) | 16 of 81 (9 to 23) |
| pnr_probe/results/seen_t1 | mlp_phys_cusum | 0.051 | -40 (51) | 15 of 81 (8 to 22) | 0.026 | -48 (38) | 11 of 81 (5 to 17) |
| pnr_probe/results/seen_t1 | gru_phys | 0.053 | -48 (75) | 23 of 81 (15 to 31) | 0.023 | -64 (73) | 19 of 81 (12 to 27) |
| pnr_probe/results/seen_t1 | gru_phys_cusum | 0.049 | -56 (61) | 17 of 81 (10 to 25) | 0.021 | -72 (48) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/seen_surprise | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_surprise | mlp_phys | 15 of 81 (8 to 22) | 57 / 9 | -1 (-10 to +7) | +72 (72) | 49 of 1071 (0.046) | 21 of 31 | 0.030 of 472 / 0.058 of 599 |
| pnr_probe/results/seen_surprise | mlp_phys_cusum | 15 of 81 (8 to 22) | 58 / 8 | -1 (-10 to +7) | +72 (73) | 50 of 1071 (0.047) | 19 of 31 | 0.042 of 472 / 0.050 of 599 |
| pnr_probe/results/seen_surprise | gru_phys | 18 of 81 (11 to 25) | 62 / 1 | +2 (-6 to +10) | +76 (80) | 56 of 1071 (0.052) | 25 of 31 | 0.059 of 472 / 0.047 of 599 |
| pnr_probe/results/seen_surprise | gru_phys_cusum | 14 of 81 (8 to 21) | 51 / 16 | -2 (-9 to +5) | +80 (65) | 37 of 1071 (0.035) | 24 of 31 | 0.040 of 472 / 0.030 of 599 |
| pnr_probe/results/seen_csd | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_csd | mlp_phys | 25 of 81 (17 to 33) | 52 / 4 | +9 (+2 to +16) | +48 (77) | 52 of 1071 (0.049) | 27 of 31 | 0.032 of 472 / 0.062 of 599 |
| pnr_probe/results/seen_csd | mlp_phys_cusum | 16 of 81 (9 to 23) | 47 / 18 | +0 (-6 to +6) | +56 (63) | 49 of 1071 (0.046) | 28 of 31 | 0.042 of 472 / 0.048 of 599 |
| pnr_probe/results/seen_csd | gru_phys | 12 of 81 (6 to 19) | 61 / 8 | -4 (-11 to +3) | +104 (73) | 41 of 1071 (0.038) | 18 of 31 | 0.019 of 472 / 0.053 of 599 |
| pnr_probe/results/seen_csd | gru_phys_cusum | 15 of 81 (8 to 22) | 57 / 9 | -1 (-8 to +6) | +104 (72) | 52 of 1071 (0.049) | 20 of 31 | 0.032 of 472 / 0.062 of 599 |
| pnr_probe/results/seen_ttc | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_ttc | mlp_phys | 2 of 81 (0 to 5) | 3 / 76 | -14 (-22 to -6) | +144 (5) | 12 of 1071 (0.011) | 0 of 31 | 0.011 of 472 / 0.012 of 599 |
| pnr_probe/results/seen_ttc | mlp_phys_cusum | 5 of 81 (1 to 9) | 19 / 57 | -11 (-20 to -3) | +96 (24) | 41 of 1071 (0.038) | 9 of 31 | 0.036 of 472 / 0.040 of 599 |
| pnr_probe/results/seen_ttc | gru_phys | 18 of 81 (11 to 25) | 52 / 11 | +2 (-5 to +9) | +96 (70) | 54 of 1071 (0.050) | 15 of 31 | 0.044 of 472 / 0.055 of 599 |
| pnr_probe/results/seen_ttc | gru_phys_cusum | 10 of 81 (5 to 16) | 31 / 40 | -6 (-13 to +0) | +80 (41) | 48 of 1071 (0.045) | 17 of 31 | 0.049 of 472 / 0.042 of 599 |
| pnr_probe/results/seen_micro | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_micro | mlp_phys | 15 of 81 (8 to 22) | 42 / 24 | -1 (-8 to +6) | +120 (57) | 58 of 1071 (0.054) | 18 of 31 | 0.068 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_micro | mlp_phys_cusum | 10 of 81 (5 to 16) | 35 / 36 | -6 (-14 to +1) | +184 (45) | 45 of 1071 (0.042) | 16 of 31 | 0.049 of 472 / 0.037 of 599 |
| pnr_probe/results/seen_micro | gru_phys | 18 of 81 (11 to 26) | 50 / 13 | +2 (-5 to +9) | +132 (68) | 55 of 1071 (0.051) | 24 of 31 | 0.049 of 472 / 0.053 of 599 |
| pnr_probe/results/seen_micro | gru_phys_cusum | 13 of 81 (7 to 20) | 41 / 27 | -3 (-9 to +3) | +152 (54) | 55 of 1071 (0.051) | 24 of 31 | 0.049 of 472 / 0.053 of 599 |
| pnr_probe/results/seen_bio | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_bio | mlp_phys | 21 of 81 (14 to 29) | 55 / 5 | +5 (-3 to +13) | +56 (76) | 48 of 1071 (0.045) | 18 of 31 | 0.025 of 472 / 0.060 of 599 |
| pnr_probe/results/seen_bio | mlp_phys_cusum | 18 of 81 (11 to 25) | 45 / 18 | +2 (-5 to +9) | +56 (63) | 46 of 1071 (0.043) | 23 of 31 | 0.030 of 472 / 0.053 of 599 |
| pnr_probe/results/seen_bio | gru_phys | 15 of 81 (9 to 22) | 58 / 8 | -1 (-9 to +7) | +96 (73) | 57 of 1071 (0.053) | 15 of 31 | 0.028 of 472 / 0.073 of 599 |
| pnr_probe/results/seen_bio | gru_phys_cusum | 11 of 81 (5 to 17) | 57 / 13 | -5 (-13 to +2) | +96 (68) | 53 of 1071 (0.049) | 17 of 31 | 0.028 of 472 / 0.067 of 599 |
| pnr_probe/results/seen_bioplus | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_bioplus | mlp_phys | 21 of 81 (14 to 29) | 53 / 7 | +5 (-3 to +13) | +52 (74) | 53 of 1071 (0.049) | 14 of 31 | 0.025 of 472 / 0.068 of 599 |
| pnr_probe/results/seen_bioplus | mlp_phys_cusum | 17 of 81 (10 to 24) | 51 / 13 | +1 (-8 to +9) | +64 (68) | 48 of 1071 (0.045) | 18 of 31 | 0.034 of 472 / 0.053 of 599 |
| pnr_probe/results/seen_bioplus | gru_phys | 17 of 81 (10 to 24) | 58 / 6 | +1 (-8 to +9) | +80 (75) | 44 of 1071 (0.041) | 15 of 31 | 0.021 of 472 / 0.057 of 599 |
| pnr_probe/results/seen_bioplus | gru_phys_cusum | 16 of 81 (9 to 23) | 58 / 7 | +0 (-8 to +8) | +84 (74) | 40 of 1071 (0.037) | 16 of 31 | 0.019 of 472 / 0.052 of 599 |
| pnr_probe/results/seen_t1 | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| pnr_probe/results/seen_t1 | mlp_phys | 20 of 81 (13 to 28) | 49 / 12 | +4 (-5 to +13) | +40 (69) | 61 of 1071 (0.057) | 11 of 31 | 0.040 of 472 / 0.070 of 599 |
| pnr_probe/results/seen_t1 | mlp_phys_cusum | 15 of 81 (8 to 22) | 36 / 30 | -1 (-10 to +8) | +40 (51) | 55 of 1071 (0.051) | 12 of 31 | 0.038 of 472 / 0.062 of 599 |
| pnr_probe/results/seen_t1 | gru_phys | 23 of 81 (15 to 31) | 52 / 6 | +7 (-2 to +16) | +48 (75) | 57 of 1071 (0.053) | 14 of 31 | 0.032 of 472 / 0.070 of 599 |
| pnr_probe/results/seen_t1 | gru_phys_cusum | 17 of 81 (10 to 24) | 44 / 20 | +1 (-7 to +9) | +56 (61) | 53 of 1071 (0.049) | 17 of 31 | 0.038 of 472 / 0.058 of 599 |
