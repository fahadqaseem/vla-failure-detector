# Bio-inspired precursor features: ranking on unseen tasks

All data (natural + perturbed 7 tasks + perturbed_v2 tasks 0, 1, 4, 7, pooled), replay-scan t_pnr labels (refined),
leave-one-task-out. Rank: timely alarms of the set's best model with false alarms on held-out successes at or under
the budget, then median window (t_alarm - t_pnr) closest to 0. Models: mlp_phys, gru_phys, both also _cusum.
AUROC (per-step / time-matched, same model) is secondary. Intervals, paired difference from progress, natural /
perturbed false alarms and unnecessary alarms: unseen_report_fixed_0.025.md and unseen_report_fixed_0.05.md.

## Budget 2.5% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | progress (reference) | progress | 10 of 54 | 0.024 | +152 | 0.692 / 0.586 |
| 2 | a | gru_phys | 4 of 54 | 0.004 | +184 | 0.843 / 0.762 |
| 3 | b | none within budget (lowest 0.0342) | 0 | | | |

## Budget 5.0% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | progress (reference) | progress | 14 of 54 | 0.045 | +124 | 0.692 / 0.586 |
| 2 | a | gru_phys | 8 of 54 | 0.008 | +168 | 0.843 / 0.762 |
| 3 | b | none within budget (lowest 0.0616) | 0 | | | |

## Every model (secondary)

| split | feature set | model | timely, FPR, window at 2.5% | timely, FPR, window at 5% | AUROC per-step / time-matched |
|---|---|---|---|---|---|
| unseen | none | progress | 10 of 54, 0.024, +152 | 14 of 54, 0.045, +124 | 0.692 / 0.586 |
| unseen | a | gru_phys | 4 of 54, 0.004, +184 | 8 of 54, 0.008, +168 | 0.843 / 0.762 |
| unseen | a | gru_phys_cusum | 7 of 54, 0.049, +116 | 14 of 54, 0.086, +40 | 0.808 / 0.702 |
| seen | none | progress | 10 of 54, 0.024, +140 | 13 of 54, 0.044, +120 | 0.692 / 0.586 |
| seen | a | gru_phys | 15 of 54, 0.023, +72 | 16 of 54, 0.038, +56 | 0.936 / 0.910 |
| seen | a | gru_phys_cusum | 11 of 54, 0.021, +64 | 16 of 54, 0.053, +44 | 0.892 / 0.837 |
| unseen | b | gru_phys | 8 of 54, 0.034, +96 | 9 of 54, 0.062, +88 | 0.863 / 0.795 |
| unseen | b | gru_phys_cusum | 2 of 54, 0.069, +152 | 6 of 54, 0.114, +128 | 0.826 / 0.743 |
| seen | b | gru_phys | 15 of 54, 0.021, +72 | 19 of 54, 0.049, +60 | 0.924 / 0.904 |
| seen | b | gru_phys_cusum | 12 of 54, 0.027, +64 | 15 of 54, 0.045, +64 | 0.882 / 0.820 |
