# Dense replay features: summary

Bias check: timed failures pass 78/81 (96.3%), successes 912/1071 (85.2%), Fisher p = 0.00265: no large gap (rule: more than 10 points lower, or p < 0.05).

## Replay pass rate (all three rules)

| class | episodes | pass (all 3) | eef <= 10 mm | same outcome | goal objects <= 10 mm |
|---|---|---|---|---|---|
| successes | 1071 | 912 (85.2%) | 953 | 993 | 971 |
| recoverable failures | 31 | 28 (90.3%) | 28 | 29 | 28 |
| timed failures | 81 | 78 (96.3%) | 79 | 81 | 78 |
| doomed failures | 55 | 54 (98.2%) | 54 | 55 | 55 |
| all | 1238 | 1072 (86.6%) | 1114 | 1158 | 1132 |

Secondary: (a) Track 1 physical + old micro-events, CUSUM variants, seen split and 5%: unseen_report_fixed_*.md, seen_report_fixed_*.md, ranking.md. All runs use only episodes that passed.
