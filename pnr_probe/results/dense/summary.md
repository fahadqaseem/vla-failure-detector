# Dense replay features: summary

**WARNING: timed failures pass the replay check much less often than successes (54/81 = 66.7% vs 1022/1071 = 95.4%, Fisher p = 1.99e-14). Leaving out failed replays biases the comparison towards failures whose replay works.**

## Primary comparison: (b) gru_phys vs progress, unseen tasks, 2.5% false alarms

| model | timely (95% interval) | vs progress (paired 95% interval) | late / missed | median window | false alarms on successes | natural / perturbed |
|---|---|---|---|---|---|---|
| (b) gru_phys | 8 of 54 (3 to 13) | -2 (-8 to +4) | 19 / 27 | +96 (27) | 35 of 1022 (0.034) | 0.039 of 463 / 0.030 of 559 |
| progress | 10 of 54 (5 to 16) | | 22 / 22 | +152 (32) | 25 of 1022 (0.024) | 0.028 of 463 / 0.021 of 559 |

## Replay pass rate (all three rules)

| class | episodes | pass (all 3) | eef <= 10 mm | same outcome | goal objects <= 10 mm |
|---|---|---|---|---|---|
| successes | 1071 | 1022 (95.4%) | 1062 | 1039 | 1054 |
| recoverable failures | 31 | 29 (93.5%) | 30 | 31 | 29 |
| timed failures | 81 | 54 (66.7%) | 60 | 81 | 63 |
| doomed failures | 55 | 42 (76.4%) | 44 | 55 | 49 |
| all | 1238 | 1147 (92.6%) | 1196 | 1206 | 1195 |

Secondary: (a) Track 1 physical + old micro-events, CUSUM variants, seen split and 5%: unseen_report_fixed_*.md, seen_report_fixed_*.md, ranking.md. All runs use only episodes that passed.
