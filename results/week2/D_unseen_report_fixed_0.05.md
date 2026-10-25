# Week 2 completeness (Phase A and B)

Slurm jobs (array tasks, including resubmits): w2-collect: 7 completed, 0 other; w2-lookahead: 26 completed, 0 other; w2-precheck: 7 completed, 0 other; w2-refine: 79 completed, 0 other; w2-scan: 63 completed, 0 other

| task | episodes (of 100) | failures | replay gate | pre-checks (of failures) | scan / recoverable |
|---|---|---|---|---|---|
| 0 | 94 | 33 | pass | 33 of 33 | 31 / 2 |
| 1 | 100 | 13 | pass | 13 of 13 | 12 / 1 |
| 4 | 100 | 11 | pass | 11 of 11 | 11 / 0 |
| 5 | 100 | 4 | FAIL: query 1 of data/perturbed_v2/task05/t05_e00_p0_s1.npz | 0 of 4 | 0 / 0 |
| 6 | 94 | 26 | FAIL: query 1 of data/perturbed_v2/task06/t06_e00_p0_s1.npz | 0 of 26 | 0 / 0 |
| 7 | 100 | 9 | pass | 9 of 9 | 9 / 0 |
| 8 | 100 | 26 | FAIL: query -1 of data/perturbed_v2/task08/t08_e00_p0_s1.npz | 0 of 26 | 0 / 0 |

Tasks dropped (gate failed or not run): [5, 6, 8]. Tasks with fewer than 100 episodes: [0, 6] (an initial state is skipped after 20 invalid perturbed starts).
Failures without a pre-check (gate passed): none
Full scans (new failures): 63 of 63 done; missing: none
K 16 refinement: 79 of 79 done; missing: none
Look-ahead (Phase B): 251 of 251 done; missing: none
Failures that are missing a scan or pre-check have no label and are left out of every Phase D number.
# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/D_unseen | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| results/week2/D_unseen | gated_mlp | 17 of 81 (10 to 24) | 57 / 7 | +0 (-5 to +5) | +112 (74) | 65 of 1071 (0.061) | 27 of 31 | 0.040 of 472 / 0.077 of 599 |
| results/week2/D_unseen | gated_combined | 17 of 81 (10 to 24) | 57 / 7 | +0 (-5 to +5) | +112 (74) | 60 of 1071 (0.056) | 23 of 31 | 0.049 of 472 / 0.062 of 599 |
| results/week2/D_unseen | mlp_cusum | 10 of 81 (5 to 16) | 43 / 28 | -7 (-14 to +0) | +96 (53) | 45 of 1071 (0.042) | 10 of 31 | 0.025 of 472 / 0.055 of 599 |
| results/week2/D_unseen | combined_cusum | 11 of 81 (5 to 17) | 46 / 24 | -6 (-13 to +1) | +112 (57) | 36 of 1071 (0.034) | 13 of 31 | 0.028 of 472 / 0.038 of 599 |
| results/week2/D_unseen | mlp_rescue_cusum | 11 of 81 (5 to 17) | 42 / 28 | -6 (-14 to +2) | +128 (53) | 61 of 1071 (0.057) | 12 of 31 | 0.028 of 472 / 0.080 of 599 |
| results/week2/D_unseen | gru_cusum | 16 of 81 (9 to 23) | 45 / 20 | -1 (-7 to +6) | +72 (61) | 163 of 1071 (0.152) | 13 of 31 | 0.114 of 472 / 0.182 of 599 |
| results/week2/B_lookahead | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 4 of 150 (0.027) | 23 of 27 | 0.030 of 100 / 0.020 of 50 |
| results/week2/B_lookahead | lookahead_nomove | 0 of 46 (0 to 0) | 0 / 46 | -11 (-17 to -6) | none | 0 of 150 (0.000) | 0 of 27 | 0.000 of 100 / 0.000 of 50 |
| results/week2/B_lookahead | lookahead_mlp | 3 of 46 (0 to 7) | 1 / 42 | -8 (-15 to -1) | -104 (4) | 17 of 150 (0.113) | 2 of 27 | 0.100 of 100 / 0.140 of 50 |
| results/week2/B_lookahead | lookahead_nosucc | 0 of 46 (0 to 0) | 0 / 46 | -11 (-17 to -6) | none | 0 of 150 (0.000) | 0 of 27 | 0.000 of 100 / 0.000 of 50 |
