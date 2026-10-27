# Bio-inspired precursor features: ranking on unseen tasks

All data (natural + perturbed 7 tasks + perturbed_v2 tasks 0, 1, 4, 7, pooled), replay-scan t_pnr labels (refined),
leave-one-task-out. Rank: timely alarms of the set's best model with false alarms on held-out successes at or under
the budget, then median window (t_alarm - t_pnr) closest to 0. Models: mlp_phys, gru_phys, both also _cusum.
AUROC (per-step / time-matched, same model) is secondary. Intervals, paired difference from progress, natural /
perturbed false alarms and unnecessary alarms: unseen_report_fixed_0.025.md and unseen_report_fixed_0.05.md.

## Budget 2.5% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | 4 micro-events | gru_phys | 13 of 81 | 0.024 | +164 | 0.831 / 0.743 |
| 2 | 5b 1-4 + Track 1 | gru_phys | 12 of 81 | 0.022 | +152 | 0.859 / 0.771 |
| 3 | Track 1 physical (reference) | gru_phys | 10 of 81 | 0.013 | +136 | 0.881 / 0.816 |
| 4 | 2 critical slowing down | gru_phys | 8 of 81 | 0.016 | +128 | 0.832 / 0.736 |
| 5 | 5a all of 1-4 | mlp_phys | 4 of 81 | 0.015 | +88 | 0.870 / 0.809 |
| 6 | 3 time-to-contact | mlp_phys_cusum | 2 of 81 | 0.023 | +104 | 0.603 / 0.511 |
| 7 | 1 surprise | mlp_phys | 2 of 81 | 0.017 | +112 | 0.641 / 0.600 |
| 8 | progress (reference) | none within budget (lowest 0.0252) | 0 | | | |

## Budget 5.0% false alarms

| rank | feature set | best model within budget | timely | false alarms on successes | median window | AUROC per-step / time-matched |
|---|---|---|---|---|---|---|
| 1 | progress (reference) | progress | 17 of 81 | 0.048 | +144 | 0.676 / 0.585 |
| 2 | 4 micro-events | gru_phys | 14 of 81 | 0.047 | +112 | 0.831 / 0.743 |
| 3 | Track 1 physical (reference) | gru_phys | 12 of 81 | 0.014 | +112 | 0.881 / 0.816 |
| 4 | 2 critical slowing down | gru_phys | 9 of 81 | 0.032 | +120 | 0.832 / 0.736 |
| 5 | 5b 1-4 + Track 1 | mlp_phys | 8 of 81 | 0.029 | +88 | 0.887 / 0.836 |
| 6 | 1 surprise | gru_phys | 7 of 81 | 0.042 | +128 | 0.695 / 0.617 |
| 7 | 5a all of 1-4 | mlp_phys | 6 of 81 | 0.021 | +80 | 0.870 / 0.809 |
| 8 | 3 time-to-contact | mlp_phys_cusum | 5 of 81 | 0.047 | +76 | 0.603 / 0.511 |

## Every model (secondary)

