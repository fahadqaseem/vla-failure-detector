# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/failurespot/loto | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| results/pi05/failurespot/loto | failurespot_mlp | 0.047 | none | 0 of 27 (0 to 0) | 0.027 | none | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto | failurespot_lstm | 0.022 | -144 (2) | 0 of 27 (0 to 0) | 0.012 | -112 (1) | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto | safe_mlp | 0.064 | -104 (21) | 7 of 27 (3 to 12) | 0.045 | -144 (19) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto | safe_lstm | 0.077 | -272 (5) | 1 of 27 (0 to 3) | 0.019 | -376 (5) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto | supervised_random_mlp | 0.040 | -4 (4) | 2 of 27 (0 to 5) | 0.014 | -200 (3) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto | supervised_random_lstm | 0.001 | -208 (2) | 1 of 27 (0 to 3) | 0.001 | +24 (1) | 1 of 27 (0 to 3) |
| results/pi05/failurespot/loto | actprobe_mlp | 0.055 | -40 (21) | 8 of 27 (4 to 13) | 0.026 | -136 (15) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto | actprobe_lstm | 0.043 | -24 (20) | 8 of 27 (4 to 13) | 0.019 | -96 (19) | 5 of 27 (1 to 9) |
| results/pi05/failurespot/loto | logpzo | 0.186 | +0 (4) | 2 of 27 (0 to 5) | 0.084 | none | 0 of 27 (0 to 0) |
| results/pi05/failurespot/loto | gru_phys | 0.015 | -72 (8) | 3 of 27 (0 to 6) | 0.009 | -128 (8) | 3 of 27 (0 to 6) |
| results/pi05/failurespot/loto | gru_phys_ttp | 0.009 | +96 (15) | 9 of 27 (4 to 14) | 0.005 | +64 (15) | 8 of 27 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/failurespot/loto | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| results/pi05/failurespot/loto | failurespot_mlp | 0 of 27 (0 to 0) | 0 / 27 | -2 (-5 to +0) | none | 25 of 928 (0.027) | 0 of 7 | 0.051 of 475 / 0.002 of 453 |
| results/pi05/failurespot/loto | failurespot_lstm | 0 of 27 (0 to 0) | 1 / 26 | -2 (-5 to +0) | +112 (1) | 11 of 928 (0.012) | 1 of 7 | 0.013 of 475 / 0.011 of 453 |
| results/pi05/failurespot/loto | safe_mlp | 5 of 27 (1 to 9) | 14 / 8 | +3 (-2 to +8) | +144 (19) | 42 of 928 (0.045) | 1 of 7 | 0.021 of 475 / 0.071 of 453 |
| results/pi05/failurespot/loto | safe_lstm | 1 of 27 (0 to 3) | 4 / 22 | -1 (-4 to +2) | +376 (5) | 18 of 928 (0.019) | 1 of 7 | 0.021 of 475 / 0.018 of 453 |
| results/pi05/failurespot/loto | supervised_random_mlp | 1 of 27 (0 to 3) | 2 / 24 | -1 (-4 to +2) | +200 (3) | 13 of 928 (0.014) | 3 of 7 | 0.011 of 475 / 0.018 of 453 |
| results/pi05/failurespot/loto | supervised_random_lstm | 1 of 27 (0 to 3) | 0 / 26 | -1 (-4 to +2) | -24 (1) | 1 of 928 (0.001) | 0 of 7 | 0.000 of 475 / 0.002 of 453 |
| results/pi05/failurespot/loto | actprobe_mlp | 5 of 27 (1 to 9) | 10 / 12 | +3 (+0 to +6) | +136 (15) | 24 of 928 (0.026) | 6 of 7 | 0.015 of 475 / 0.038 of 453 |
| results/pi05/failurespot/loto | actprobe_lstm | 5 of 27 (1 to 9) | 14 / 8 | +3 (+0 to +7) | +96 (19) | 18 of 928 (0.019) | 7 of 7 | 0.015 of 475 / 0.024 of 453 |
| results/pi05/failurespot/loto | logpzo | 0 of 27 (0 to 0) | 0 / 27 | -2 (-5 to +0) | none | 78 of 928 (0.084) | 0 of 7 | 0.131 of 475 / 0.035 of 453 |
| results/pi05/failurespot/loto | gru_phys | 3 of 27 (0 to 6) | 5 / 19 | +1 (-3 to +5) | +128 (8) | 8 of 928 (0.009) | 1 of 7 | 0.002 of 475 / 0.015 of 453 |
| results/pi05/failurespot/loto | gru_phys_ttp | 8 of 27 (4 to 13) | 7 / 12 | +6 (+1 to +11) | -64 (15) | 5 of 928 (0.005) | 1 of 7 | 0.004 of 475 / 0.007 of 453 |
