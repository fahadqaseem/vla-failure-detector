#!/bin/bash
#SBATCH --job-name=b3-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 3 baselines report: merge the groups, same tables as T1all, paper metrics for every model; logged and pushed.
source slurm/common.sh
B=results/week3/baselines; W=results/week2
python scripts/28_merge_groups.py --dir $B/unseen --groups 10 || exit 1
python scripts/28_merge_groups.py --dir $B/seen --groups 5 || exit 1
for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $B/unseen $W/T1all_unseen_gru $W/T1all_unseen_conv --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$B/unseen_report_${k// /_}.md"
    python scripts/13_report.py --pred $B/seen $W/T1all_seen_gru $W/T1all_seen_conv --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$B/seen_report_${k// /_}.md"
done
python scripts/27_paper_metrics.py --pred $B/unseen $W/T1all_unseen_gru $W/T1all_unseen_conv $W/D_unseen --out $B/paper_metrics_unseen.md
python scripts/27_paper_metrics.py --pred $B/seen $W/T1all_seen_gru $W/T1all_seen_conv $W/D_seen --out $B/paper_metrics_seen.md
echo "| $(date +%F) | Week 3 baselines on all data: 06_train_predictor.py --only_group (array, slurm/b3_train.sbatch), safe, hideseek, timer, progress; 28_merge_groups.py, 13_report.py, 27_paper_metrics.py | $(git rev-parse --short HEAD) | $B/unseen_report_fixed_0.05.md (headline), paper_metrics_unseen.md, seen_* | written by job $SLURM_JOB_ID (auto); hideseek built from the paper, code not released |" >> results/LOG.md
bash slurm/w2_push.sh "week3: baselines report"
