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
