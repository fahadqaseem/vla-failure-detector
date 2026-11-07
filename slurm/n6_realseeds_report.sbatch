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
# Nov 7: seeds 1 to 4 of the realistic-input models, results/seeds/realistic_unseen.md (48_seeds.py).
for P in oft pi05; do for T in 50 80; do for S in 1 2 3 4; do for M in gru_robot_ttp gru_robotcontact_ttp; do
  python scripts/28_merge_groups.py --dir data/seeds_real/$P/thr$T/unseen/s$S/$M --groups 10 || exit 1
done; done; done; done
python scripts/48_seeds.py --seed0 oft:data/realistic/oft pi05:data/realistic/pi05 --seed0_sub merged --root data/seeds_real \
    --models gru_robotcontact_ttp gru_robot_ttp --thrs 50 80 --splits unseen --name realistic --out results/seeds || exit 1
echo "| $(date +%F) | Nov 7: gru_robotcontact_ttp and gru_robot_ttp seeds 1 to 4 (n6_train.sbatch, data/seeds_real), seed 0 = data/realistic; 48_seeds.py | $(git rev-parse --short HEAD) | results/seeds/realistic_unseen.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "realistic-input seeds"
