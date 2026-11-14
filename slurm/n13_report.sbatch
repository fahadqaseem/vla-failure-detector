#!/bin/bash
#SBATCH --job-name=n13-report
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
# Nov 13 plan: final report with seeds 0 to 4 for the best two models (BEST from n13_pick.sbatch).
O=results/regression_v2; mkdir -p $O
python scripts/61_regression_report.py --root data/regression_v2 --out $O --seed_models $BEST || exit 1
echo "| $(date +%F) | Nov 13 regression final (60_regression.py, 61_regression_report.py): seeds 0 to 4 for $BEST, report.md, per_task.md, backup_alarms.md, seeds.md | $(git rev-parse --short HEAD) | results/regression_v2/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "regression v2: final report"
