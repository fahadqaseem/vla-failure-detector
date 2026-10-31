# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week3/complementarity | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| results/week3/complementarity | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.014 | -136 (43) | 10 of 81 (5 to 16) |
| results/week3/complementarity | safe | 0.147 | -48 (51) | 18 of 81 (11 to 25) | 0.077 | -40 (42) | 13 of 81 (7 to 20) |
| results/week3/complementarity | hideseek | 0.037 | -120 (71) | 13 of 81 (7 to 20) | 0.025 | -136 (71) | 11 of 81 (5 to 17) |
| results/week3/complementarity | or_25 | 0.110 | -80 (74) | 28 of 81 (20 to 37) | 0.064 | -88 (65) | 21 of 81 (13 to 29) |
| results/week3/complementarity | or_50 | 0.104 | -80 (74) | 26 of 81 (18 to 34) | 0.040 | -104 (65) | 20 of 81 (13 to 28) |
| results/week3/complementarity | or_75 | 0.081 | -96 (71) | 25 of 81 (17 to 33) | 0.029 | -152 (63) | 17 of 81 (10 to 24) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/complementarity | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| results/week3/complementarity | gru_phys | 10 of 81 (5 to 16) | 33 / 38 | -1 (-9 to +7) | +136 (43) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| results/week3/complementarity | safe | 13 of 81 (7 to 20) | 29 / 39 | +2 (-7 to +11) | +40 (42) | 82 of 1071 (0.077) | 7 of 31 | 0.030 of 472 / 0.114 of 599 |
| results/week3/complementarity | hideseek | 11 of 81 (5 to 17) | 60 / 10 | +0 (-6 to +6) | +136 (71) | 27 of 1071 (0.025) | 16 of 31 | 0.023 of 472 / 0.027 of 599 |
| results/week3/complementarity | or_25 | 21 of 81 (13 to 29) | 44 / 16 | +10 (+3 to +17) | +88 (65) | 69 of 1071 (0.064) | 21 of 31 | 0.028 of 472 / 0.093 of 599 |
| results/week3/complementarity | or_50 | 20 of 81 (13 to 28) | 45 / 16 | +9 (+3 to +15) | +104 (65) | 43 of 1071 (0.040) | 21 of 31 | 0.023 of 472 / 0.053 of 599 |
| results/week3/complementarity | or_75 | 17 of 81 (10 to 24) | 46 / 18 | +6 (+2 to +11) | +152 (63) | 31 of 1071 (0.029) | 22 of 31 | 0.025 of 472 / 0.032 of 599 |
