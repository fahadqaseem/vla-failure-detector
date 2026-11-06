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
# Nov 6 item 4: OR combination per policy and rule, results/combo (47_combo.py, 13_report.py, 46_paired_alarms.py).
O=results/combo; mkdir -p $O
for P in oft pi05; do for T in 50 70 80; do
  D=data/combo/$P/thr$T
  python scripts/47_combo.py --root $D --out $D/merged > $O/${P}_thr${T}_levels.txt || exit 1
  for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $D/merged --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/${P}_thr${T}_report_${k// /_}.md" || exit 1
  done
  python scripts/46_paired_alarms.py --pred $D/merged --out $O/${P}_thr${T}_alarms.md || exit 1
done; done
echo "| $(date +%F) | Nov 6 item 4: progress OR gru_phys_ttp, thresholds from training-task calibration successes per fold (06 --save_calib, data/combo); 47_combo.py, 13_report.py, 46_paired_alarms.py | $(git rev-parse --short HEAD) | results/combo/{oft,pi05}_thr{50,70,80}_report_fixed_*.md, *_alarms.md, *_levels.txt | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "OR combination report"
