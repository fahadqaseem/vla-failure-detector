# Track 1 seen-task models at or under 5% false alarms: bootstrap 95% intervals (fixed 5%)

Seen-task split (5 folds by initial-state index within each task), natural + perturbed (7 of 10 tasks), pooled. Rows taken from `13_report.py --pred results/week2/T1_seen_conv results/week2/T1_seen_gru --key 'fixed 0.05'` (10000 bootstrap draws over the 46 failures with t_pnr > 0, seed 0; vs progress = paired, same draws per run).

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_seen_conv | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/T1_seen_conv | conv_phys | 14 of 46 (8 to 20) | 25 / 7 | +3 (-3 to +9) | +40 (39) | 36 of 743 (0.048) | 6 of 27 | 0.025 of 472 / 0.089 of 271 |
| results/week2/T1_seen_conv | conv_physvla | 17 of 46 (11 to 23) | 25 / 4 | +6 (-1 to +13) | +32 (42) | 34 of 743 (0.046) | 12 of 27 | 0.019 of 472 / 0.092 of 271 |
| results/week2/T1_seen_conv | conv_physall | 17 of 46 (11 to 24) | 27 / 2 | +6 (-1 to +14) | +36 (44) | 33 of 743 (0.044) | 16 of 27 | 0.017 of 472 / 0.092 of 271 |
| results/week2/T1_seen_gru | gru_phys | 13 of 46 (7 to 19) | 25 / 8 | +2 (-5 to +9) | +48 (38) | 26 of 743 (0.035) | 9 of 27 | 0.019 of 472 / 0.063 of 271 |
| results/week2/T1_seen_gru | gru_physvla | 14 of 46 (8 to 20) | 28 / 4 | +3 (-3 to +9) | +56 (42) | 28 of 743 (0.038) | 7 of 27 | 0.017 of 472 / 0.074 of 271 |
