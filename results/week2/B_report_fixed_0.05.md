# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/B_lookahead | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 4 of 150 (0.027) | 23 of 27 | 0.030 of 100 / 0.020 of 50 |
| results/week2/B_lookahead | lookahead_nomove | 0 of 46 (0 to 0) | 0 / 46 | -11 (-17 to -6) | none | 0 of 150 (0.000) | 0 of 27 | 0.000 of 100 / 0.000 of 50 |
| results/week2/B_lookahead | lookahead_mlp | 3 of 46 (0 to 7) | 1 / 42 | -8 (-15 to -1) | -104 (4) | 17 of 150 (0.113) | 2 of 27 | 0.100 of 100 / 0.140 of 50 |
| results/week2/B_lookahead | lookahead_nosucc | 0 of 46 (0 to 0) | 0 / 46 | -11 (-17 to -6) | none | 0 of 150 (0.000) | 0 of 27 | 0.000 of 100 / 0.000 of 50 |
