#!/bin/bash
# Nov 13 plan (results/plan_nov13.md): seed 0 for every model and both policies, then n13_pick (report, best two, seeds 1 to 4, final report).
cd ~/vla-failure-detector
ids=()
for P in oft pi05; do for M in gru_phys_frac safe_lin safe_mlp safe_lstm gru_physvla_frac baselines; do
  ids+=($(sbatch --parsable --array=0-9 --job-name=n13-$P-$M --export=ALL,POL=$P,MODEL=$M,SEED=0 slurm/n13_reg.sbatch))
done; done
dep=$(IFS=:; echo "${ids[*]}")
pick=$(sbatch --parsable --dependency=afterok:$dep slurm/n13_pick.sbatch)
echo "seed0 ${ids[*]} pick $pick"
