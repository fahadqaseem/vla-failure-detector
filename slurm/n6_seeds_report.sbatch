#!/bin/bash
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
# Nov 6 item 2: merge the seed runs, results/seeds (48_seeds.py).
for P in oft pi05; do for T in 50 70 80; do for SP in unseen seen; do n=10; [ $SP = seen ] && n=5
  for S in 1 2 3 4; do for M in gru_phys gru_phys_frac gru_phys_ttp; do
    python scripts/28_merge_groups.py --dir data/seeds/$P/thr$T/$SP/s$S/$M --groups $n || exit 1
  done; done; done; done; done
python scripts/48_seeds.py --out results/seeds || exit 1
echo "| $(date +%F) | Nov 6 item 2: 06_train_predictor.py seeds 1 to 4 (slurm/n6_train.sbatch, data/seeds), seed 0 = data/week3_reg, data/pi05_reg; 48_seeds.py | $(git rev-parse --short HEAD) | results/seeds/seeds_unseen.md (headline), seeds_seen.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "seeds report"
