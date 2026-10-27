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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/unseen_surprise | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_surprise | mlp_phys | 3 of 81 (0 to 7) | 32 / 46 | -14 (-22 to -7) | +144 (35) | 143 of 1071 (0.134) | 13 of 31 | 0.093 of 472 / 0.165 of 599 |
| pnr_probe/results/unseen_surprise | mlp_phys_cusum | 1 of 81 (0 to 3) | 1 / 79 | -16 (-24 to -9) | +100 (2) | 17 of 1071 (0.016) | 0 of 31 | 0.036 of 472 / 0.000 of 599 |
| pnr_probe/results/unseen_surprise | gru_phys | 7 of 81 (3 to 12) | 44 / 30 | -10 (-18 to -2) | +128 (51) | 45 of 1071 (0.042) | 10 of 31 | 0.013 of 472 / 0.065 of 599 |
| pnr_probe/results/unseen_surprise | gru_phys_cusum | 2 of 81 (0 to 5) | 3 / 76 | -15 (-23 to -8) | +128 (5) | 47 of 1071 (0.044) | 3 of 31 | 0.100 of 472 / 0.000 of 599 |
| pnr_probe/results/unseen_csd | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_csd | mlp_phys | 10 of 81 (5 to 16) | 49 / 22 | -7 (-15 to +1) | +104 (59) | 104 of 1071 (0.097) | 11 of 31 | 0.061 of 472 / 0.125 of 599 |
| pnr_probe/results/unseen_csd | mlp_phys_cusum | 8 of 81 (3 to 14) | 21 / 52 | -9 (-16 to -2) | +88 (29) | 46 of 1071 (0.043) | 8 of 31 | 0.036 of 472 / 0.048 of 599 |
| pnr_probe/results/unseen_csd | gru_phys | 9 of 81 (4 to 15) | 50 / 22 | -8 (-15 to -1) | +120 (59) | 34 of 1071 (0.032) | 10 of 31 | 0.021 of 472 / 0.040 of 599 |
| pnr_probe/results/unseen_csd | gru_phys_cusum | 8 of 81 (3 to 14) | 47 / 26 | -9 (-16 to -2) | +112 (55) | 28 of 1071 (0.026) | 12 of 31 | 0.015 of 472 / 0.035 of 599 |
| pnr_probe/results/unseen_ttc | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_ttc | mlp_phys | 10 of 81 (5 to 16) | 4 / 67 | -7 (-17 to +3) | -32 (14) | 77 of 1071 (0.072) | 1 of 31 | 0.055 of 472 / 0.085 of 599 |
| pnr_probe/results/unseen_ttc | mlp_phys_cusum | 5 of 81 (1 to 10) | 23 / 53 | -12 (-21 to -4) | +76 (28) | 50 of 1071 (0.047) | 13 of 31 | 0.053 of 472 / 0.042 of 599 |
| pnr_probe/results/unseen_ttc | gru_phys | 9 of 81 (4 to 15) | 31 / 41 | -8 (-16 to +0) | +156 (40) | 78 of 1071 (0.073) | 20 of 31 | 0.083 of 472 / 0.065 of 599 |
| pnr_probe/results/unseen_ttc | gru_phys_cusum | 13 of 81 (7 to 20) | 31 / 37 | -4 (-10 to +2) | +84 (44) | 54 of 1071 (0.050) | 20 of 31 | 0.051 of 472 / 0.050 of 599 |
| pnr_probe/results/unseen_micro | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_micro | mlp_phys | 13 of 81 (7 to 20) | 46 / 22 | -4 (-11 to +3) | +160 (59) | 59 of 1071 (0.055) | 17 of 31 | 0.061 of 472 / 0.050 of 599 |
| pnr_probe/results/unseen_micro | mlp_phys_cusum | 11 of 81 (5 to 17) | 39 / 31 | -6 (-13 to +1) | +116 (50) | 62 of 1071 (0.058) | 18 of 31 | 0.070 of 472 / 0.048 of 599 |
| pnr_probe/results/unseen_micro | gru_phys | 14 of 81 (8 to 21) | 42 / 25 | -3 (-10 to +4) | +112 (56) | 50 of 1071 (0.047) | 20 of 31 | 0.038 of 472 / 0.053 of 599 |
| pnr_probe/results/unseen_micro | gru_phys_cusum | 10 of 81 (5 to 16) | 26 / 45 | -7 (-13 to -2) | +156 (36) | 53 of 1071 (0.049) | 21 of 31 | 0.053 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_bio | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_bio | mlp_phys | 6 of 81 (2 to 11) | 18 / 57 | -11 (-19 to -3) | +80 (24) | 22 of 1071 (0.021) | 4 of 31 | 0.011 of 472 / 0.028 of 599 |
| pnr_probe/results/unseen_bio | mlp_phys_cusum | 4 of 81 (1 to 8) | 18 / 59 | -13 (-21 to -6) | +136 (22) | 25 of 1071 (0.023) | 6 of 31 | 0.021 of 472 / 0.025 of 599 |
| pnr_probe/results/unseen_bio | gru_phys | 4 of 81 (1 to 8) | 40 / 37 | -13 (-21 to -5) | +148 (44) | 150 of 1071 (0.140) | 4 of 31 | 0.089 of 472 / 0.180 of 599 |
| pnr_probe/results/unseen_bio | gru_phys_cusum | 6 of 81 (2 to 11) | 36 / 39 | -11 (-18 to -4) | +96 (42) | 169 of 1071 (0.158) | 9 of 31 | 0.104 of 472 / 0.200 of 599 |
| pnr_probe/results/unseen_bioplus | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_bioplus | mlp_phys | 8 of 81 (3 to 14) | 41 / 32 | -9 (-16 to -2) | +88 (49) | 31 of 1071 (0.029) | 1 of 31 | 0.019 of 472 / 0.037 of 599 |
| pnr_probe/results/unseen_bioplus | mlp_phys_cusum | 6 of 81 (2 to 11) | 13 / 62 | -11 (-18 to -4) | +104 (19) | 13 of 1071 (0.012) | 1 of 31 | 0.011 of 472 / 0.013 of 599 |
| pnr_probe/results/unseen_bioplus | gru_phys | 16 of 81 (9 to 23) | 43 / 22 | -1 (-9 to +7) | +112 (59) | 75 of 1071 (0.070) | 8 of 31 | 0.034 of 472 / 0.098 of 599 |
| pnr_probe/results/unseen_bioplus | gru_phys_cusum | 5 of 81 (1 to 10) | 36 / 40 | -12 (-20 to -4) | +128 (41) | 149 of 1071 (0.139) | 7 of 31 | 0.083 of 472 / 0.184 of 599 |
| pnr_probe/results/unseen_t1 | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/unseen_t1 | mlp_phys | 6 of 81 (2 to 11) | 42 / 33 | -11 (-20 to -2) | +136 (48) | 64 of 1071 (0.060) | 1 of 31 | 0.038 of 472 / 0.077 of 599 |
| pnr_probe/results/unseen_t1 | mlp_phys_cusum | 1 of 81 (0 to 3) | 15 / 65 | -16 (-24 to -9) | +108 (16) | 55 of 1071 (0.051) | 7 of 31 | 0.036 of 472 / 0.063 of 599 |
| pnr_probe/results/unseen_t1 | gru_phys | 12 of 81 (6 to 19) | 32 / 37 | -5 (-14 to +4) | +112 (44) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| pnr_probe/results/unseen_t1 | gru_phys_cusum | 4 of 81 (1 to 8) | 24 / 53 | -13 (-21 to -5) | +128 (28) | 126 of 1071 (0.118) | 2 of 31 | 0.144 of 472 / 0.097 of 599 |
