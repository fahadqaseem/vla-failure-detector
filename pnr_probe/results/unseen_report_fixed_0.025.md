# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/unseen_surprise | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_surprise | mlp_phys | 0.134 | -144 (35) | 3 of 81 (0 to 7) | 0.017 | -112 (25) | 2 of 81 (0 to 5) |
| pnr_probe/results/unseen_surprise | mlp_phys_cusum | 0.016 | -100 (2) | 1 of 81 (0 to 3) | 0.007 | -176 (2) | 0 of 81 (0 to 0) |
| pnr_probe/results/unseen_surprise | gru_phys | 0.042 | -128 (51) | 7 of 81 (3 to 12) | 0.029 | -116 (26) | 2 of 81 (0 to 5) |
| pnr_probe/results/unseen_surprise | gru_phys_cusum | 0.044 | -128 (5) | 2 of 81 (0 to 5) | 0.042 | -44 (4) | 2 of 81 (0 to 5) |
| pnr_probe/results/unseen_csd | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_csd | mlp_phys | 0.097 | -104 (59) | 10 of 81 (5 to 16) | 0.048 | -136 (42) | 8 of 81 (3 to 14) |
| pnr_probe/results/unseen_csd | mlp_phys_cusum | 0.043 | -88 (29) | 8 of 81 (3 to 14) | 0.017 | -120 (23) | 5 of 81 (1 to 10) |
| pnr_probe/results/unseen_csd | gru_phys | 0.032 | -120 (59) | 9 of 81 (4 to 15) | 0.016 | -128 (57) | 8 of 81 (3 to 14) |
| pnr_probe/results/unseen_csd | gru_phys_cusum | 0.026 | -112 (55) | 8 of 81 (3 to 14) | 0.014 | -128 (49) | 6 of 81 (2 to 11) |
| pnr_probe/results/unseen_ttc | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_ttc | mlp_phys | 0.072 | +32 (14) | 10 of 81 (5 to 16) | 0.000 | none | 0 of 81 (0 to 0) |
| pnr_probe/results/unseen_ttc | mlp_phys_cusum | 0.047 | -76 (28) | 5 of 81 (1 to 10) | 0.023 | -104 (18) | 2 of 81 (0 to 5) |
| pnr_probe/results/unseen_ttc | gru_phys | 0.073 | -156 (40) | 9 of 81 (4 to 15) | 0.056 | -60 (22) | 6 of 81 (2 to 11) |
| pnr_probe/results/unseen_ttc | gru_phys_cusum | 0.050 | -84 (44) | 13 of 81 (7 to 20) | 0.026 | -88 (38) | 10 of 81 (4 to 16) |
| pnr_probe/results/unseen_micro | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_micro | mlp_phys | 0.055 | -160 (59) | 13 of 81 (7 to 20) | 0.028 | -204 (34) | 9 of 81 (4 to 15) |
| pnr_probe/results/unseen_micro | mlp_phys_cusum | 0.058 | -116 (50) | 11 of 81 (5 to 17) | 0.032 | -196 (34) | 6 of 81 (2 to 11) |
| pnr_probe/results/unseen_micro | gru_phys | 0.047 | -112 (56) | 14 of 81 (8 to 21) | 0.024 | -164 (38) | 13 of 81 (7 to 20) |
| pnr_probe/results/unseen_micro | gru_phys_cusum | 0.049 | -156 (36) | 10 of 81 (5 to 16) | 0.034 | -128 (23) | 8 of 81 (3 to 14) |
| pnr_probe/results/unseen_bio | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_bio | mlp_phys | 0.021 | -80 (24) | 6 of 81 (2 to 11) | 0.015 | -88 (17) | 4 of 81 (1 to 8) |
| pnr_probe/results/unseen_bio | mlp_phys_cusum | 0.023 | -136 (22) | 4 of 81 (1 to 8) | 0.005 | -128 (5) | 1 of 81 (0 to 3) |
| pnr_probe/results/unseen_bio | gru_phys | 0.140 | -148 (44) | 4 of 81 (1 to 8) | 0.098 | -144 (38) | 2 of 81 (0 to 5) |
| pnr_probe/results/unseen_bio | gru_phys_cusum | 0.158 | -96 (42) | 6 of 81 (2 to 11) | 0.129 | -144 (38) | 4 of 81 (1 to 8) |
| pnr_probe/results/unseen_bioplus | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_bioplus | mlp_phys | 0.029 | -88 (49) | 8 of 81 (3 to 14) | 0.012 | -136 (42) | 4 of 81 (1 to 8) |
| pnr_probe/results/unseen_bioplus | mlp_phys_cusum | 0.012 | -104 (19) | 6 of 81 (2 to 11) | 0.003 | -112 (17) | 4 of 81 (1 to 8) |
| pnr_probe/results/unseen_bioplus | gru_phys | 0.070 | -112 (59) | 16 of 81 (9 to 23) | 0.022 | -152 (53) | 12 of 81 (6 to 19) |
| pnr_probe/results/unseen_bioplus | gru_phys_cusum | 0.139 | -128 (41) | 5 of 81 (1 to 10) | 0.110 | -144 (37) | 5 of 81 (1 to 10) |
| pnr_probe/results/unseen_t1 | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| pnr_probe/results/unseen_t1 | mlp_phys | 0.060 | -136 (48) | 6 of 81 (2 to 11) | 0.057 | -124 (40) | 4 of 81 (1 to 8) |
| pnr_probe/results/unseen_t1 | mlp_phys_cusum | 0.051 | -108 (16) | 1 of 81 (0 to 3) | 0.019 | -104 (9) | 1 of 81 (0 to 3) |
| pnr_probe/results/unseen_t1 | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.013 | -136 (43) | 10 of 81 (5 to 16) |
| pnr_probe/results/unseen_t1 | gru_phys_cusum | 0.118 | -128 (28) | 4 of 81 (1 to 8) | 0.044 | -136 (24) | 3 of 81 (0 to 7) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/unseen_surprise | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_surprise | mlp_phys | 2 of 81 (0 to 5) | 23 / 56 | -9 (-15 to -3) | +112 (25) | 18 of 1071 (0.017) | 9 of 31 | 0.006 of 472 / 0.025 of 599 |
| pnr_probe/results/unseen_surprise | mlp_phys_cusum | 0 of 81 (0 to 0) | 2 / 79 | -11 (-17 to -5) | +176 (2) | 8 of 1071 (0.007) | 0 of 31 | 0.017 of 472 / 0.000 of 599 |
| pnr_probe/results/unseen_surprise | gru_phys | 2 of 81 (0 to 5) | 24 / 55 | -9 (-16 to -2) | +116 (26) | 31 of 1071 (0.029) | 5 of 31 | 0.011 of 472 / 0.043 of 599 |
| pnr_probe/results/unseen_surprise | gru_phys_cusum | 2 of 81 (0 to 5) | 2 / 77 | -9 (-15 to -3) | +44 (4) | 45 of 1071 (0.042) | 2 of 31 | 0.095 of 472 / 0.000 of 599 |
| pnr_probe/results/unseen_csd | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_csd | mlp_phys | 8 of 81 (3 to 14) | 34 / 39 | -3 (-10 to +4) | +136 (42) | 51 of 1071 (0.048) | 7 of 31 | 0.025 of 472 / 0.065 of 599 |
| pnr_probe/results/unseen_csd | mlp_phys_cusum | 5 of 81 (1 to 10) | 18 / 58 | -6 (-13 to +1) | +120 (23) | 18 of 1071 (0.017) | 6 of 31 | 0.015 of 472 / 0.018 of 599 |
| pnr_probe/results/unseen_csd | gru_phys | 8 of 81 (3 to 14) | 49 / 24 | -3 (-9 to +3) | +128 (57) | 17 of 1071 (0.016) | 10 of 31 | 0.006 of 472 / 0.023 of 599 |
| pnr_probe/results/unseen_csd | gru_phys_cusum | 6 of 81 (2 to 11) | 43 / 32 | -5 (-11 to +1) | +128 (49) | 15 of 1071 (0.014) | 9 of 31 | 0.004 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_ttc | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_ttc | mlp_phys | 0 of 81 (0 to 0) | 0 / 81 | -11 (-17 to -5) | none | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| pnr_probe/results/unseen_ttc | mlp_phys_cusum | 2 of 81 (0 to 5) | 16 / 63 | -9 (-16 to -2) | +104 (18) | 25 of 1071 (0.023) | 10 of 31 | 0.019 of 472 / 0.027 of 599 |
| pnr_probe/results/unseen_ttc | gru_phys | 6 of 81 (2 to 11) | 16 / 59 | -5 (-12 to +2) | +60 (22) | 60 of 1071 (0.056) | 18 of 31 | 0.064 of 472 / 0.050 of 599 |
| pnr_probe/results/unseen_ttc | gru_phys_cusum | 10 of 81 (5 to 16) | 28 / 43 | -1 (-7 to +5) | +88 (38) | 28 of 1071 (0.026) | 19 of 31 | 0.021 of 472 / 0.030 of 599 |
| pnr_probe/results/unseen_micro | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_micro | mlp_phys | 9 of 81 (4 to 15) | 25 / 47 | -2 (-10 to +6) | +204 (34) | 30 of 1071 (0.028) | 5 of 31 | 0.030 of 472 / 0.027 of 599 |
| pnr_probe/results/unseen_micro | mlp_phys_cusum | 6 of 81 (2 to 11) | 28 / 47 | -5 (-12 to +2) | +196 (34) | 34 of 1071 (0.032) | 13 of 31 | 0.042 of 472 / 0.023 of 599 |
| pnr_probe/results/unseen_micro | gru_phys | 13 of 81 (7 to 20) | 25 / 43 | +2 (-6 to +10) | +164 (38) | 26 of 1071 (0.024) | 12 of 31 | 0.015 of 472 / 0.032 of 599 |
| pnr_probe/results/unseen_micro | gru_phys_cusum | 8 of 81 (3 to 14) | 15 / 58 | -3 (-10 to +4) | +128 (23) | 36 of 1071 (0.034) | 17 of 31 | 0.032 of 472 / 0.035 of 599 |
| pnr_probe/results/unseen_bio | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_bio | mlp_phys | 4 of 81 (1 to 8) | 13 / 64 | -7 (-14 to +0) | +88 (17) | 16 of 1071 (0.015) | 1 of 31 | 0.006 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_bio | mlp_phys_cusum | 1 of 81 (0 to 3) | 4 / 76 | -10 (-17 to -4) | +128 (5) | 5 of 1071 (0.005) | 2 of 31 | 0.002 of 472 / 0.007 of 599 |
| pnr_probe/results/unseen_bio | gru_phys | 2 of 81 (0 to 5) | 36 / 43 | -9 (-16 to -2) | +144 (38) | 105 of 1071 (0.098) | 3 of 31 | 0.055 of 472 / 0.132 of 599 |
| pnr_probe/results/unseen_bio | gru_phys_cusum | 4 of 81 (1 to 8) | 34 / 43 | -7 (-13 to -1) | +144 (38) | 138 of 1071 (0.129) | 6 of 31 | 0.076 of 472 / 0.170 of 599 |
| pnr_probe/results/unseen_bioplus | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_bioplus | mlp_phys | 4 of 81 (1 to 8) | 38 / 39 | -7 (-14 to -1) | +136 (42) | 13 of 1071 (0.012) | 1 of 31 | 0.004 of 472 / 0.018 of 599 |
| pnr_probe/results/unseen_bioplus | mlp_phys_cusum | 4 of 81 (1 to 8) | 13 / 64 | -7 (-13 to -1) | +112 (17) | 3 of 1071 (0.003) | 0 of 31 | 0.004 of 472 / 0.002 of 599 |
| pnr_probe/results/unseen_bioplus | gru_phys | 12 of 81 (6 to 19) | 41 / 28 | +1 (-6 to +8) | +152 (53) | 24 of 1071 (0.022) | 5 of 31 | 0.002 of 472 / 0.038 of 599 |
| pnr_probe/results/unseen_bioplus | gru_phys_cusum | 5 of 81 (1 to 10) | 32 / 44 | -6 (-13 to +0) | +144 (37) | 118 of 1071 (0.110) | 4 of 31 | 0.061 of 472 / 0.149 of 599 |
| pnr_probe/results/unseen_t1 | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| pnr_probe/results/unseen_t1 | mlp_phys | 4 of 81 (1 to 8) | 36 / 41 | -7 (-14 to +0) | +124 (40) | 61 of 1071 (0.057) | 1 of 31 | 0.038 of 472 / 0.072 of 599 |
| pnr_probe/results/unseen_t1 | mlp_phys_cusum | 1 of 81 (0 to 3) | 8 / 72 | -10 (-17 to -4) | +104 (9) | 20 of 1071 (0.019) | 3 of 31 | 0.013 of 472 / 0.023 of 599 |
| pnr_probe/results/unseen_t1 | gru_phys | 10 of 81 (5 to 16) | 33 / 38 | -1 (-9 to +7) | +136 (43) | 14 of 1071 (0.013) | 2 of 31 | 0.000 of 472 / 0.023 of 599 |
| pnr_probe/results/unseen_t1 | gru_phys_cusum | 3 of 81 (0 to 7) | 21 / 57 | -8 (-15 to -1) | +136 (24) | 47 of 1071 (0.044) | 2 of 31 | 0.089 of 472 / 0.008 of 599 |
