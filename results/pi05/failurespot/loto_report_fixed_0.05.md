# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/failurespot/loto6 | progress | 0.052 | -104 (24) | 5 of 27 (2 to 9) | 0.027 | -144 (21) | 2 of 27 (0 to 5) |
| results/pi05/failurespot/loto6 | failurespot_mlp | 0.003 | none | 0 of 27 (0 to 0) | 0.001 | none | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto6 | failurespot_lstm | 0.017 | -144 (2) | 0 of 27 (0 to 0) | 0.013 | -112 (1) | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto6 | safe_mlp | 0.077 | -104 (21) | 7 of 27 (3 to 12) | 0.056 | -144 (19) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto6 | safe_lstm | 0.036 | -272 (5) | 1 of 27 (0 to 3) | 0.019 | -376 (5) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto6 | supervised_random_mlp | 0.048 | -4 (4) | 2 of 27 (0 to 5) | 0.017 | -200 (3) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto6 | supervised_random_lstm | 0.001 | -208 (2) | 1 of 27 (0 to 3) | 0.001 | +24 (1) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto6 | actprobe_mlp | 0.059 | -40 (21) | 8 of 27 (4 to 13) | 0.030 | -136 (15) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto6 | actprobe_lstm | 0.051 | -24 (20) | 8 of 27 (4 to 13) | 0.023 | -96 (19) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto6 | logpzo | 0.169 | +0 (4) | 2 of 27 (0 to 5) | 0.042 | none | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto6 | gru_phys | 0.019 | -72 (8) | 3 of 27 (0 to 6) | 0.011 | -128 (8) | 3 of 27 (0 to 6) |
| results/pi05/failurespot/loto6 | gru_phys_ttp | 0.011 | +96 (15) | 9 of 27 (4 to 14) | 0.007 | +64 (15) | 8 of 27 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/failurespot/loto6 | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 39 of 744 (0.052) | 6 of 7 | 0.041 of 291 / 0.060 of 453 |
| results/pi05/failurespot/loto6 | failurespot_mlp | 0 of 27 (0 to 0) | 0 / 27 | -5 (-9 to -1) | none | 2 of 744 (0.003) | 0 of 7 | 0.000 of 291 / 0.004 of 453 |
| results/pi05/failurespot/loto6 | failurespot_lstm | 0 of 27 (0 to 0) | 2 / 25 | -5 (-9 to -1) | +144 (2) | 13 of 744 (0.017) | 2 of 7 | 0.024 of 291 / 0.013 of 453 |
| results/pi05/failurespot/loto6 | safe_mlp | 7 of 27 (3 to 12) | 14 / 6 | +2 (-4 to +8) | +104 (21) | 57 of 744 (0.077) | 4 of 7 | 0.058 of 291 / 0.088 of 453 |
| results/pi05/failurespot/loto6 | safe_lstm | 1 of 27 (0 to 3) | 4 / 22 | -4 (-9 to +0) | +272 (5) | 27 of 744 (0.036) | 1 of 7 | 0.027 of 291 / 0.042 of 453 |
| results/pi05/failurespot/loto6 | supervised_random_mlp | 2 of 27 (0 to 5) | 2 / 23 | -3 (-8 to +2) | +4 (4) | 36 of 744 (0.048) | 5 of 7 | 0.055 of 291 / 0.044 of 453 |
| results/pi05/failurespot/loto6 | supervised_random_lstm | 1 of 27 (0 to 3) | 1 / 25 | -4 (-9 to +0) | +208 (2) | 1 of 744 (0.001) | 0 of 7 | 0.000 of 291 / 0.002 of 453 |
| results/pi05/failurespot/loto6 | actprobe_mlp | 8 of 27 (4 to 13) | 13 / 6 | +3 (-1 to +7) | +40 (21) | 44 of 744 (0.059) | 7 of 7 | 0.034 of 291 / 0.075 of 453 |
| results/pi05/failurespot/loto6 | actprobe_lstm | 8 of 27 (4 to 13) | 12 / 7 | +3 (+0 to +7) | +24 (20) | 38 of 744 (0.051) | 7 of 7 | 0.045 of 291 / 0.055 of 453 |
| results/pi05/failurespot/loto6 | logpzo | 2 of 27 (0 to 5) | 2 / 23 | -3 (-8 to +2) | +0 (4) | 126 of 744 (0.169) | 0 of 7 | 0.186 of 291 / 0.159 of 453 |
| results/pi05/failurespot/loto6 | gru_phys | 3 of 27 (0 to 6) | 5 / 19 | -2 (-7 to +3) | +72 (8) | 14 of 744 (0.019) | 1 of 7 | 0.010 of 291 / 0.024 of 453 |
| results/pi05/failurespot/loto6 | gru_phys_ttp | 9 of 27 (4 to 14) | 6 / 12 | +4 (+1 to +8) | -96 (15) | 8 of 744 (0.011) | 1 of 7 | 0.010 of 291 / 0.011 of 453 |
