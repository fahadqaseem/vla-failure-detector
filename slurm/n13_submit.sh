#!/bin/bash
# Nov 13 plan and amendment (results/plan_nov13.md): seeds 0 to 4 for every learned model, seed 0 for the baselines, both policies,
# one held-out task per array task; then n13_report (61_regression_report.py, 62_regression_plots.py, push). CPU only.
cd ~/vla-failure-detector
ids=()
for P in oft pi05; do
  ids+=($(sbatch --parsable --array=0-9 --job-name=n13-$P-baselines --export=ALL,POL=$P,MODEL=baselines,SEED=0 slurm/n13_reg.sbatch))
  for M in gru_phys_frac safe_lin safe_mlp safe_lstm gru_physvla_frac; do for S in 0 1 2 3 4; do
    ids+=($(sbatch --parsable --array=0-9 --job-name=n13-$P-$M-s$S --export=ALL,POL=$P,MODEL=$M,SEED=$S slurm/n13_reg.sbatch))
  done; done
done
dep=$(IFS=:; echo "${ids[*]}")
rep=$(sbatch --parsable --dependency=afterok:$dep slurm/n13_report.sbatch)
echo "train ${ids[*]} report $rep"
