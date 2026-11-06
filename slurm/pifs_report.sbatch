#!/bin/bash
#SBATCH --job-name=pifs-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# FailureSpot on Pi0.5: table next to our models and progress, logged and pushed. Main table (Fahad, Nov 6): held-out episodes of the 6
# gate-passed tasks only (0, 1, 4, 5, 6, 7), like for like; secondary: all 10 tasks plus the per-task gate and chunk check. Our rows (progress,
# gru_phys, gru_phys_ttp) come from the seed 0 regression run at 50% (data/$P_reg/thr50/unseen), same data and labels.
source slurm/common.sh
source slurm/t2_fail.sh
R=results/$P/failurespot; OS=data/${P}_reg/thr50/unseen/all_scores.json
python scripts/31_fs_report.py --root $R --ours_scores $OS --tasks 0 1 4 5 6 7 --table table.md --loto_out $R/loto6 || exit 1
python scripts/31_fs_report.py --root $R --ours_scores $OS --table table_all10.md --loto_out $R/loto --task_table data/$P || exit 1
for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $R/loto6 --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/loto_report_${k// /_}.md" || exit 1
    python scripts/13_report.py --pred $R/loto --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/loto_all10_report_${k// /_}.md" || exit 1
done
echo "| $(date +%F) | FailureSpot on Pi0.5 ($DATA): 41_pi_chunks.py, 45_check_chunks.py, 29_fs_convert.py, 30_fs_run.py (H 50, K 8; pi0.yaml), 31_fs_report.py (main: tasks 0, 1, 4, 5, 6, 7; secondary: all 10 with chunk check), 13_report.py | $(git rev-parse --short HEAD) | $R/table.md (6 gate-passed tasks, headline), loto_report_*; table_all10.md, loto_all10_report_* | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "$P: failurespot report"
