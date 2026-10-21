# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_gated | timer | 4 of 11 (1 to 7) | -4 (-7 to -1) | +40 (11) | 47 of 472 (0.100) | 14 of 14 |
| results/predictor_gated | progress | 8 of 11 (5 to 11) |  | -144 (11) | 44 of 472 (0.093) | 13 of 14 |
| results/predictor_gated | safe | 1 of 11 (0 to 3) | -7 (-11 to -2) | +88 (5) | 54 of 472 (0.114) | 6 of 14 |
| results/predictor_gated | logreg | 1 of 11 (0 to 3) | -7 (-11 to -2) | +60 (4) | 50 of 472 (0.106) | 4 of 14 |
| results/predictor_gated | mlp | 2 of 11 (0 to 5) | -6 (-10 to -1) | -48 (3) | 52 of 472 (0.110) | 2 of 14 |
| results/predictor_gated | combined | 2 of 11 (0 to 5) | -6 (-10 to -1) | -120 (3) | 52 of 472 (0.110) | 3 of 14 |
| results/predictor_gated | mlp_reg | 2 of 11 (0 to 5) | -6 (-10 to -1) | -32 (3) | 50 of 472 (0.106) | 0 of 14 |
| results/predictor_gated | combined_reg | 1 of 11 (0 to 3) | -7 (-11 to -2) | +24 (4) | 52 of 472 (0.110) | 0 of 14 |
| results/predictor_gated | gated_mlp | 6 of 11 (3 to 9) | -2 (-5 to +0) | -48 (10) | 45 of 472 (0.095) | 10 of 14 |
| results/predictor_gated | gated_combined | 6 of 11 (3 to 9) | -2 (-5 to +0) | -52 (10) | 47 of 472 (0.100) | 13 of 14 |
| results/predictor_seen_task_gated | timer | 4 of 11 (1 to 7) | -4 (-7 to -1) | +64 (11) | 46 of 472 (0.097) | 14 of 14 |
| results/predictor_seen_task_gated | progress | 8 of 11 (5 to 11) |  | -144 (11) | 39 of 472 (0.083) | 13 of 14 |
| results/predictor_seen_task_gated | safe | 6 of 11 (3 to 9) | -2 (-6 to +2) | -12 (10) | 43 of 472 (0.091) | 13 of 14 |
| results/predictor_seen_task_gated | logreg | 4 of 11 (1 to 7) | -4 (-7 to -1) | +28 (10) | 42 of 472 (0.089) | 9 of 14 |
| results/predictor_seen_task_gated | mlp | 3 of 11 (0 to 6) | -5 (-8 to -2) | +48 (9) | 56 of 472 (0.119) | 9 of 14 |
| results/predictor_seen_task_gated | combined | 5 of 11 (2 to 8) | -3 (-6 to +0) | -92 (10) | 51 of 472 (0.108) | 9 of 14 |
| results/predictor_seen_task_gated | mlp_reg | 2 of 11 (0 to 5) | -6 (-9 to -3) | +16 (5) | 56 of 472 (0.119) | 7 of 14 |
| results/predictor_seen_task_gated | combined_reg | 4 of 11 (1 to 7) | -4 (-8 to +0) | -100 (6) | 64 of 472 (0.136) | 9 of 14 |
| results/predictor_seen_task_gated | gated_mlp | 7 of 11 (4 to 10) | -1 (-3 to +0) | -96 (11) | 42 of 472 (0.089) | 12 of 14 |
| results/predictor_seen_task_gated | gated_combined | 8 of 11 (5 to 11) | +0 (+0 to +0) | -112 (11) | 46 of 472 (0.097) | 13 of 14 |
