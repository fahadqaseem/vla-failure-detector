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
# Timely alarms with bootstrap 95% intervals, threshold fixed 0.20

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/D_seen | progress | 26 of 81 (18 to 34) | 51 / 4 |  | +64 (77) | 190 of 1071 (0.177) | 31 of 31 | 0.201 of 472 / 0.159 of 599 |
| results/week2/D_seen | gated_mlp | 26 of 81 (18 to 34) | 51 / 4 | +0 (+0 to +0) | +64 (77) | 190 of 1071 (0.177) | 31 of 31 | 0.201 of 472 / 0.159 of 599 |
| results/week2/D_seen | gated_combined | 26 of 81 (18 to 34) | 51 / 4 | +0 (+0 to +0) | +64 (77) | 190 of 1071 (0.177) | 31 of 31 | 0.201 of 472 / 0.159 of 599 |
| results/week2/D_seen | mlp_cusum | 38 of 81 (29 to 47) | 39 / 4 | +12 (+2 to +22) | +8 (77) | 306 of 1071 (0.286) | 22 of 31 | 0.157 of 472 / 0.387 of 599 |
| results/week2/D_seen | combined_cusum | 35 of 81 (26 to 44) | 43 / 3 | +9 (-1 to +18) | +16 (78) | 207 of 1071 (0.193) | 25 of 31 | 0.083 of 472 / 0.280 of 599 |
| results/week2/D_seen | mlp_rescue_cusum | 31 of 81 (23 to 39) | 47 / 3 | +5 (-4 to +15) | +16 (78) | 220 of 1071 (0.205) | 24 of 31 | 0.108 of 472 / 0.282 of 599 |
| results/week2/D_seen | gru_cusum | 25 of 81 (17 to 33) | 51 / 5 | -1 (-10 to +8) | +40 (76) | 197 of 1071 (0.184) | 27 of 31 | 0.100 of 472 / 0.250 of 599 |
