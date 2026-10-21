# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_gated | timer | 7 of 11 (4 to 10) | -2 (-6 to +2) | -24 (11) | 92 of 472 (0.195) | 14 of 14 |
| results/predictor_gated | progress | 9 of 11 (6 to 11) |  | -160 (11) | 87 of 472 (0.184) | 13 of 14 |
| results/predictor_gated | safe | 2 of 11 (0 to 5) | -7 (-11 to -2) | +32 (7) | 93 of 472 (0.197) | 6 of 14 |
| results/predictor_gated | logreg | 2 of 11 (0 to 5) | -7 (-11 to -2) | +48 (7) | 88 of 472 (0.186) | 6 of 14 |
| results/predictor_gated | mlp | 4 of 11 (1 to 7) | -5 (-9 to -1) | +8 (9) | 90 of 472 (0.191) | 6 of 14 |
| results/predictor_gated | combined | 5 of 11 (2 to 8) | -4 (-8 to +0) | +16 (11) | 86 of 472 (0.182) | 8 of 14 |
| results/predictor_gated | mlp_reg | 6 of 11 (3 to 9) | -3 (-7 to +1) | -88 (9) | 78 of 472 (0.165) | 4 of 14 |
| results/predictor_gated | combined_reg | 5 of 11 (2 to 8) | -4 (-8 to +0) | +16 (11) | 94 of 472 (0.199) | 8 of 14 |
| results/predictor_gated | gated_mlp | 9 of 11 (6 to 11) | +0 (+0 to +0) | -160 (11) | 87 of 472 (0.184) | 13 of 14 |
| results/predictor_gated | gated_combined | 9 of 11 (6 to 11) | +0 (+0 to +0) | -160 (11) | 87 of 472 (0.184) | 13 of 14 |
| results/predictor_seen_task_gated | timer | 6 of 11 (3 to 9) | -2 (-5 to +0) | -16 (11) | 86 of 472 (0.182) | 14 of 14 |
| results/predictor_seen_task_gated | progress | 8 of 11 (5 to 11) |  | -160 (11) | 69 of 472 (0.146) | 13 of 14 |
| results/predictor_seen_task_gated | safe | 6 of 11 (3 to 9) | -2 (-6 to +2) | -176 (10) | 80 of 472 (0.169) | 13 of 14 |
| results/predictor_seen_task_gated | logreg | 5 of 11 (2 to 8) | -3 (-6 to +0) | -36 (10) | 100 of 472 (0.212) | 9 of 14 |
| results/predictor_seen_task_gated | mlp | 6 of 11 (3 to 9) | -2 (-6 to +2) | -148 (10) | 110 of 472 (0.233) | 9 of 14 |
| results/predictor_seen_task_gated | combined | 6 of 11 (3 to 9) | -2 (-6 to +2) | -140 (10) | 105 of 472 (0.222) | 10 of 14 |
| results/predictor_seen_task_gated | mlp_reg | 3 of 11 (0 to 6) | -5 (-9 to -1) | +8 (7) | 85 of 472 (0.180) | 8 of 14 |
| results/predictor_seen_task_gated | combined_reg | 4 of 11 (1 to 7) | -4 (-8 to +0) | +8 (9) | 113 of 472 (0.239) | 10 of 14 |
| results/predictor_seen_task_gated | gated_mlp | 8 of 11 (5 to 11) | +0 (+0 to +0) | -160 (11) | 69 of 472 (0.146) | 13 of 14 |
| results/predictor_seen_task_gated | gated_combined | 8 of 11 (5 to 11) | +0 (+0 to +0) | -160 (11) | 69 of 472 (0.146) | 13 of 14 |
