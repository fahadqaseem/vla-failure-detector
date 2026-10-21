# Timely alarms with bootstrap 95% intervals, threshold time-varying 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_with_perturbed | timer | 8 of 46 (3 to 13) | -5 (-12 to +2) | +252 (46) | 81 of 743 (0.109) | 27 of 27 |
| results/predictor_with_perturbed | progress | 13 of 46 (7 to 19) |  | +108 (36) | 74 of 743 (0.100) | 12 of 27 |
| results/predictor_with_perturbed | safe | 9 of 46 (4 to 15) | -4 (-11 to +3) | +108 (32) | 81 of 743 (0.109) | 5 of 27 |
| results/predictor_with_perturbed | logreg | 5 of 46 (1 to 10) | -8 (-15 to -1) | -184 (5) | 99 of 743 (0.133) | 2 of 27 |
| results/predictor_with_perturbed | mlp | 6 of 46 (2 to 11) | -7 (-14 to +0) | +136 (29) | 97 of 743 (0.131) | 6 of 27 |
| results/predictor_with_perturbed | combined | 9 of 46 (4 to 15) | -4 (-11 to +3) | +128 (34) | 102 of 743 (0.137) | 8 of 27 |
| results/predictor_with_perturbed | mlp_reg | 10 of 46 (5 to 16) | -3 (-9 to +3) | +136 (35) | 104 of 743 (0.140) | 7 of 27 |
| results/predictor_with_perturbed | combined_reg | 12 of 46 (6 to 18) | -1 (-7 to +5) | +112 (35) | 106 of 743 (0.143) | 8 of 27 |
| results/predictor_with_perturbed | gated_mlp | 13 of 46 (7 to 19) | +0 (-4 to +4) | +88 (43) | 35 of 743 (0.047) | 21 of 27 |
| results/predictor_with_perturbed | gated_combined | 11 of 46 (6 to 17) | -2 (-7 to +3) | +96 (42) | 26 of 743 (0.035) | 22 of 27 |
| results/predictor_with_perturbed_seen_task | timer | 8 of 46 (3 to 13) | -6 (-11 to -1) | +236 (46) | 27 of 743 (0.036) | 27 of 27 |
| results/predictor_with_perturbed_seen_task | progress | 14 of 46 (8 to 20) |  | +68 (40) | 41 of 743 (0.055) | 23 of 27 |
| results/predictor_with_perturbed_seen_task | safe | 9 of 46 (4 to 14) | -5 (-11 to +1) | +48 (28) | 24 of 743 (0.032) | 18 of 27 |
| results/predictor_with_perturbed_seen_task | logreg | 15 of 46 (9 to 21) | +1 (-8 to +10) | -24 (27) | 37 of 743 (0.050) | 6 of 27 |
| results/predictor_with_perturbed_seen_task | mlp | 9 of 46 (4 to 15) | -5 (-13 to +3) | +24 (25) | 26 of 743 (0.035) | 5 of 27 |
| results/predictor_with_perturbed_seen_task | combined | 20 of 46 (14 to 26) | +6 (-3 to +15) | -28 (34) | 156 of 743 (0.210) | 17 of 27 |
| results/predictor_with_perturbed_seen_task | mlp_reg | 8 of 46 (3 to 13) | -6 (-13 to +0) | +56 (30) | 27 of 743 (0.036) | 10 of 27 |
| results/predictor_with_perturbed_seen_task | combined_reg | 12 of 46 (6 to 18) | -2 (-9 to +5) | +24 (29) | 39 of 743 (0.052) | 11 of 27 |
| results/predictor_with_perturbed_seen_task | gated_mlp | 10 of 46 (5 to 16) | -4 (-8 to -1) | +88 (41) | 40 of 743 (0.054) | 19 of 27 |
| results/predictor_with_perturbed_seen_task | gated_combined | 14 of 46 (8 to 20) | +0 (-4 to +4) | +84 (42) | 49 of 743 (0.066) | 23 of 27 |
