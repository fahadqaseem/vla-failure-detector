# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_gated | timer | 4 of 11 (1 to 7) | -2 (-5 to +0) | +72 (11) | 43 of 472 (0.091) | 14 of 14 |
| results/predictor_gated | progress | 6 of 11 (3 to 9) |  | -64 (10) | 23 of 472 (0.049) | 11 of 14 |
| results/predictor_gated | safe | 0 of 11 (0 to 0) | -6 (-9 to -3) | +104 (2) | 24 of 472 (0.051) | 2 of 14 |
| results/predictor_gated | logreg | 1 of 11 (0 to 3) | -5 (-9 to -1) | +32 (3) | 50 of 472 (0.106) | 1 of 14 |
| results/predictor_gated | mlp | 1 of 11 (0 to 3) | -5 (-9 to -1) | -36 (2) | 49 of 472 (0.104) | 0 of 14 |
| results/predictor_gated | combined | 2 of 11 (0 to 5) | -4 (-9 to +1) | -128 (2) | 50 of 472 (0.106) | 0 of 14 |
| results/predictor_gated | mlp_reg | 1 of 11 (0 to 3) | -5 (-9 to -1) | +112 (3) | 47 of 472 (0.100) | 0 of 14 |
| results/predictor_gated | combined_reg | 1 of 11 (0 to 3) | -5 (-9 to -1) | +80 (2) | 51 of 472 (0.108) | 0 of 14 |
| results/predictor_gated | gated_mlp | 4 of 11 (1 to 7) | -2 (-6 to +2) | +88 (10) | 27 of 472 (0.057) | 7 of 14 |
| results/predictor_gated | gated_combined | 4 of 11 (1 to 7) | -2 (-5 to +0) | +88 (9) | 29 of 472 (0.061) | 7 of 14 |
| results/predictor_seen_task_gated | timer | 4 of 11 (1 to 7) | -2 (-5 to +0) | +96 (11) | 21 of 472 (0.044) | 14 of 14 |
| results/predictor_seen_task_gated | progress | 6 of 11 (3 to 9) |  | -56 (10) | 22 of 472 (0.047) | 11 of 14 |
| results/predictor_seen_task_gated | safe | 5 of 11 (2 to 8) | -1 (-4 to +2) | +16 (10) | 20 of 472 (0.042) | 13 of 14 |
| results/predictor_seen_task_gated | logreg | 4 of 11 (1 to 7) | -2 (-6 to +2) | +16 (9) | 16 of 472 (0.034) | 9 of 14 |
| results/predictor_seen_task_gated | mlp | 2 of 11 (0 to 5) | -4 (-8 to +0) | +48 (7) | 23 of 472 (0.049) | 5 of 14 |
| results/predictor_seen_task_gated | combined | 3 of 11 (0 to 6) | -3 (-7 to +1) | +24 (7) | 22 of 472 (0.047) | 9 of 14 |
| results/predictor_seen_task_gated | mlp_reg | 2 of 11 (0 to 5) | -4 (-8 to +0) | +16 (5) | 36 of 472 (0.076) | 7 of 14 |
| results/predictor_seen_task_gated | combined_reg | 2 of 11 (0 to 5) | -4 (-8 to +0) | +16 (5) | 42 of 472 (0.089) | 8 of 14 |
| results/predictor_seen_task_gated | gated_mlp | 5 of 11 (2 to 8) | -1 (-4 to +2) | -36 (10) | 22 of 472 (0.047) | 9 of 14 |
| results/predictor_seen_task_gated | gated_combined | 5 of 11 (2 to 8) | -1 (-4 to +2) | +88 (11) | 25 of 472 (0.053) | 10 of 14 |
