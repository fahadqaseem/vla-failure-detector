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
# Nov 7: OR combination for seeds 1 to 4 (47_combo.py per seed, progress reused from seed 0), results/combo/seeds.md (49_combo_seeds.py).
for P in oft pi05; do for T in 50 70 80; do for S in 1 2 3 4; do
  D=data/combo_seeds/$P/thr$T/s$S
  python scripts/47_combo.py --root $D --progress_root data/combo/$P/thr$T --out $D/merged > /dev/null || exit 1
done; done; done
python scripts/49_combo_seeds.py --out results/combo/seeds.md || exit 1
echo "| $(date +%F) | Nov 7: progress OR gru_phys_ttp, seeds 1 to 4 (gru_phys_ttp retrained with --save_calib, data/combo_seeds; progress reused from data/combo), 47_combo.py, 49_combo_seeds.py | $(git rev-parse --short HEAD) | results/combo/seeds.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "OR combination over seeds"
