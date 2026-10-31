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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/failurespot/own/g0 | actprobe_lstm | 13 of 46 (7 to 19) | 33 / 0 |  | +108 (46) | 181 of 780 (0.232) | 25 of 25 | 0.339 of 330 / 0.153 of 450 |
| results/week3/failurespot/own/g0 | actprobe_mlp | 1 of 46 (0 to 3) | 0 / 45 |  | -344 (1) | 9 of 780 (0.012) | 0 of 25 | 0.018 of 330 / 0.007 of 450 |
| results/week3/failurespot/own/g0 | failurespot_lstm | 1 of 46 (0 to 3) | 0 / 45 |  | -176 (1) | 44 of 780 (0.056) | 1 of 25 | 0.048 of 330 / 0.062 of 450 |
| results/week3/failurespot/own/g0 | failurespot_mlp | 2 of 46 (0 to 5) | 15 / 29 |  | +88 (17) | 94 of 780 (0.121) | 3 of 25 | 0.127 of 330 / 0.116 of 450 |
| results/week3/failurespot/own/g0 | safe_lstm | 4 of 46 (1 to 8) | 10 / 32 |  | +232 (14) | 40 of 780 (0.051) | 4 of 25 | 0.097 of 330 / 0.018 of 450 |
| results/week3/failurespot/own/g0 | safe_mlp | 11 of 46 (6 to 17) | 28 / 7 |  | +56 (39) | 49 of 780 (0.063) | 9 of 25 | 0.042 of 330 / 0.078 of 450 |
| results/week3/failurespot/own/g0 | supervised_random_lstm | 3 of 46 (0 to 7) | 6 / 37 |  | +32 (9) | 46 of 780 (0.059) | 3 of 25 | 0.088 of 330 / 0.038 of 450 |
| results/week3/failurespot/own/g0 | supervised_random_mlp | 20 of 46 (13 to 26) | 24 / 2 |  | +16 (44) | 229 of 780 (0.294) | 17 of 25 | 0.267 of 330 / 0.313 of 450 |
| results/week3/failurespot/own/g1 | actprobe_lstm | 11 of 47 (6 to 17) | 34 / 2 |  | +96 (45) | 36 of 639 (0.056) | 14 of 15 | 0.057 of 334 / 0.056 of 305 |
| results/week3/failurespot/own/g1 | actprobe_mlp | 1 of 47 (0 to 3) | 0 / 46 |  | -344 (1) | 44 of 639 (0.069) | 0 of 15 | 0.087 of 334 / 0.049 of 305 |
| results/week3/failurespot/own/g1 | failurespot_lstm | 2 of 47 (0 to 5) | 0 / 45 |  | -168 (2) | 91 of 639 (0.142) | 3 of 15 | 0.159 of 334 / 0.125 of 305 |
| results/week3/failurespot/own/g1 | failurespot_mlp | 0 of 47 (0 to 0) | 4 / 43 |  | +172 (4) | 30 of 639 (0.047) | 2 of 15 | 0.069 of 334 / 0.023 of 305 |
| results/week3/failurespot/own/g1 | safe_lstm | 2 of 47 (0 to 5) | 36 / 9 |  | +220 (38) | 52 of 639 (0.081) | 6 of 15 | 0.114 of 334 / 0.046 of 305 |
| results/week3/failurespot/own/g1 | safe_mlp | 10 of 47 (5 to 16) | 31 / 6 |  | +64 (41) | 19 of 639 (0.030) | 8 of 15 | 0.030 of 334 / 0.030 of 305 |
| results/week3/failurespot/own/g1 | supervised_random_lstm | 2 of 47 (0 to 5) | 39 / 6 |  | +160 (41) | 23 of 639 (0.036) | 8 of 15 | 0.054 of 334 / 0.016 of 305 |
| results/week3/failurespot/own/g1 | supervised_random_mlp | 14 of 47 (8 to 20) | 30 / 3 |  | +40 (44) | 73 of 639 (0.114) | 12 of 15 | 0.138 of 334 / 0.089 of 305 |
| results/week3/failurespot/own/g2 | actprobe_lstm | 6 of 57 (2 to 11) | 51 / 0 |  | +184 (57) | 53 of 695 (0.076) | 28 of 28 | 0.080 of 327 / 0.073 of 368 |
| results/week3/failurespot/own/g2 | actprobe_mlp | 0 of 57 (0 to 0) | 1 / 56 |  | +296 (1) | 18 of 695 (0.026) | 0 of 28 | 0.037 of 327 / 0.016 of 368 |
| results/week3/failurespot/own/g2 | failurespot_lstm | 4 of 57 (1 to 8) | 0 / 53 |  | -116 (4) | 68 of 695 (0.098) | 4 of 28 | 0.089 of 327 / 0.106 of 368 |
| results/week3/failurespot/own/g2 | failurespot_mlp | 18 of 57 (11 to 25) | 4 / 35 |  | -36 (22) | 230 of 695 (0.331) | 4 of 28 | 0.275 of 327 / 0.380 of 368 |
| results/week3/failurespot/own/g2 | safe_lstm | 1 of 57 (0 to 3) | 28 / 28 |  | +304 (29) | 30 of 695 (0.043) | 2 of 28 | 0.003 of 327 / 0.079 of 368 |
| results/week3/failurespot/own/g2 | safe_mlp | 18 of 57 (11 to 25) | 31 / 8 |  | +72 (49) | 192 of 695 (0.276) | 7 of 28 | 0.174 of 327 / 0.367 of 368 |
| results/week3/failurespot/own/g2 | supervised_random_lstm | 2 of 57 (0 to 5) | 7 / 48 |  | +128 (9) | 22 of 695 (0.032) | 3 of 28 | 0.015 of 327 / 0.046 of 368 |
| results/week3/failurespot/own/g2 | supervised_random_mlp | 15 of 57 (9 to 22) | 21 / 21 |  | +48 (36) | 156 of 695 (0.224) | 5 of 28 | 0.113 of 327 / 0.323 of 368 |