| split | feature set | model | timely, FPR, window at 2.5% | timely, FPR, window at 5% | AUROC per-step / time-matched |
|---|---|---|---|---|---|
| unseen | none | progress | 11 of 81, 0.025, +200 | 17 of 81, 0.048, +144 | 0.676 / 0.585 |
| unseen | 1 surprise | mlp_phys | 2 of 81, 0.017, +112 | 3 of 81, 0.134, +144 | 0.641 / 0.600 |
| unseen | 1 surprise | mlp_phys_cusum | 0 of 81, 0.007, +176 | 1 of 81, 0.016, +100 | 0.627 / 0.570 |
| unseen | 1 surprise | gru_phys | 2 of 81, 0.029, +116 | 7 of 81, 0.042, +128 | 0.695 / 0.617 |
| unseen | 1 surprise | gru_phys_cusum | 2 of 81, 0.042, +44 | 2 of 81, 0.044, +128 | 0.700 / 0.610 |
| seen | none | progress | 11 of 81, 0.026, +180 | 16 of 81, 0.046, +144 | 0.676 / 0.585 |
| seen | 1 surprise | mlp_phys | 7 of 81, 0.027, +120 | 15 of 81, 0.046, +72 | 0.876 / 0.827 |
| seen | 1 surprise | mlp_phys_cusum | 6 of 81, 0.023, +128 | 15 of 81, 0.047, +72 | 0.876 / 0.826 |
| seen | 1 surprise | gru_phys | 15 of 81, 0.026, +96 | 18 of 81, 0.052, +76 | 0.897 / 0.850 |
| seen | 1 surprise | gru_phys_cusum | 6 of 81, 0.011, +96 | 14 of 81, 0.035, +80 | 0.891 / 0.844 |
| unseen | 2 critical slowing down | mlp_phys | 8 of 81, 0.048, +136 | 10 of 81, 0.097, +104 | 0.870 / 0.801 |
| unseen | 2 critical slowing down | mlp_phys_cusum | 5 of 81, 0.017, +120 | 8 of 81, 0.043, +88 | 0.852 / 0.769 |
| unseen | 2 critical slowing down | gru_phys | 8 of 81, 0.016, +128 | 9 of 81, 0.032, +120 | 0.832 / 0.736 |
| unseen | 2 critical slowing down | gru_phys_cusum | 6 of 81, 0.014, +128 | 8 of 81, 0.026, +112 | 0.832 / 0.721 |
| seen | 2 critical slowing down | mlp_phys | 14 of 81, 0.021, +80 | 25 of 81, 0.049, +48 | 0.939 / 0.910 |
| seen | 2 critical slowing down | mlp_phys_cusum | 8 of 81, 0.019, +80 | 16 of 81, 0.046, +56 | 0.914 / 0.874 |
| seen | 2 critical slowing down | gru_phys | 6 of 81, 0.023, +140 | 12 of 81, 0.038, +104 | 0.899 / 0.844 |
| seen | 2 critical slowing down | gru_phys_cusum | 9 of 81, 0.023, +120 | 15 of 81, 0.049, +104 | 0.890 / 0.815 |
| unseen | 3 time-to-contact | mlp_phys | 0 of 81, 0.000, none | 10 of 81, 0.072, -32 | 0.700 / 0.674 |
| unseen | 3 time-to-contact | mlp_phys_cusum | 2 of 81, 0.023, +104 | 5 of 81, 0.047, +76 | 0.603 / 0.511 |
| unseen | 3 time-to-contact | gru_phys | 6 of 81, 0.056, +60 | 9 of 81, 0.073, +156 | 0.834 / 0.793 |
| unseen | 3 time-to-contact | gru_phys_cusum | 10 of 81, 0.026, +88 | 13 of 81, 0.050, +84 | 0.817 / 0.740 |
| seen | 3 time-to-contact | mlp_phys | 0 of 81, 0.000, none | 2 of 81, 0.011, +144 | 0.732 / 0.704 |
| seen | 3 time-to-contact | mlp_phys_cusum | 3 of 81, 0.022, +104 | 5 of 81, 0.038, +96 | 0.618 / 0.526 |
| seen | 3 time-to-contact | gru_phys | 12 of 81, 0.025, +96 | 18 of 81, 0.050, +96 | 0.873 / 0.828 |
| seen | 3 time-to-contact | gru_phys_cusum | 6 of 81, 0.019, +88 | 10 of 81, 0.045, +80 | 0.830 / 0.754 |
| unseen | 4 micro-events | mlp_phys | 9 of 81, 0.028, +204 | 13 of 81, 0.055, +160 | 0.779 / 0.716 |
| unseen | 4 micro-events | mlp_phys_cusum | 6 of 81, 0.032, +196 | 11 of 81, 0.058, +116 | 0.785 / 0.716 |
| unseen | 4 micro-events | gru_phys | 13 of 81, 0.024, +164 | 14 of 81, 0.047, +112 | 0.831 / 0.743 |
| unseen | 4 micro-events | gru_phys_cusum | 8 of 81, 0.034, +128 | 10 of 81, 0.049, +156 | 0.821 / 0.753 |
| seen | 4 micro-events | mlp_phys | 7 of 81, 0.023, +184 | 15 of 81, 0.054, +120 | 0.802 / 0.763 |
| seen | 4 micro-events | mlp_phys_cusum | 4 of 81, 0.015, +216 | 10 of 81, 0.042, +184 | 0.790 / 0.724 |
| seen | 4 micro-events | gru_phys | 11 of 81, 0.024, +168 | 18 of 81, 0.051, +132 | 0.859 / 0.804 |
| seen | 4 micro-events | gru_phys_cusum | 6 of 81, 0.021, +184 | 13 of 81, 0.051, +152 | 0.831 / 0.772 |
| unseen | 5a all of 1-4 | mlp_phys | 4 of 81, 0.015, +88 | 6 of 81, 0.021, +80 | 0.870 / 0.809 |
| unseen | 5a all of 1-4 | mlp_phys_cusum | 1 of 81, 0.005, +128 | 4 of 81, 0.023, +136 | 0.844 / 0.767 |
| unseen | 5a all of 1-4 | gru_phys | 2 of 81, 0.098, +144 | 4 of 81, 0.140, +148 | 0.841 / 0.743 |
| unseen | 5a all of 1-4 | gru_phys_cusum | 4 of 81, 0.129, +144 | 6 of 81, 0.158, +96 | 0.836 / 0.730 |
| seen | 5a all of 1-4 | mlp_phys | 14 of 81, 0.022, +80 | 21 of 81, 0.045, +56 | 0.947 / 0.921 |
| seen | 5a all of 1-4 | mlp_phys_cusum | 8 of 81, 0.019, +76 | 18 of 81, 0.043, +56 | 0.924 / 0.893 |
| seen | 5a all of 1-4 | gru_phys | 6 of 81, 0.022, +132 | 15 of 81, 0.053, +96 | 0.912 / 0.863 |
| seen | 5a all of 1-4 | gru_phys_cusum | 8 of 81, 0.021, +136 | 11 of 81, 0.049, +96 | 0.901 / 0.837 |
| unseen | 5b 1-4 + Track 1 | mlp_phys | 4 of 81, 0.012, +136 | 8 of 81, 0.029, +88 | 0.887 / 0.836 |
| unseen | 5b 1-4 + Track 1 | mlp_phys_cusum | 4 of 81, 0.003, +112 | 6 of 81, 0.012, +104 | 0.846 / 0.779 |
| unseen | 5b 1-4 + Track 1 | gru_phys | 12 of 81, 0.022, +152 | 16 of 81, 0.070, +112 | 0.859 / 0.771 |
| unseen | 5b 1-4 + Track 1 | gru_phys_cusum | 5 of 81, 0.110, +144 | 5 of 81, 0.139, +128 | 0.842 / 0.733 |
| seen | 5b 1-4 + Track 1 | mlp_phys | 13 of 81, 0.020, +80 | 21 of 81, 0.049, +52 | 0.954 / 0.935 |
| seen | 5b 1-4 + Track 1 | mlp_phys_cusum | 11 of 81, 0.019, +80 | 17 of 81, 0.045, +64 | 0.926 / 0.891 |
| seen | 5b 1-4 + Track 1 | gru_phys | 10 of 81, 0.020, +104 | 17 of 81, 0.041, +80 | 0.924 / 0.885 |
| seen | 5b 1-4 + Track 1 | gru_phys_cusum | 9 of 81, 0.016, +96 | 16 of 81, 0.037, +84 | 0.906 / 0.845 |
| unseen | Track 1 physical (reference) | mlp_phys | 4 of 81, 0.057, +124 | 6 of 81, 0.060, +136 | 0.879 / 0.831 |
| unseen | Track 1 physical (reference) | mlp_phys_cusum | 1 of 81, 0.019, +104 | 1 of 81, 0.051, +108 | 0.863 / 0.796 |
| unseen | Track 1 physical (reference) | gru_phys | 10 of 81, 0.013, +136 | 12 of 81, 0.014, +112 | 0.881 / 0.816 |
| unseen | Track 1 physical (reference) | gru_phys_cusum | 3 of 81, 0.044, +136 | 4 of 81, 0.118, +128 | 0.843 / 0.767 |
| seen | Track 1 physical (reference) | mlp_phys | 16 of 81, 0.025, +60 | 20 of 81, 0.057, +40 | 0.932 / 0.907 |
| seen | Track 1 physical (reference) | mlp_phys_cusum | 11 of 81, 0.026, +48 | 15 of 81, 0.051, +40 | 0.894 / 0.847 |
| seen | Track 1 physical (reference) | gru_phys | 19 of 81, 0.023, +64 | 23 of 81, 0.053, +48 | 0.938 / 0.913 |
| seen | Track 1 physical (reference) | gru_phys_cusum | 10 of 81, 0.021, +72 | 17 of 81, 0.049, +56 | 0.887 / 0.835 |
