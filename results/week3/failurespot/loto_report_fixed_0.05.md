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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/failurespot/loto | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| results/week3/failurespot/loto | failurespot_mlp | 0 of 81 (0 to 0) | 3 / 78 | -17 (-24 to -10) | +88 (3) | 28 of 1071 (0.026) | 0 of 31 | 0.059 of 472 / 0.000 of 599 |
| results/week3/failurespot/loto | failurespot_lstm | 0 of 81 (0 to 0) | 0 / 81 | -17 (-24 to -10) | none | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| results/week3/failurespot/loto | safe_mlp | 22 of 81 (14 to 30) | 31 / 28 | +5 (-5 to +15) | +64 (53) | 193 of 1071 (0.180) | 9 of 31 | 0.110 of 472 / 0.235 of 599 |
| results/week3/failurespot/loto | safe_lstm | 8 of 81 (3 to 14) | 8 / 65 | -9 (-18 to +0) | +4 (16) | 94 of 1071 (0.088) | 4 of 31 | 0.025 of 472 / 0.137 of 599 |
| results/week3/failurespot/loto | supervised_random_mlp | 25 of 81 (17 to 33) | 32 / 24 | +8 (-3 to +19) | +48 (57) | 199 of 1071 (0.186) | 8 of 31 | 0.112 of 472 / 0.244 of 599 |
| results/week3/failurespot/loto | supervised_random_lstm | 18 of 81 (11 to 26) | 23 / 40 | +1 (-10 to +12) | +24 (41) | 122 of 1071 (0.114) | 5 of 31 | 0.055 of 472 / 0.160 of 599 |
| results/week3/failurespot/loto | actprobe_mlp | 9 of 81 (4 to 15) | 30 / 42 | -8 (-15 to -1) | +120 (39) | 19 of 1071 (0.018) | 8 of 31 | 0.023 of 472 / 0.013 of 599 |
| results/week3/failurespot/loto | actprobe_lstm | 16 of 81 (9 to 23) | 64 / 1 | -1 (-9 to +7) | +136 (80) | 218 of 1071 (0.204) | 26 of 31 | 0.138 of 472 / 0.255 of 599 |
| results/week3/failurespot/gru_phys/unseen | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| results/week3/failurespot/gru_phys/unseen | gru_phys | 12 of 81 (6 to 19) | 32 / 37 | -5 (-14 to +4) | +112 (44) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
