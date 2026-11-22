#!/bin/bash
# Nov 22 amendment (results/plan_nov22_gt20.md): full 20-replay ground truth. OFT workers first (array %5 = the GPU cap), Pi0.5 workers
# after them; when the OFT workers end, regression v2 on the OFT 20-replay truth (60_regression.py --target gt20, every model, seeds 0
# to 4, CPU) and its report (results/gt20/main.md, seeds.md, backup.md, per_task.md, plots_reg/).
cd ~/vla-failure-detector
W=${W:-5}
o=$(sbatch --parsable ${AFTER:+--dependency=afterany:$AFTER} --array=0-$((W - 1))%$W --job-name=gt20-oft --export=ALL,P=oft slurm/gt20_worker.sbatch)
pi=$(sbatch --parsable --dependency=afterany:$o --array=0-$((W - 1))%$W --job-name=gt20-pi05 --export=ALL,P=pi05 slurm/gt20_worker.sbatch)
ids=($(sbatch --parsable --dependency=afterany:$o --array=0-9 --job-name=gt20r-oft-baselines \
  --export=ALL,POL=oft,MODEL=baselines,SEED=0,OUT=data/gt20/regression,EXTRA="--target gt20 --gt20_dir data/gt20/oft" slurm/n13_reg.sbatch))
for M in gru_phys_frac safe_lin safe_mlp safe_lstm gru_physvla_frac; do for S in 0 1 2 3 4; do
  ids+=($(sbatch --parsable --dependency=afterany:$o --array=0-9 --job-name=gt20r-oft-$M-s$S \
    --export=ALL,POL=oft,MODEL=$M,SEED=$S,OUT=data/gt20/regression,EXTRA="--target gt20 --gt20_dir data/gt20/oft" slurm/n13_reg.sbatch))
done; done
dep=$(IFS=:; echo "${ids[*]}")
rep=$(sbatch --parsable --dependency=afterok:$dep slurm/gt20_report.sbatch)
echo "oft workers $o, pi05 workers $pi, regression ${ids[0]} to ${ids[-1]} (${#ids[@]} arrays), report $rep"
