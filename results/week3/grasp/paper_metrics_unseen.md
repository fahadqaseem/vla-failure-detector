# Models in the papers' metrics

See scripts/27_paper_metrics.py for the definitions. * = only alpha 0.20 is available for that run. n/a = the run did not save success scores.

| run | model | per-step AUROC | time-matched AUROC | trajectory AUROC | bACC | wACC | TWA |
|---|---|---|---|---|---|---|---|
| data/week3_grasp/unseen | gru_grasp | 0.878 | 0.792 | 0.944 | 0.841 | 0.826 | 0.681 |
| data/week3_grasp/unseen | gru_graspreal | 0.787 | 0.682 | 0.821 | 0.846 | 0.927 | 0.655 |
| data/week3_grasp/unseen | gru_graspphys | 0.867 | 0.785 | 0.913 | 0.750 | 0.640 | 0.587 |
| data/week3_grasp/unseen | gru_phys | 0.880 | 0.815 | 0.858 | 0.717 | 0.620 | 0.602 |
| data/week3_grasp/unseen | gru_robot | 0.767 | 0.658 | 0.779 | 0.817 | 0.852 | 0.623 |
