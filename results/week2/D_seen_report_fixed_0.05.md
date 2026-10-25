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
| results/week2/D_seen | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| results/week2/D_seen | gated_mlp | 18 of 81 (11 to 25) | 54 / 9 | +2 (-4 to +8) | +88 (72) | 49 of 1071 (0.046) | 26 of 31 | 0.030 of 472 / 0.058 of 599 |
| results/week2/D_seen | gated_combined | 17 of 81 (10 to 24) | 57 / 7 | +1 (-5 to +7) | +88 (74) | 54 of 1071 (0.050) | 26 of 31 | 0.038 of 472 / 0.060 of 599 |
| results/week2/D_seen | mlp_cusum | 22 of 81 (14 to 30) | 54 / 5 | +6 (-4 to +16) | +44 (76) | 103 of 1071 (0.096) | 17 of 31 | 0.049 of 472 / 0.134 of 599 |
| results/week2/D_seen | combined_cusum | 13 of 81 (7 to 20) | 62 / 6 | -3 (-11 to +5) | +64 (75) | 45 of 1071 (0.042) | 15 of 31 | 0.017 of 472 / 0.062 of 599 |
| results/week2/D_seen | mlp_rescue_cusum | 15 of 81 (8 to 22) | 60 / 6 | -1 (-11 to +9) | +56 (75) | 54 of 1071 (0.050) | 18 of 31 | 0.023 of 472 / 0.072 of 599 |
| results/week2/D_seen | gru_cusum | 10 of 81 (5 to 16) | 64 / 7 | -6 (-14 to +2) | +92 (74) | 47 of 1071 (0.044) | 17 of 31 | 0.015 of 472 / 0.067 of 599 |
