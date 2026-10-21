# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_with_perturbed | timer | 9 of 46 (4 to 15) | -6 (-12 to +0) | +192 (46) | 88 of 743 (0.118) | 27 of 27 |
| results/predictor_with_perturbed | progress | 15 of 46 (9 to 21) |  | +92 (42) | 67 of 743 (0.090) | 25 of 27 |
| results/predictor_with_perturbed | safe | 8 of 46 (3 to 13) | -7 (-14 to +0) | +112 (40) | 100 of 743 (0.135) | 13 of 27 |
| results/predictor_with_perturbed | logreg | 9 of 46 (4 to 14) | -6 (-14 to +2) | +96 (38) | 111 of 743 (0.149) | 11 of 27 |
| results/predictor_with_perturbed | mlp | 6 of 46 (2 to 11) | -9 (-16 to -2) | +104 (26) | 108 of 743 (0.145) | 7 of 27 |
| results/predictor_with_perturbed | combined | 11 of 46 (6 to 17) | -4 (-10 to +2) | +72 (31) | 109 of 743 (0.147) | 8 of 27 |
| results/predictor_with_perturbed | mlp_reg | 6 of 46 (2 to 11) | -9 (-16 to -2) | +96 (21) | 80 of 743 (0.108) | 3 of 27 |
| results/predictor_with_perturbed | combined_reg | 9 of 46 (4 to 15) | -6 (-13 to +1) | +64 (23) | 106 of 743 (0.143) | 6 of 27 |
| results/predictor_with_perturbed | gated_mlp | 15 of 46 (9 to 21) | +0 (-3 to +3) | +76 (44) | 65 of 743 (0.087) | 24 of 27 |
| results/predictor_with_perturbed | gated_combined | 16 of 46 (10 to 22) | +1 (+0 to +3) | +60 (44) | 65 of 743 (0.087) | 26 of 27 |
| results/predictor_with_perturbed_seen_task | timer | 8 of 46 (3 to 13) | -8 (-14 to -2) | +192 (46) | 69 of 743 (0.093) | 27 of 27 |
| results/predictor_with_perturbed_seen_task | progress | 16 of 46 (10 to 22) |  | +88 (42) | 68 of 743 (0.092) | 25 of 27 |
| results/predictor_with_perturbed_seen_task | safe | 16 of 46 (10 to 22) | +0 (-7 to +7) | +24 (45) | 60 of 743 (0.081) | 25 of 27 |
| results/predictor_with_perturbed_seen_task | logreg | 18 of 46 (12 to 24) | +2 (-6 to +10) | +24 (43) | 64 of 743 (0.086) | 18 of 27 |
| results/predictor_with_perturbed_seen_task | mlp | 10 of 46 (5 to 16) | -6 (-14 to +2) | +48 (38) | 37 of 743 (0.050) | 11 of 27 |
| results/predictor_with_perturbed_seen_task | combined | 23 of 46 (17 to 30) | +7 (-1 to +15) | -8 (43) | 227 of 743 (0.306) | 22 of 27 |
| results/predictor_with_perturbed_seen_task | mlp_reg | 10 of 46 (5 to 16) | -6 (-13 to +0) | +48 (41) | 60 of 743 (0.081) | 15 of 27 |
| results/predictor_with_perturbed_seen_task | combined_reg | 19 of 46 (13 to 26) | +3 (-4 to +10) | +16 (42) | 83 of 743 (0.112) | 22 of 27 |
| results/predictor_with_perturbed_seen_task | gated_mlp | 15 of 46 (9 to 21) | -1 (-3 to +0) | +76 (44) | 74 of 743 (0.100) | 26 of 27 |
| results/predictor_with_perturbed_seen_task | gated_combined | 16 of 46 (10 to 22) | +0 (+0 to +0) | +60 (44) | 68 of 743 (0.092) | 26 of 27 |
