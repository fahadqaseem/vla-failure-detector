# Bio-inspired precursor features: ranking on unseen tasks

All data (natural + perturbed 7 tasks + perturbed_v2 tasks 0, 1, 4, 7, pooled), replay-scan t_pnr labels (refined),
leave-one-task-out. Rank: timely alarms of the set's best model with false alarms on held-out successes at or under
the budget, then median window (t_alarm - t_pnr) closest to 0. Models: mlp_phys, gru_phys, both also _cusum.
AUROC (per-step / time-matched, same model) is secondary. Intervals, paired difference from progress, natural /
perturbed false alarms and unnecessary alarms: unseen_report_fixed_0.025.md and unseen_report_fixed_0.05.md.

## Budget 2.5% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | b | gru_phys | 8 of 78 | 0.015 | +136 | 0.863 / 0.785 |
| 2 | a | gru_phys | 7 of 78 | 0.003 | +128 | 0.859 / 0.771 |
| 3 | progress (reference) | none within budget (lowest 0.0340) | 0 | | | |

## Budget 5.0% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | progress (reference) | progress | 19 of 78 | 0.049 | +136 | 0.677 / 0.589 |
| 2 | a | none within budget (lowest 0.0921) | 0 | | | |
| 3 | b | none within budget (lowest 0.1009) | 0 | | | |

## Every model (secondary)

| split | feature set | model | timely, FPR, window at 2.5% | timely, FPR, window at 5% | AUROC per-step / time-matched |
|---|---|---|---|---|---|
| unseen | none | progress | 14 of 78, 0.034, +200 | 19 of 78, 0.049, +136 | 0.677 / 0.589 |
| unseen | a | gru_phys | 7 of 78, 0.003, +128 | 7 of 78, 0.092, +120 | 0.859 / 0.771 |
| unseen | a | gru_phys_cusum | 9 of 78, 0.185, +72 | 13 of 78, 0.209, +56 | 0.839 / 0.754 |
| seen | none | progress | 11 of 78, 0.025, +176 | 19 of 78, 0.043, +144 | 0.677 / 0.589 |
| seen | a | gru_phys | 16 of 78, 0.024, +72 | 22 of 78, 0.045, +56 | 0.946 / 0.915 |
| seen | a | gru_phys_cusum | 12 of 78, 0.018, +72 | 15 of 78, 0.045, +56 | 0.908 / 0.862 |
| unseen | b | gru_phys | 8 of 78, 0.015, +136 | 11 of 78, 0.101, +120 | 0.863 / 0.785 |
| unseen | b | gru_phys_cusum | 4 of 78, 0.167, +132 | 6 of 78, 0.191, +112 | 0.839 / 0.757 |
| seen | b | gru_phys | 14 of 78, 0.020, +72 | 19 of 78, 0.038, +64 | 0.942 / 0.912 |
| seen | b | gru_phys_cusum | 10 of 78, 0.022, +84 | 14 of 78, 0.048, +56 | 0.904 / 0.853 |
