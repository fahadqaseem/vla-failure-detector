#!/bin/bash
#SBATCH --job-name=n13-pick
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
# Nov 13 plan: seed-0 report, pick the best two learned models (rule in the plan), submit seeds 1 to 4 for them, then the final report.
O=results/regression_v2; mkdir -p $O
python scripts/61_regression_report.py --root data/regression_v2 --out $O || exit 1
BEST=$(cat $O/best2.txt)
echo "| $(date +%F) | Nov 13 regression seed 0 (60_regression.py, n13_reg.sbatch): report, per_task, backup_alarms; best two = $BEST | $(git rev-parse --short HEAD) | results/regression_v2/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "regression v2: seed 0 report"
ids=()
for P in oft pi05; do for M in $BEST; do for S in 1 2 3 4; do
  ids+=($(sbatch --parsable --array=0-9 --job-name=n13-$P-$M-s$S --export=ALL,POL=$P,MODEL=$M,SEED=$S slurm/n13_reg.sbatch))
done; done; done
dep=$(IFS=:; echo "${ids[*]}")
rep=$(sbatch --parsable --dependency=afterok:$dep --export=ALL,BEST="$BEST" slurm/n13_report.sbatch)
echo "seeds ${ids[*]} report $rep"
echo "| $(date +%F) | Nov 13 regression seeds 1 to 4 for $BEST submitted: ${ids[*]}; final report $rep | $(git rev-parse --short HEAD) | submitted | CPU only |" >> results/LOG.md
bash slurm/w2_push.sh "regression v2: seeds submitted"
