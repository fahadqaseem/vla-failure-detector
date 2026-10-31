# Models in the papers' metrics

See scripts/27_paper_metrics.py for the definitions. * = only alpha 0.20 is available for that run. n/a = the run did not save success scores.

| run | model | per-step AUROC | time-matched AUROC | trajectory AUROC | bACC | wACC | TWA |
|---|---|---|---|---|---|---|---|
| results/week3/baselines/unseen | timer | 0.796 | 0.538 | 1.000 | 0.958 | 0.926 | 0.555 |
| results/week3/baselines/unseen | progress | 0.676 | 0.585 | 0.962 | 0.868 | 0.881 | 0.623 |
| results/week3/baselines/unseen | safe | 0.827 | 0.734 | 0.904 | 0.787 | 0.784 | 0.645 |
| results/week3/baselines/unseen | hideseek | 0.747 | 0.591 | 0.907 | 0.769 | 0.765 | 0.576 |
| results/week2/T1all_unseen_gru | gru_phys | 0.881 | 0.816 | n/a | 0.719* | 0.623* | 0.603* |
| results/week2/T1all_unseen_gru | gru_phys_cusum | 0.843 | 0.767 | n/a | 0.684* | 0.773* | 0.585* |
| results/week2/T1all_unseen_gru | gru_physvla | 0.848 | 0.740 | n/a | 0.788* | 0.708* | 0.636* |
| results/week2/T1all_unseen_gru | gru_physvla_cusum | 0.830 | 0.721 | n/a | 0.708* | 0.669* | 0.584* |
| results/week2/T1all_unseen_conv | conv_phys | 0.788 | 0.734 | n/a | 0.611* | 0.549* | 0.517* |
| results/week2/T1all_unseen_conv | conv_phys_cusum | 0.756 | 0.673 | n/a | 0.600* | 0.693* | 0.568* |
| results/week2/T1all_unseen_conv | conv_physvla | 0.889 | 0.815 | n/a | 0.783* | 0.673* | 0.629* |
| results/week2/T1all_unseen_conv | conv_physvla_cusum | 0.862 | 0.778 | n/a | 0.715* | 0.616* | 0.585* |
| results/week2/T1all_unseen_conv | conv_physall | 0.899 | 0.825 | n/a | 0.832* | 0.762* | 0.670* |
| results/week2/T1all_unseen_conv | conv_physall_cusum | 0.878 | 0.797 | n/a | 0.766* | 0.713* | 0.629* |
| results/week2/D_unseen | gated_mlp | 0.640 | 0.556 | n/a | 0.877* | 0.830* | 0.651* |
| results/week2/D_unseen | gated_combined | 0.639 | 0.556 | n/a | 0.877* | 0.830* | 0.651* |
| results/week2/D_unseen | mlp_cusum | 0.807 | 0.696 | n/a | 0.802* | 0.754* | 0.663* |
| results/week2/D_unseen | combined_cusum | 0.807 | 0.683 | n/a | 0.782* | 0.723* | 0.651* |
| results/week2/D_unseen | mlp_rescue_cusum | 0.802 | 0.690 | n/a | 0.757* | 0.688* | 0.638* |
| results/week2/D_unseen | gru_cusum | 0.796 | 0.671 | n/a | 0.826* | 0.765* | 0.642* |
