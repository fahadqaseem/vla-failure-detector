# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures |
|---|---|---|---|---|---|---|---|
| results/lead_experiments/lead0_mlp | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead0_mlp | mlp | 5 of 46 (1 to 9) | 11 / 30 | -6 (-13 to +1) | +76 (16) | 99 of 743 (0.133) | 7 of 27 |
| results/lead_experiments/lead0_mlp | mlp_cusum | 6 of 46 (2 to 11) | 25 / 15 | -5 (-11 to +1) | +104 (31) | 22 of 743 (0.030) | 12 of 27 |
| results/lead_experiments/lead32_mlp | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead32_mlp | mlp | 3 of 46 (0 to 7) | 12 / 31 | -8 (-14 to -2) | +128 (15) | 68 of 743 (0.092) | 5 of 27 |
| results/lead_experiments/lead32_mlp | mlp_cusum | 6 of 46 (2 to 11) | 28 / 12 | -5 (-11 to +1) | +96 (34) | 26 of 743 (0.035) | 11 of 27 |
| results/lead_experiments/lead64_mlp | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead64_mlp | mlp | 4 of 46 (1 to 8) | 8 / 34 | -7 (-14 to +0) | +52 (12) | 104 of 743 (0.140) | 3 of 27 |
| results/lead_experiments/lead64_mlp | mlp_cusum | 7 of 46 (3 to 12) | 26 / 13 | -4 (-11 to +3) | +88 (33) | 37 of 743 (0.050) | 9 of 27 |
| results/lead_experiments/lead0_combined | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead0_combined | combined | 6 of 46 (2 to 11) | 17 / 23 | -5 (-12 to +2) | +80 (23) | 86 of 743 (0.116) | 4 of 27 |
| results/lead_experiments/lead0_combined | combined_cusum | 8 of 46 (3 to 13) | 24 / 14 | -3 (-9 to +3) | +124 (32) | 27 of 743 (0.036) | 4 of 27 |
| results/lead_experiments/lead32_combined | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead32_combined | combined | 3 of 46 (0 to 7) | 12 / 31 | -8 (-14 to -2) | +112 (15) | 106 of 743 (0.143) | 2 of 27 |
| results/lead_experiments/lead32_combined | combined_cusum | 7 of 46 (3 to 12) | 28 / 11 | -4 (-9 to +1) | +80 (35) | 111 of 743 (0.149) | 7 of 27 |
| results/lead_experiments/lead64_combined | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 |
| results/lead_experiments/lead64_combined | combined | 5 of 46 (1 to 10) | 8 / 33 | -6 (-13 to +1) | +32 (13) | 106 of 743 (0.143) | 2 of 27 |
| results/lead_experiments/lead64_combined | combined_cusum | 10 of 46 (5 to 16) | 29 / 7 | -1 (-7 to +5) | +80 (39) | 28 of 743 (0.038) | 15 of 27 |
