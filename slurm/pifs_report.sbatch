#!/bin/bash
#SBATCH --job-name=pifs-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# FailureSpot on Pi0.5: table next to gru_phys and progress, logged and pushed.
source slurm/common.sh
source slurm/t2_fail.sh
R=results/$P/failurespot; G=results/$P/${DATA}_unseen_gru
python scripts/31_fs_report.py --root $R --progress $G/per_episode.json --gru $G || exit 1
for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $R/loto $G --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/loto_report_${k// /_}.md"
done
echo "| $(date +%F) | FailureSpot on Pi0.5 ($DATA): 41_pi_chunks.py, 29_fs_convert.py, 30_fs_run.py (H 50, K 8; pi0.yaml), 31_fs_report.py, 13_report.py | $(git rev-parse --short HEAD) | $R/table.md, loto_report_* | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "$P: failurespot report"
