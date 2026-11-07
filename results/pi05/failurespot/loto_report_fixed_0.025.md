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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/failurespot/loto6 | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 20 of 744 (0.027) | 6 of 7 | 0.024 of 291 / 0.029 of 453 |
| results/pi05/failurespot/loto6 | failurespot_mlp | 0 of 27 (0 to 0) | 0 / 27 | -2 (-5 to +0) | none | 1 of 744 (0.001) | 0 of 7 | 0.000 of 291 / 0.002 of 453 |
| results/pi05/failurespot/loto6 | failurespot_lstm | 0 of 27 (0 to 0) | 1 / 26 | -2 (-5 to +0) | +112 (1) | 10 of 744 (0.013) | 1 of 7 | 0.017 of 291 / 0.011 of 453 |
| results/pi05/failurespot/loto6 | safe_mlp | 5 of 27 (1 to 9) | 14 / 8 | +3 (-2 to +8) | +144 (19) | 42 of 744 (0.056) | 1 of 7 | 0.034 of 291 / 0.071 of 453 |
| results/pi05/failurespot/loto6 | safe_lstm | 1 of 27 (0 to 3) | 4 / 22 | -1 (-4 to +2) | +376 (5) | 14 of 744 (0.019) | 1 of 7 | 0.021 of 291 / 0.018 of 453 |
| results/pi05/failurespot/loto6 | supervised_random_mlp | 1 of 27 (0 to 3) | 2 / 24 | -1 (-4 to +2) | +200 (3) | 13 of 744 (0.017) | 3 of 7 | 0.017 of 291 / 0.018 of 453 |
| results/pi05/failurespot/loto6 | supervised_random_lstm | 1 of 27 (0 to 3) | 0 / 26 | -1 (-4 to +2) | -24 (1) | 1 of 744 (0.001) | 0 of 7 | 0.000 of 291 / 0.002 of 453 |
| results/pi05/failurespot/loto6 | actprobe_mlp | 5 of 27 (1 to 9) | 10 / 12 | +3 (+0 to +6) | +136 (15) | 22 of 744 (0.030) | 6 of 7 | 0.017 of 291 / 0.038 of 453 |
| results/pi05/failurespot/loto6 | actprobe_lstm | 5 of 27 (1 to 9) | 14 / 8 | +3 (+0 to +7) | +96 (19) | 17 of 744 (0.023) | 7 of 7 | 0.021 of 291 / 0.024 of 453 |
| results/pi05/failurespot/loto6 | logpzo | 0 of 27 (0 to 0) | 0 / 27 | -2 (-5 to +0) | none | 31 of 744 (0.042) | 0 of 7 | 0.052 of 291 / 0.035 of 453 |
| results/pi05/failurespot/loto6 | gru_phys | 3 of 27 (0 to 6) | 5 / 19 | +1 (-3 to +5) | +128 (8) | 8 of 744 (0.011) | 1 of 7 | 0.003 of 291 / 0.015 of 453 |
| results/pi05/failurespot/loto6 | gru_phys_ttp | 8 of 27 (4 to 13) | 7 / 12 | +6 (+1 to +11) | -64 (15) | 5 of 744 (0.007) | 1 of 7 | 0.007 of 291 / 0.007 of 453 |
