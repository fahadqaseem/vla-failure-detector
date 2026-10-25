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
# Timely alarms with bootstrap 95% intervals, threshold fixed 0.10

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/D_seen | progress | 22 of 81 (14 to 30) | 50 / 9 |  | +124 (72) | 96 of 1071 (0.090) | 30 of 31 | 0.104 of 472 / 0.078 of 599 |
| results/week2/D_seen | gated_mlp | 23 of 81 (15 to 31) | 54 / 4 | +1 (-2 to +4) | +80 (77) | 108 of 1071 (0.101) | 30 of 31 | 0.089 of 472 / 0.110 of 599 |
| results/week2/D_seen | gated_combined | 25 of 81 (17 to 33) | 52 / 4 | +3 (+0 to +7) | +64 (77) | 114 of 1071 (0.106) | 31 of 31 | 0.089 of 472 / 0.120 of 599 |
| results/week2/D_seen | mlp_cusum | 30 of 81 (22 to 39) | 47 / 4 | +8 (-2 to +18) | +24 (77) | 176 of 1071 (0.164) | 18 of 31 | 0.097 of 472 / 0.217 of 599 |
| results/week2/D_seen | combined_cusum | 22 of 81 (14 to 30) | 55 / 4 | +0 (-9 to +9) | +40 (77) | 88 of 1071 (0.082) | 21 of 31 | 0.021 of 472 / 0.130 of 599 |
| results/week2/D_seen | mlp_rescue_cusum | 24 of 81 (16 to 32) | 53 / 4 | +2 (-7 to +11) | +40 (77) | 111 of 1071 (0.104) | 21 of 31 | 0.047 of 472 / 0.149 of 599 |
| results/week2/D_seen | gru_cusum | 18 of 81 (11 to 25) | 58 / 5 | -4 (-12 to +4) | +64 (76) | 88 of 1071 (0.082) | 22 of 31 | 0.030 of 472 / 0.124 of 599 |
