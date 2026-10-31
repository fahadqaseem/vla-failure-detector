# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week3/failurespot/loto | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| results/week3/failurespot/loto | failurespot_mlp | 0.026 | -88 (3) | 0 of 81 (0 to 0) | 0.015 | -88 (3) | 0 of 81 (0 to 0) |
| results/week3/failurespot/loto | failurespot_lstm | 0.000 | none | 0 of 81 (0 to 0) | 0.000 | none | 0 of 81 (0 to 0) |
| results/week3/failurespot/loto | safe_mlp | 0.180 | -64 (53) | 22 of 81 (14 to 30) | 0.173 | -40 (47) | 21 of 81 (13 to 29) |
| results/week3/failurespot/loto | safe_lstm | 0.088 | -4 (16) | 8 of 81 (3 to 14) | 0.000 | none | 0 of 81 (0 to 0) |
| results/week3/failurespot/loto | supervised_random_mlp | 0.186 | -48 (57) | 25 of 81 (17 to 33) | 0.180 | -48 (50) | 22 of 81 (15 to 30) |
| results/week3/failurespot/loto | supervised_random_lstm | 0.114 | -24 (41) | 18 of 81 (11 to 26) | 0.081 | -76 (38) | 14 of 81 (8 to 21) |
| results/week3/failurespot/loto | actprobe_mlp | 0.018 | -120 (39) | 9 of 81 (4 to 15) | 0.018 | -120 (39) | 9 of 81 (4 to 15) |
| results/week3/failurespot/loto | actprobe_lstm | 0.204 | -136 (80) | 16 of 81 (9 to 23) | 0.195 | -152 (76) | 13 of 81 (7 to 20) |
| results/week3/failurespot/gru_phys/unseen | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| results/week3/failurespot/gru_phys/unseen | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.014 | -136 (43) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/failurespot/loto | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| results/week3/failurespot/loto | failurespot_mlp | 0 of 81 (0 to 0) | 3 / 78 | -11 (-17 to -5) | +88 (3) | 16 of 1071 (0.015) | 0 of 31 | 0.034 of 472 / 0.000 of 599 |
| results/week3/failurespot/loto | failurespot_lstm | 0 of 81 (0 to 0) | 0 / 81 | -11 (-17 to -5) | none | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| results/week3/failurespot/loto | safe_mlp | 21 of 81 (13 to 29) | 26 / 34 | +10 (+0 to +20) | +40 (47) | 185 of 1071 (0.173) | 9 of 31 | 0.104 of 472 / 0.227 of 599 |
| results/week3/failurespot/loto | safe_lstm | 0 of 81 (0 to 0) | 0 / 81 | -11 (-17 to -5) | none | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| results/week3/failurespot/loto | supervised_random_mlp | 22 of 81 (15 to 30) | 28 / 31 | +11 (+1 to +21) | +48 (50) | 193 of 1071 (0.180) | 5 of 31 | 0.106 of 472 / 0.239 of 599 |
| results/week3/failurespot/loto | supervised_random_lstm | 14 of 81 (8 to 21) | 24 / 43 | +3 (-6 to +12) | +76 (38) | 87 of 1071 (0.081) | 5 of 31 | 0.044 of 472 / 0.110 of 599 |
| results/week3/failurespot/loto | actprobe_mlp | 9 of 81 (4 to 15) | 30 / 42 | -2 (-9 to +5) | +120 (39) | 19 of 1071 (0.018) | 8 of 31 | 0.023 of 472 / 0.013 of 599 |
| results/week3/failurespot/loto | actprobe_lstm | 13 of 81 (7 to 20) | 63 / 5 | +2 (-5 to +9) | +152 (76) | 209 of 1071 (0.195) | 25 of 31 | 0.129 of 472 / 0.247 of 599 |
| results/week3/failurespot/gru_phys/unseen | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| results/week3/failurespot/gru_phys/unseen | gru_phys | 10 of 81 (5 to 16) | 33 / 38 | -1 (-9 to +7) | +136 (43) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
