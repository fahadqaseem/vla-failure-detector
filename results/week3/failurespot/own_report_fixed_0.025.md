# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week3/failurespot/own/g0 | actprobe_lstm | 0.232 | -108 (46) | 13 of 46 (7 to 19) | 0.200 | -120 (46) | 12 of 46 (6 to 18) |
| results/week3/failurespot/own/g0 | actprobe_mlp | 0.012 | +344 (1) | 1 of 46 (0 to 3) | 0.006 | none | 0 of 46 (0 to 0) |
| results/week3/failurespot/own/g0 | failurespot_lstm | 0.056 | +176 (1) | 1 of 46 (0 to 3) | 0.009 | none | 0 of 46 (0 to 0) |
| results/week3/failurespot/own/g0 | failurespot_mlp | 0.121 | -88 (17) | 2 of 46 (0 to 5) | 0.046 | -124 (8) | 1 of 46 (0 to 3) |
| results/week3/failurespot/own/g0 | safe_lstm | 0.051 | -232 (14) | 4 of 46 (1 to 8) | 0.037 | -240 (11) | 3 of 46 (0 to 7) |
| results/week3/failurespot/own/g0 | safe_mlp | 0.063 | -56 (39) | 11 of 46 (6 to 17) | 0.008 | -92 (26) | 6 of 46 (2 to 11) |
| results/week3/failurespot/own/g0 | supervised_random_lstm | 0.059 | -32 (9) | 3 of 46 (0 to 7) | 0.003 | +16 (5) | 3 of 46 (0 to 7) |
| results/week3/failurespot/own/g0 | supervised_random_mlp | 0.294 | -16 (44) | 20 of 46 (13 to 26) | 0.040 | -64 (38) | 6 of 46 (2 to 11) |
| results/week3/failurespot/own/g1 | actprobe_lstm | 0.056 | -96 (45) | 11 of 47 (6 to 17) | 0.039 | -108 (44) | 9 of 47 (4 to 15) |
| results/week3/failurespot/own/g1 | actprobe_mlp | 0.069 | +344 (1) | 1 of 47 (0 to 3) | 0.049 | +344 (1) | 1 of 47 (0 to 3) |
| results/week3/failurespot/own/g1 | failurespot_lstm | 0.142 | +168 (2) | 2 of 47 (0 to 5) | 0.105 | +168 (2) | 2 of 47 (0 to 5) |
| results/week3/failurespot/own/g1 | failurespot_mlp | 0.047 | -172 (4) | 0 of 47 (0 to 0) | 0.041 | -172 (4) | 0 of 47 (0 to 0) |
| results/week3/failurespot/own/g1 | safe_lstm | 0.081 | -220 (38) | 2 of 47 (0 to 5) | 0.013 | -272 (27) | 0 of 47 (0 to 0) |
| results/week3/failurespot/own/g1 | safe_mlp | 0.030 | -64 (41) | 10 of 47 (5 to 16) | 0.017 | -64 (39) | 8 of 47 (3 to 13) |
| results/week3/failurespot/own/g1 | supervised_random_lstm | 0.036 | -160 (41) | 2 of 47 (0 to 5) | 0.013 | -192 (34) | 1 of 47 (0 to 3) |
| results/week3/failurespot/own/g1 | supervised_random_mlp | 0.114 | -40 (44) | 14 of 47 (8 to 20) | 0.014 | -100 (34) | 2 of 47 (0 to 5) |
| results/week3/failurespot/own/g2 | actprobe_lstm | 0.076 | -184 (57) | 6 of 57 (2 to 11) | 0.042 | -200 (57) | 6 of 57 (2 to 11) |
| results/week3/failurespot/own/g2 | actprobe_mlp | 0.026 | -296 (1) | 0 of 57 (0 to 0) | 0.007 | -296 (1) | 0 of 57 (0 to 0) |
| results/week3/failurespot/own/g2 | failurespot_lstm | 0.098 | +116 (4) | 4 of 57 (1 to 8) | 0.017 | +176 (3) | 3 of 57 (0 to 7) |
| results/week3/failurespot/own/g2 | failurespot_mlp | 0.331 | +36 (22) | 18 of 57 (11 to 25) | 0.275 | +16 (16) | 14 of 57 (8 to 21) |
| results/week3/failurespot/own/g2 | safe_lstm | 0.043 | -304 (29) | 1 of 57 (0 to 3) | 0.024 | -304 (16) | 1 of 57 (0 to 3) |
| results/week3/failurespot/own/g2 | safe_mlp | 0.276 | -72 (49) | 18 of 57 (11 to 25) | 0.263 | -72 (43) | 17 of 57 (11 to 24) |
| results/week3/failurespot/own/g2 | supervised_random_lstm | 0.032 | -128 (9) | 2 of 57 (0 to 5) | 0.006 | -152 (8) | 1 of 57 (0 to 3) |
| results/week3/failurespot/own/g2 | supervised_random_mlp | 0.224 | -48 (36) | 15 of 57 (9 to 22) | 0.045 | -64 (24) | 9 of 57 (4 to 15) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/failurespot/own/g0 | actprobe_lstm | 12 of 46 (6 to 18) | 34 / 0 |  | +120 (46) | 156 of 780 (0.200) | 25 of 25 | 0.291 of 330 / 0.133 of 450 |
| results/week3/failurespot/own/g0 | actprobe_mlp | 0 of 46 (0 to 0) | 0 / 46 |  | none | 5 of 780 (0.006) | 0 of 25 | 0.009 of 330 / 0.004 of 450 |
| results/week3/failurespot/own/g0 | failurespot_lstm | 0 of 46 (0 to 0) | 0 / 46 |  | none | 7 of 780 (0.009) | 0 of 25 | 0.015 of 330 / 0.004 of 450 |
| results/week3/failurespot/own/g0 | failurespot_mlp | 1 of 46 (0 to 3) | 7 / 38 |  | +124 (8) | 36 of 780 (0.046) | 1 of 25 | 0.070 of 330 / 0.029 of 450 |
| results/week3/failurespot/own/g0 | safe_lstm | 3 of 46 (0 to 7) | 8 / 35 |  | +240 (11) | 29 of 780 (0.037) | 4 of 25 | 0.073 of 330 / 0.011 of 450 |
| results/week3/failurespot/own/g0 | safe_mlp | 6 of 46 (2 to 11) | 20 / 20 |  | +92 (26) | 6 of 780 (0.008) | 2 of 25 | 0.000 of 330 / 0.013 of 450 |
| results/week3/failurespot/own/g0 | supervised_random_lstm | 3 of 46 (0 to 7) | 2 / 41 |  | -16 (5) | 2 of 780 (0.003) | 0 of 25 | 0.000 of 330 / 0.004 of 450 |
| results/week3/failurespot/own/g0 | supervised_random_mlp | 6 of 46 (2 to 11) | 32 / 8 |  | +64 (38) | 31 of 780 (0.040) | 10 of 25 | 0.024 of 330 / 0.051 of 450 |
| results/week3/failurespot/own/g1 | actprobe_lstm | 9 of 47 (4 to 15) | 35 / 3 |  | +108 (44) | 25 of 639 (0.039) | 13 of 15 | 0.042 of 334 / 0.036 of 305 |
| results/week3/failurespot/own/g1 | actprobe_mlp | 1 of 47 (0 to 3) | 0 / 46 |  | -344 (1) | 31 of 639 (0.049) | 0 of 15 | 0.063 of 334 / 0.033 of 305 |
| results/week3/failurespot/own/g1 | failurespot_lstm | 2 of 47 (0 to 5) | 0 / 45 |  | -168 (2) | 67 of 639 (0.105) | 2 of 15 | 0.120 of 334 / 0.089 of 305 |
| results/week3/failurespot/own/g1 | failurespot_mlp | 0 of 47 (0 to 0) | 4 / 43 |  | +172 (4) | 26 of 639 (0.041) | 2 of 15 | 0.063 of 334 / 0.016 of 305 |
| results/week3/failurespot/own/g1 | safe_lstm | 0 of 47 (0 to 0) | 27 / 20 |  | +272 (27) | 8 of 639 (0.013) | 3 of 15 | 0.021 of 334 / 0.003 of 305 |
| results/week3/failurespot/own/g1 | safe_mlp | 8 of 47 (3 to 13) | 31 / 8 |  | +64 (39) | 11 of 639 (0.017) | 7 of 15 | 0.015 of 334 / 0.020 of 305 |
| results/week3/failurespot/own/g1 | supervised_random_lstm | 1 of 47 (0 to 3) | 33 / 13 |  | +192 (34) | 8 of 639 (0.013) | 7 of 15 | 0.012 of 334 / 0.013 of 305 |
| results/week3/failurespot/own/g1 | supervised_random_mlp | 2 of 47 (0 to 5) | 32 / 13 |  | +100 (34) | 9 of 639 (0.014) | 5 of 15 | 0.015 of 334 / 0.013 of 305 |
| results/week3/failurespot/own/g2 | actprobe_lstm | 6 of 57 (2 to 11) | 51 / 0 |  | +200 (57) | 29 of 695 (0.042) | 28 of 28 | 0.043 of 327 / 0.041 of 368 |
| results/week3/failurespot/own/g2 | actprobe_mlp | 0 of 57 (0 to 0) | 1 / 56 |  | +296 (1) | 5 of 695 (0.007) | 0 of 28 | 0.015 of 327 / 0.000 of 368 |
| results/week3/failurespot/own/g2 | failurespot_lstm | 3 of 57 (0 to 7) | 0 / 54 |  | -176 (3) | 12 of 695 (0.017) | 0 of 28 | 0.015 of 327 / 0.019 of 368 |
| results/week3/failurespot/own/g2 | failurespot_mlp | 14 of 57 (8 to 21) | 2 / 41 |  | -16 (16) | 191 of 695 (0.275) | 3 of 28 | 0.180 of 327 / 0.359 of 368 |
| results/week3/failurespot/own/g2 | safe_lstm | 1 of 57 (0 to 3) | 15 / 41 |  | +304 (16) | 17 of 695 (0.024) | 2 of 28 | 0.000 of 327 / 0.046 of 368 |
| results/week3/failurespot/own/g2 | safe_mlp | 17 of 57 (11 to 24) | 26 / 14 |  | +72 (43) | 183 of 695 (0.263) | 5 of 28 | 0.165 of 327 / 0.351 of 368 |
| results/week3/failurespot/own/g2 | supervised_random_lstm | 1 of 57 (0 to 3) | 7 / 49 |  | +152 (8) | 4 of 695 (0.006) | 3 of 28 | 0.000 of 327 / 0.011 of 368 |
| results/week3/failurespot/own/g2 | supervised_random_mlp | 9 of 57 (4 to 15) | 15 / 33 |  | +64 (24) | 31 of 695 (0.045) | 4 of 28 | 0.009 of 327 / 0.076 of 368 |
