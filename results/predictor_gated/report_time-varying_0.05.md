# Timely alarms with bootstrap 95% intervals, threshold time-varying 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|
| results/predictor_gated | timer | 4 of 11 (1 to 7) | -2 (-6 to +2) | +72 (11) | 43 of 472 (0.091) | 14 of 14 |
| results/predictor_gated | progress | 6 of 11 (3 to 9) |  | -136 (9) | 47 of 472 (0.100) | 6 of 14 |
| results/predictor_gated | safe | 2 of 11 (0 to 5) | -4 (-7 to -1) | +84 (8) | 13 of 472 (0.028) | 2 of 14 |
| results/predictor_gated | logreg | 1 of 11 (0 to 3) | -5 (-9 to -1) | +80 (5) | 58 of 472 (0.123) | 1 of 14 |
| results/predictor_gated | mlp | 4 of 11 (1 to 7) | -2 (-6 to +2) | +20 (10) | 54 of 472 (0.114) | 6 of 14 |
| results/predictor_gated | combined | 5 of 11 (2 to 8) | -1 (-4 to +2) | +16 (11) | 56 of 472 (0.119) | 6 of 14 |
| results/predictor_gated | mlp_reg | 4 of 11 (1 to 7) | -2 (-6 to +2) | -72 (8) | 51 of 472 (0.108) | 4 of 14 |
| results/predictor_gated | combined_reg | 5 of 11 (2 to 8) | -1 (-4 to +2) | -160 (7) | 56 of 472 (0.119) | 4 of 14 |
| results/predictor_gated | gated_mlp | 5 of 11 (2 to 8) | -1 (-3 to +0) | +28 (10) | 16 of 472 (0.034) | 7 of 14 |
| results/predictor_gated | gated_combined | 4 of 11 (1 to 7) | -2 (-5 to +0) | +88 (9) | 18 of 472 (0.038) | 7 of 14 |
| results/predictor_seen_task_gated | timer | 4 of 11 (1 to 7) | -2 (-6 to +2) | +104 (11) | 16 of 472 (0.034) | 14 of 14 |
| results/predictor_seen_task_gated | progress | 6 of 11 (3 to 9) |  | -40 (9) | 26 of 472 (0.055) | 7 of 14 |
| results/predictor_seen_task_gated | safe | 1 of 11 (0 to 3) | -5 (-8 to -2) | -488 (1) | 20 of 472 (0.042) | 6 of 14 |
| results/predictor_seen_task_gated | logreg | 2 of 11 (0 to 5) | -4 (-8 to +0) | +32 (5) | 21 of 472 (0.044) | 5 of 14 |
| results/predictor_seen_task_gated | mlp | 2 of 11 (0 to 5) | -4 (-8 to +0) | +60 (8) | 27 of 472 (0.057) | 8 of 14 |
| results/predictor_seen_task_gated | combined | 3 of 11 (0 to 6) | -3 (-7 to +1) | +48 (8) | 27 of 472 (0.057) | 6 of 14 |
| results/predictor_seen_task_gated | mlp_reg | 2 of 11 (0 to 5) | -4 (-7 to -1) | +48 (6) | 41 of 472 (0.087) | 6 of 14 |
| results/predictor_seen_task_gated | combined_reg | 2 of 11 (0 to 5) | -4 (-7 to -1) | +56 (6) | 36 of 472 (0.076) | 8 of 14 |
| results/predictor_seen_task_gated | gated_mlp | 7 of 11 (4 to 10) | +1 (+0 to +3) | -88 (10) | 26 of 472 (0.055) | 9 of 14 |
| results/predictor_seen_task_gated | gated_combined | 6 of 11 (3 to 9) | +0 (-3 to +3) | +0 (11) | 24 of 472 (0.051) | 10 of 14 |
