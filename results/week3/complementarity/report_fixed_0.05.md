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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/complementarity | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| results/week3/complementarity | gru_phys | 12 of 81 (6 to 19) | 32 / 37 | -5 (-14 to +4) | +112 (44) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| results/week3/complementarity | safe | 18 of 81 (11 to 25) | 33 / 30 | +1 (-9 to +11) | +48 (51) | 157 of 1071 (0.147) | 8 of 31 | 0.083 of 472 / 0.197 of 599 |
| results/week3/complementarity | hideseek | 13 of 81 (7 to 20) | 58 / 10 | -4 (-11 to +3) | +120 (71) | 40 of 1071 (0.037) | 18 of 31 | 0.049 of 472 / 0.028 of 599 |
| results/week3/complementarity | or_25 | 28 of 81 (20 to 36) | 46 / 7 | +11 (+3 to +19) | +80 (74) | 118 of 1071 (0.110) | 24 of 31 | 0.059 of 472 / 0.150 of 599 |
| results/week3/complementarity | or_50 | 26 of 81 (18 to 34) | 48 / 7 | +9 (+1 to +17) | +80 (74) | 111 of 1071 (0.104) | 26 of 31 | 0.055 of 472 / 0.142 of 599 |
| results/week3/complementarity | or_75 | 25 of 81 (17 to 33) | 46 / 10 | +8 (+2 to +14) | +96 (71) | 87 of 1071 (0.081) | 27 of 31 | 0.061 of 472 / 0.097 of 599 |
