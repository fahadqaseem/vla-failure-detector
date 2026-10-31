# Models in the papers' metrics

See scripts/27_paper_metrics.py for the definitions. * = only alpha 0.20 is available for that run. n/a = the run did not save success scores.

| run | model | per-step AUROC | time-matched AUROC | trajectory AUROC | bACC | wACC | TWA |
|---|---|---|---|---|---|---|---|
| results/week3/baselines/seen | timer | 0.796 | 0.538 | 1.000 | 0.953 | 0.919 | 0.632 |
| results/week3/baselines/seen | progress | 0.676 | 0.585 | 0.962 | 0.864 | 0.878 | 0.627 |
| results/week3/baselines/seen | safe | 0.913 | 0.876 | 0.985 | 0.894 | 0.849 | 0.800 |
| results/week3/baselines/seen | hideseek | 0.801 | 0.659 | 0.985 | 0.861 | 0.800 | 0.656 |
| results/week2/T1all_seen_gru | gru_phys | 0.938 | 0.913 | n/a | 0.835* | 0.807* | 0.746* |
| results/week2/T1all_seen_gru | gru_phys_cusum | 0.887 | 0.835 | n/a | 0.768* | 0.778* | 0.683* |
| results/week2/T1all_seen_gru | gru_physvla | 0.935 | 0.893 | n/a | 0.859* | 0.813* | 0.759* |
| results/week2/T1all_seen_gru | gru_physvla_cusum | 0.914 | 0.857 | n/a | 0.836* | 0.800* | 0.727* |
| results/week2/T1all_seen_conv | conv_phys | 0.933 | 0.915 | n/a | 0.834* | 0.809* | 0.747* |
| results/week2/T1all_seen_conv | conv_phys_cusum | 0.903 | 0.864 | n/a | 0.814* | 0.817* | 0.716* |
| results/week2/T1all_seen_conv | conv_physvla | 0.956 | 0.934 | n/a | 0.871* | 0.821* | 0.785* |
| results/week2/T1all_seen_conv | conv_physvla_cusum | 0.932 | 0.895 | n/a | 0.864* | 0.826* | 0.766* |
| results/week2/T1all_seen_conv | conv_physall | 0.959 | 0.933 | n/a | 0.875* | 0.822* | 0.785* |
| results/week2/T1all_seen_conv | conv_physall_cusum | 0.936 | 0.897 | n/a | 0.868* | 0.815* | 0.770* |
| results/week2/D_seen | gated_mlp | 0.645 | 0.561 | n/a | 0.881* | 0.838* | 0.658* |
| results/week2/D_seen | gated_combined | 0.645 | 0.561 | n/a | 0.881* | 0.838* | 0.658* |
| results/week2/D_seen | mlp_cusum | 0.902 | 0.842 | n/a | 0.809* | 0.736* | 0.720* |
| results/week2/D_seen | combined_cusum | 0.912 | 0.854 | n/a | 0.859* | 0.835* | 0.766* |
| results/week2/D_seen | mlp_rescue_cusum | 0.907 | 0.846 | n/a | 0.859* | 0.817* | 0.749* |
| results/week2/D_seen | gru_cusum | 0.877 | 0.791 | n/a | 0.873* | 0.832* | 0.733* |
