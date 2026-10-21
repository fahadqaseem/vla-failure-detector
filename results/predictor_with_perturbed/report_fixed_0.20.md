# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_with_perturbed | timer | 15 of 46 (9 to 21) | -2 (-8 to +4) | +104 (46) | 140 of 743 (0.188) | 27 of 27 |
| results/predictor_with_perturbed | progress | 17 of 46 (11 to 24) |  | +40 (44) | 116 of 743 (0.156) | 26 of 27 |
| results/predictor_with_perturbed | safe | 11 of 46 (6 to 17) | -6 (-14 to +2) | +64 (42) | 142 of 743 (0.191) | 14 of 27 |
| results/predictor_with_perturbed | logreg | 13 of 46 (7 to 19) | -4 (-12 to +4) | +56 (45) | 152 of 743 (0.205) | 16 of 27 |
| results/predictor_with_perturbed | mlp | 11 of 46 (6 to 17) | -6 (-14 to +2) | +64 (42) | 144 of 743 (0.194) | 15 of 27 |
| results/predictor_with_perturbed | combined | 14 of 46 (8 to 20) | -3 (-10 to +4) | +56 (41) | 159 of 743 (0.214) | 14 of 27 |
| results/predictor_with_perturbed | mlp_reg | 18 of 46 (12 to 25) | +1 (-7 to +9) | +28 (40) | 142 of 743 (0.191) | 9 of 27 |
| results/predictor_with_perturbed | combined_reg | 18 of 46 (12 to 25) | +1 (-6 to +9) | +40 (41) | 143 of 743 (0.192) | 12 of 27 |
| results/predictor_with_perturbed | gated_mlp | 17 of 46 (11 to 24) | +0 (+0 to +0) | +40 (44) | 116 of 743 (0.156) | 26 of 27 |
| results/predictor_with_perturbed | gated_combined | 17 of 46 (11 to 24) | +0 (+0 to +0) | +40 (44) | 116 of 743 (0.156) | 26 of 27 |
| results/predictor_with_perturbed_seen_task | timer | 13 of 46 (7 to 19) | -3 (-8 to +2) | +96 (46) | 145 of 743 (0.195) | 27 of 27 |
| results/predictor_with_perturbed_seen_task | progress | 16 of 46 (10 to 22) |  | +60 (44) | 98 of 743 (0.132) | 26 of 27 |
| results/predictor_with_perturbed_seen_task | safe | 27 of 46 (20 to 34) | +11 (+3 to +19) | -40 (45) | 132 of 743 (0.178) | 25 of 27 |
| results/predictor_with_perturbed_seen_task | logreg | 22 of 46 (16 to 29) | +6 (-2 to +14) | +0 (44) | 146 of 743 (0.197) | 19 of 27 |
| results/predictor_with_perturbed_seen_task | mlp | 17 of 46 (11 to 23) | +1 (-7 to +9) | +16 (40) | 95 of 743 (0.128) | 16 of 27 |
| results/predictor_with_perturbed_seen_task | combined | 33 of 46 (27 to 39) | +17 (+9 to +25) | -92 (44) | 348 of 743 (0.468) | 24 of 27 |
| results/predictor_with_perturbed_seen_task | mlp_reg | 14 of 46 (8 to 20) | -2 (-9 to +5) | +24 (41) | 135 of 743 (0.182) | 20 of 27 |
| results/predictor_with_perturbed_seen_task | combined_reg | 24 of 46 (17 to 31) | +8 (+0 to +15) | -8 (42) | 163 of 743 (0.219) | 25 of 27 |
| results/predictor_with_perturbed_seen_task | gated_mlp | 16 of 46 (10 to 22) | +0 (+0 to +0) | +60 (44) | 98 of 743 (0.132) | 26 of 27 |
| results/predictor_with_perturbed_seen_task | gated_combined | 16 of 46 (10 to 22) | +0 (+0 to +0) | +60 (44) | 98 of 743 (0.132) | 26 of 27 |
