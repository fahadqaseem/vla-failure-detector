# Models in the papers' metrics

See scripts/27_paper_metrics.py for the definitions. * = only alpha 0.20 is available for that run. n/a = the run did not save success scores.

| run | model | per-step AUROC | time-matched AUROC | trajectory AUROC | bACC | wACC | TWA |
|---|---|---|---|---|---|---|---|
| data/week3_grasp/seen | gru_grasp | 0.919 | 0.865 | 0.968 | 0.849 | 0.804 | 0.723 |
| data/week3_grasp/seen | gru_graspreal | 0.895 | 0.837 | 0.956 | 0.859 | 0.812 | 0.716 |
| data/week3_grasp/seen | gru_graspphys | 0.934 | 0.906 | 0.953 | 0.870 | 0.834 | 0.761 |
| data/week3_grasp/seen | gru_phys | 0.938 | 0.913 | 0.942 | 0.843 | 0.807 | 0.749 |
| data/week3_grasp/seen | gru_robot | 0.883 | 0.822 | 0.941 | 0.853 | 0.835 | 0.711 |
