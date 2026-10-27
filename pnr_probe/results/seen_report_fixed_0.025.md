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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/seen_surprise | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_surprise | mlp_phys | 7 of 81 (3 to 12) | 48 / 26 | -4 (-12 to +4) | +120 (55) | 29 of 1071 (0.027) | 11 of 31 | 0.019 of 472 / 0.033 of 599 |
| pnr_probe/results/seen_surprise | mlp_phys_cusum | 6 of 81 (2 to 11) | 45 / 30 | -5 (-13 to +3) | +128 (51) | 25 of 1071 (0.023) | 7 of 31 | 0.025 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_surprise | gru_phys | 15 of 81 (9 to 22) | 60 / 6 | +4 (-3 to +11) | +96 (75) | 28 of 1071 (0.026) | 24 of 31 | 0.025 of 472 / 0.027 of 599 |
| pnr_probe/results/seen_surprise | gru_phys_cusum | 6 of 81 (2 to 11) | 31 / 44 | -5 (-11 to +1) | +96 (37) | 12 of 1071 (0.011) | 11 of 31 | 0.015 of 472 / 0.008 of 599 |
| pnr_probe/results/seen_csd | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_csd | mlp_phys | 14 of 81 (8 to 21) | 51 / 16 | +3 (-5 to +11) | +80 (65) | 23 of 1071 (0.021) | 11 of 31 | 0.013 of 472 / 0.028 of 599 |
| pnr_probe/results/seen_csd | mlp_phys_cusum | 8 of 81 (3 to 14) | 39 / 34 | -3 (-10 to +4) | +80 (47) | 20 of 1071 (0.019) | 18 of 31 | 0.017 of 472 / 0.020 of 599 |
| pnr_probe/results/seen_csd | gru_phys | 6 of 81 (2 to 11) | 58 / 17 | -5 (-10 to +0) | +140 (64) | 25 of 1071 (0.023) | 9 of 31 | 0.011 of 472 / 0.033 of 599 |
| pnr_probe/results/seen_csd | gru_phys_cusum | 9 of 81 (4 to 15) | 56 / 16 | -2 (-8 to +3) | +120 (65) | 25 of 1071 (0.023) | 12 of 31 | 0.015 of 472 / 0.030 of 599 |
| pnr_probe/results/seen_ttc | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_ttc | mlp_phys | 0 of 81 (0 to 0) | 0 / 81 | -11 (-17 to -5) | none | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| pnr_probe/results/seen_ttc | mlp_phys_cusum | 3 of 81 (0 to 7) | 16 / 62 | -8 (-15 to -1) | +104 (19) | 24 of 1071 (0.022) | 7 of 31 | 0.021 of 472 / 0.023 of 599 |
| pnr_probe/results/seen_ttc | gru_phys | 12 of 81 (6 to 18) | 49 / 20 | +1 (-7 to +8) | +96 (61) | 27 of 1071 (0.025) | 13 of 31 | 0.021 of 472 / 0.028 of 599 |
| pnr_probe/results/seen_ttc | gru_phys_cusum | 6 of 81 (2 to 11) | 21 / 54 | -5 (-13 to +3) | +88 (27) | 20 of 1071 (0.019) | 14 of 31 | 0.013 of 472 / 0.023 of 599 |
| pnr_probe/results/seen_micro | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_micro | mlp_phys | 7 of 81 (2 to 12) | 28 / 46 | -4 (-12 to +4) | +184 (35) | 25 of 1071 (0.023) | 4 of 31 | 0.021 of 472 / 0.025 of 599 |
| pnr_probe/results/seen_micro | mlp_phys_cusum | 4 of 81 (1 to 8) | 21 / 56 | -7 (-15 to +0) | +216 (25) | 16 of 1071 (0.015) | 8 of 31 | 0.008 of 472 / 0.020 of 599 |
| pnr_probe/results/seen_micro | gru_phys | 11 of 81 (5 to 17) | 38 / 32 | +0 (-9 to +9) | +168 (49) | 26 of 1071 (0.024) | 14 of 31 | 0.021 of 472 / 0.027 of 599 |
| pnr_probe/results/seen_micro | gru_phys_cusum | 6 of 81 (2 to 11) | 21 / 54 | -5 (-12 to +1) | +184 (27) | 23 of 1071 (0.021) | 17 of 31 | 0.021 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_bio | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_bio | mlp_phys | 14 of 81 (8 to 21) | 52 / 15 | +3 (-6 to +12) | +80 (66) | 24 of 1071 (0.022) | 10 of 31 | 0.013 of 472 / 0.030 of 599 |
| pnr_probe/results/seen_bio | mlp_phys_cusum | 8 of 81 (3 to 14) | 34 / 39 | -3 (-10 to +4) | +76 (42) | 20 of 1071 (0.019) | 13 of 31 | 0.017 of 472 / 0.020 of 599 |
| pnr_probe/results/seen_bio | gru_phys | 6 of 81 (2 to 11) | 54 / 21 | -5 (-12 to +1) | +132 (60) | 24 of 1071 (0.022) | 10 of 31 | 0.013 of 472 / 0.030 of 599 |
| pnr_probe/results/seen_bio | gru_phys_cusum | 8 of 81 (3 to 14) | 50 / 23 | -3 (-10 to +4) | +136 (58) | 23 of 1071 (0.021) | 9 of 31 | 0.015 of 472 / 0.027 of 599 |
| pnr_probe/results/seen_bioplus | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_bioplus | mlp_phys | 13 of 81 (7 to 20) | 49 / 19 | +2 (-6 to +10) | +80 (62) | 21 of 1071 (0.020) | 6 of 31 | 0.008 of 472 / 0.028 of 599 |
| pnr_probe/results/seen_bioplus | mlp_phys_cusum | 11 of 81 (5 to 17) | 41 / 29 | +0 (-8 to +8) | +80 (52) | 20 of 1071 (0.019) | 11 of 31 | 0.017 of 472 / 0.020 of 599 |
| pnr_probe/results/seen_bioplus | gru_phys | 10 of 81 (5 to 16) | 60 / 11 | -1 (-8 to +5) | +104 (70) | 21 of 1071 (0.020) | 10 of 31 | 0.011 of 472 / 0.027 of 599 |
| pnr_probe/results/seen_bioplus | gru_phys_cusum | 9 of 81 (4 to 15) | 54 / 18 | -2 (-9 to +5) | +96 (63) | 17 of 1071 (0.016) | 10 of 31 | 0.011 of 472 / 0.020 of 599 |
| pnr_probe/results/seen_t1 | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/seen_t1 | mlp_phys | 16 of 81 (9 to 23) | 42 / 23 | +5 (-3 to +13) | +60 (58) | 27 of 1071 (0.025) | 7 of 31 | 0.011 of 472 / 0.037 of 599 |
| pnr_probe/results/seen_t1 | mlp_phys_cusum | 11 of 81 (5 to 17) | 27 / 43 | +0 (-9 to +8) | +48 (38) | 28 of 1071 (0.026) | 8 of 31 | 0.017 of 472 / 0.033 of 599 |
| pnr_probe/results/seen_t1 | gru_phys | 19 of 81 (12 to 27) | 54 / 8 | +8 (-1 to +16) | +64 (73) | 25 of 1071 (0.023) | 10 of 31 | 0.013 of 472 / 0.032 of 599 |
| pnr_probe/results/seen_t1 | gru_phys_cusum | 10 of 81 (5 to 16) | 38 / 33 | -1 (-9 to +7) | +72 (48) | 23 of 1071 (0.021) | 12 of 31 | 0.019 of 472 / 0.023 of 599 |
