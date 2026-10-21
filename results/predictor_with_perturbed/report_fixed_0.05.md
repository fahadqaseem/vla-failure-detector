# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_with_perturbed | timer | 9 of 46 (4 to 15) | -2 (-7 to +3) | +216 (46) | 84 of 743 (0.113) | 27 of 27 |
| results/predictor_with_perturbed | progress | 11 of 46 (6 to 17) |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/predictor_with_perturbed | safe | 7 of 46 (3 to 12) | -4 (-11 to +3) | +124 (28) | 71 of 743 (0.096) | 11 of 27 |
| results/predictor_with_perturbed | logreg | 4 of 46 (1 to 8) | -7 (-14 to +0) | +140 (28) | 98 of 743 (0.132) | 9 of 27 |
| results/predictor_with_perturbed | mlp | 5 of 46 (1 to 9) | -6 (-13 to +1) | +76 (16) | 99 of 743 (0.133) | 7 of 27 |
| results/predictor_with_perturbed | combined | 6 of 46 (2 to 11) | -5 (-12 to +2) | +80 (23) | 86 of 743 (0.116) | 4 of 27 |
| results/predictor_with_perturbed | mlp_reg | 5 of 46 (1 to 9) | -6 (-13 to +1) | +104 (15) | 60 of 743 (0.081) | 2 of 27 |
| results/predictor_with_perturbed | combined_reg | 5 of 46 (1 to 9) | -6 (-13 to +1) | +88 (21) | 87 of 743 (0.117) | 6 of 27 |
| results/predictor_with_perturbed | gated_mlp | 13 of 46 (7 to 19) | +2 (-2 to +6) | +88 (42) | 36 of 743 (0.048) | 21 of 27 |
| results/predictor_with_perturbed | gated_combined | 12 of 46 (6 to 18) | +1 (-4 to +6) | +104 (41) | 28 of 743 (0.038) | 21 of 27 |
| results/predictor_with_perturbed_seen_task | timer | 8 of 46 (3 to 13) | -3 (-8 to +2) | +216 (46) | 31 of 743 (0.042) | 27 of 27 |
| results/predictor_with_perturbed_seen_task | progress | 11 of 46 (6 to 17) |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 |
| results/predictor_with_perturbed_seen_task | safe | 13 of 46 (7 to 19) | +2 (-5 to +9) | +48 (44) | 33 of 743 (0.044) | 24 of 27 |
| results/predictor_with_perturbed_seen_task | logreg | 13 of 46 (7 to 19) | +2 (-5 to +9) | +56 (43) | 35 of 743 (0.047) | 15 of 27 |
| results/predictor_with_perturbed_seen_task | mlp | 4 of 46 (1 to 8) | -7 (-13 to -1) | +84 (38) | 19 of 743 (0.026) | 7 of 27 |
| results/predictor_with_perturbed_seen_task | combined | 19 of 46 (13 to 26) | +8 (-1 to +16) | +16 (42) | 152 of 743 (0.205) | 18 of 27 |
| results/predictor_with_perturbed_seen_task | mlp_reg | 6 of 46 (2 to 11) | -5 (-11 to +1) | +64 (38) | 29 of 743 (0.039) | 12 of 27 |
| results/predictor_with_perturbed_seen_task | combined_reg | 11 of 46 (6 to 17) | +0 (-7 to +7) | +48 (42) | 42 of 743 (0.057) | 19 of 27 |
| results/predictor_with_perturbed_seen_task | gated_mlp | 11 of 46 (6 to 17) | +0 (-4 to +4) | +88 (41) | 35 of 743 (0.047) | 23 of 27 |
| results/predictor_with_perturbed_seen_task | gated_combined | 14 of 46 (8 to 20) | +3 (-1 to +7) | +76 (42) | 48 of 743 (0.065) | 22 of 27 |
