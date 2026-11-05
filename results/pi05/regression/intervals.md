# gru_phys_frac and gru_phys_ttp vs progress, unseen tasks

Paired bootstrap intervals vs progress for the regression models (Fahad, Oct 31), unseen tasks. Same method as 13_report.py: read from its report rows (10000 draws over timed failures, same draws for both models), so nothing is recomputed. An interval that holds 0 is no evidence of a difference.

| failure threshold | target | model | timely (95%) | vs progress (95%) | false alarms on successes | unnecessary alarms |
|---|---|---|---|---|---|---|
| 50% | 5% | progress | 5 of 27 (1 to 9) | reference | 46 of 928 (0.050) | 6 of 7 |
| 50% | 5% | gru_phys_frac | 8 of 27 (4 to 13) | +3 (+0 to +6) | 5 of 928 (0.005) | 0 of 7 |
| 50% | 5% | gru_phys_ttp | 9 of 27 (4 to 14) | +4 (+1 to +8) | 8 of 928 (0.009) | 1 of 7 |
| 50% | 2.5% | progress | 2 of 27 (0 to 5) | reference | 23 of 928 (0.025) | 6 of 7 |
| 50% | 2.5% | gru_phys_frac | 6 of 27 (2 to 10) | +4 (+0 to +9) | 3 of 928 (0.003) | 0 of 7 |
| 50% | 2.5% | gru_phys_ttp | 8 of 27 (4 to 13) | +6 (+1 to +11) | 5 of 928 (0.005) | 1 of 7 |
| 70% | 5% | progress | 8 of 31 (4 to 13) | reference | 46 of 928 (0.050) | 6 of 7 |
| 70% | 5% | gru_phys_frac | 7 of 31 (3 to 12) | -1 (-7 to +5) | 11 of 928 (0.012) | 0 of 7 |
| 70% | 5% | gru_phys_ttp | 10 of 31 (5 to 15) | +2 (-3 to +8) | 13 of 928 (0.014) | 0 of 7 |
| 70% | 2.5% | progress | 6 of 31 (2 to 11) | reference | 23 of 928 (0.025) | 6 of 7 |
| 70% | 2.5% | gru_phys_frac | 6 of 31 (2 to 11) | +0 (-5 to +6) | 5 of 928 (0.005) | 0 of 7 |
| 70% | 2.5% | gru_phys_ttp | 9 of 31 (4 to 14) | +3 (-3 to +9) | 7 of 928 (0.008) | 0 of 7 |
| 80% | 5% | progress | 17 of 33 (11 to 22) | reference | 46 of 928 (0.050) | 7 of 8 |
| 80% | 5% | gru_phys_frac | 5 of 33 (1 to 9) | -12 (-18 to -6) | 3 of 928 (0.003) | 0 of 8 |
| 80% | 5% | gru_phys_ttp | 7 of 33 (3 to 12) | -10 (-16 to -3) | 5 of 928 (0.005) | 1 of 8 |
| 80% | 2.5% | progress | 12 of 33 (7 to 17) | reference | 23 of 928 (0.025) | 7 of 8 |
| 80% | 2.5% | gru_phys_frac | 4 of 33 (1 to 8) | -8 (-13 to -4) | 1 of 928 (0.001) | 0 of 8 |
| 80% | 2.5% | gru_phys_ttp | 6 of 33 (2 to 11) | -6 (-12 to +0) | 2 of 928 (0.002) | 1 of 8 |

## Unnecessary alarms and false alarms vs progress

Same bootstrap (10000 draws, seed 0, same draws for both models), over recoverable failures and over successes of the held-out tasks. Difference = model minus progress in counts of alarmed runs; negative = fewer alarms than progress. Scores from data/pi05_reg.

| failure threshold | target | model | unnecessary alarms | vs progress (95%) | false alarms | vs progress (95%) |
|---|---|---|---|---|---|---|
| 50% | 5% | gru_phys_frac | 0 vs 6 of 7 | -6 (-7 to -4) | 5 vs 46 of 928 | -41 (-55 to -28) |
| 50% | 5% | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 8 vs 46 of 928 | -38 (-52 to -25) |
| 50% | 2.5% | gru_phys_frac | 0 vs 6 of 7 | -6 (-7 to -4) | 3 vs 23 of 928 | -20 (-30 to -10) |
| 50% | 2.5% | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 5 vs 23 of 928 | -18 (-28 to -8) |
| 70% | 5% | gru_phys_frac | 0 vs 6 of 7 | -6 (-7 to -4) | 11 vs 46 of 928 | -35 (-49 to -21) |
| 70% | 5% | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 13 vs 46 of 928 | -33 (-47 to -19) |
| 70% | 2.5% | gru_phys_frac | 0 vs 6 of 7 | -6 (-7 to -4) | 5 vs 23 of 928 | -18 (-29 to -8) |
| 70% | 2.5% | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 7 vs 23 of 928 | -16 (-26 to -6) |
| 80% | 5% | gru_phys_frac | 0 vs 7 of 8 | -7 (-8 to -5) | 3 vs 46 of 928 | -43 (-57 to -30) |
| 80% | 5% | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 5 vs 46 of 928 | -41 (-55 to -28) |
| 80% | 2.5% | gru_phys_frac | 0 vs 7 of 8 | -7 (-8 to -5) | 1 vs 23 of 928 | -22 (-32 to -13) |
| 80% | 2.5% | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 2 vs 23 of 928 | -21 (-31 to -12) |
