# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr50/unseen | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| data/pi05_reg/thr50/unseen | gru_phys | 0.015 | -72 (8) | 3 of 27 (0 to 6) | 0.009 | -128 (8) | 3 of 27 (0 to 6) |
| data/pi05_reg/thr50/unseen | gru_phys_frac | 0.005 | +104 (11) | 8 of 27 (4 to 13) | 0.003 | +96 (9) | 6 of 27 (2 to 10) |
| data/pi05_reg/thr50/unseen | gru_phys_ttp | 0.009 | +96 (15) | 9 of 27 (4 to 14) | 0.005 | +64 (15) | 8 of 27 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr50/unseen | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| data/pi05_reg/thr50/unseen | gru_phys | 3 of 27 (0 to 6) | 5 / 19 | -2 (-7 to +3) | +72 (8) | 14 of 928 (0.015) | 1 of 7 | 0.006 of 475 / 0.024 of 453 |
| data/pi05_reg/thr50/unseen | gru_phys_frac | 8 of 27 (4 to 13) | 3 / 16 | +3 (+0 to +6) | -104 (11) | 5 of 928 (0.005) | 0 of 7 | 0.002 of 475 / 0.009 of 453 |
| data/pi05_reg/thr50/unseen | gru_phys_ttp | 9 of 27 (4 to 14) | 6 / 12 | +4 (+1 to +8) | -96 (15) | 8 of 928 (0.009) | 1 of 7 | 0.006 of 475 / 0.011 of 453 |
