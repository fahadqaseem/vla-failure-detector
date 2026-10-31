# gru_phys_frac and gru_phys_ttp vs progress, unseen tasks

Paired bootstrap intervals vs progress for the regression models (Fahad, Oct 31), unseen tasks. Same method as 13_report.py: read from its report rows (10000 draws over timed failures, same draws for both models), so nothing is recomputed. An interval that holds 0 is no evidence of a difference.

| failure threshold | target | model | timely (95%) | vs progress (95%) | false alarms on successes | unnecessary alarms |
|---|---|---|---|---|---|---|
| 70% | 5% | progress | 22 of 91 (14 to 30) | reference | 51 of 1071 (0.048) | 31 of 35 |
| 70% | 5% | gru_phys_frac | 21 of 91 (13 to 29) | -1 (-9 to +7) | 18 of 1071 (0.017) | 8 of 35 |
| 70% | 5% | gru_phys_ttp | 22 of 91 (14 to 30) | +0 (-8 to +8) | 19 of 1071 (0.018) | 7 of 35 |
| 70% | 2.5% | progress | 13 of 91 (7 to 20) | reference | 27 of 1071 (0.025) | 25 of 35 |
| 70% | 2.5% | gru_phys_frac | 18 of 91 (11 to 26) | +5 (-3 to +14) | 10 of 1071 (0.009) | 4 of 35 |
| 70% | 2.5% | gru_phys_ttp | 16 of 91 (9 to 23) | +3 (-5 to +12) | 8 of 1071 (0.007) | 4 of 35 |
| 80% | 5% | progress | 29 of 102 (20 to 38) | reference | 51 of 1071 (0.048) | 35 of 39 |
| 80% | 5% | gru_phys_frac | 27 of 102 (18 to 36) | -2 (-12 to +8) | 33 of 1071 (0.031) | 12 of 39 |
| 80% | 5% | gru_phys_ttp | 24 of 102 (16 to 33) | -5 (-15 to +5) | 27 of 1071 (0.025) | 8 of 39 |
| 80% | 2.5% | progress | 17 of 102 (10 to 24) | reference | 27 of 1071 (0.025) | 28 of 39 |
| 80% | 2.5% | gru_phys_frac | 23 of 102 (15 to 32) | +6 (-3 to +16) | 16 of 1071 (0.015) | 8 of 39 |
| 80% | 2.5% | gru_phys_ttp | 20 of 102 (12 to 28) | +3 (-7 to +13) | 13 of 1071 (0.012) | 7 of 39 |
