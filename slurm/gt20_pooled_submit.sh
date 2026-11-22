#!/bin/bash
# Nov 22 plan (results/plan_nov22_gt20.md, Step 4): interim pooled target (failed / all replays over checkpoints k-1, k, k+1).
# Smoke test first (2 epochs, held-out task 0, both policies); the full runs start only if it passes. Same models and seeds as n13_submit.sh.
# Output data/gt20/pooled/$POL/..., report results/gt20/pooled/ and results/gt20/pooled_main.md. CPU only.
cd ~/vla-failure-detector
smoke=()
for P in oft pi05; do
  smoke+=($(sbatch --parsable --array=0 --job-name=gt20p-smoke-$P \
    --export=ALL,POL=$P,MODEL=gru_phys_frac,SEED=0,OUT=data/gt20/pooled_smoke,EXTRA="--smoke --target pooled" slurm/n13_reg.sbatch))
done
sdep=$(IFS=:; echo "${smoke[*]}")
ids=()
for P in oft pi05; do
  ids+=($(sbatch --parsable --dependency=afterok:$sdep --array=0-9 --job-name=gt20p-$P-baselines \
    --export=ALL,POL=$P,MODEL=baselines,SEED=0,OUT=data/gt20/pooled,EXTRA="--target pooled" slurm/n13_reg.sbatch))
  for M in gru_phys_frac safe_lin safe_mlp safe_lstm gru_physvla_frac; do for S in 0 1 2 3 4; do
    ids+=($(sbatch --parsable --dependency=afterok:$sdep --array=0-9 --job-name=gt20p-$P-$M-s$S \
      --export=ALL,POL=$P,MODEL=$M,SEED=$S,OUT=data/gt20/pooled,EXTRA="--target pooled" slurm/n13_reg.sbatch))
  done; done
done
dep=$(IFS=:; echo "${ids[*]}")
rep=$(sbatch --parsable --dependency=afterok:$dep slurm/gt20_pooled_report.sbatch)
echo "smoke ${smoke[*]} train ${ids[0]} to ${ids[-1]} (${#ids[@]} arrays) report $rep"
