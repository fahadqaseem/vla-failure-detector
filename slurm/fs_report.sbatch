#!/bin/bash
#SBATCH --job-name=fs-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# FailureSpot report: table.md, 13_report.py on LOTO with gru_phys and on each seed of its split; logged and pushed.
source slurm/common.sh
R=results/week3/failurespot
python scripts/28_merge_groups.py --dir $R/gru_phys/unseen --groups 10
python scripts/31_fs_report.py --root $R
for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $R/loto $R/gru_phys/unseen --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/loto_report_${k// /_}.md"
    python scripts/13_report.py --pred $R/own/g0 $R/own/g1 $R/own/g2 --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/own_report_${k// /_}.md"
done
rm -f $R/gru_phys/unseen/all_scores.json
echo "| $(date +%F) | FailureSpot methods on our data: 29_fs_convert.py, 30_fs_run.py (own split seeds 0 to 2; LOTO, 3 inner task folds for thresholds), 31_fs_report.py, 13_report.py; gru_phys retrained for its traces | $(git rev-parse --short HEAD) | $R/table.md, loto_report_*, own_report_* | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "week3: failurespot report"
