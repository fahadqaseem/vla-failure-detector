#!/bin/bash
#SBATCH --job-name=w3-reg-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 3 regression and ablation report: merge, tables, logged and pushed. Scores stay in data/week3_reg (too big for git).
source slurm/common.sh
B=data/week3_reg; O=results/week3/regression
for t in 50 70 80; do
    python scripts/28_merge_groups.py --dir $B/thr$t/unseen --groups 10 || exit 1
    python scripts/28_merge_groups.py --dir $B/thr$t/seen --groups 5 || exit 1
    for k in "fixed 0.05" "fixed 0.025"; do
        python scripts/13_report.py --pred $B/thr$t/unseen --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/thr${t}_unseen_report_${k// /_}.md"
        python scripts/13_report.py --pred $B/thr$t/seen --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/thr${t}_seen_report_${k// /_}.md"
    done
done
python scripts/34_reg_report.py --root $B --out $O
echo "| $(date +%F) | Week 3 regression and ablation: 06_train_predictor.py --only_group (--fail_thr 0.7, 0.8; none = 50%), gru_phys, gru_phys_frac, gru_phys_ttp, gru_robot, gru_robotobj1, gru_robotobj2, unseen and seen; 34_reg_report.py, 13_report.py | $(git rev-parse --short HEAD) | $O/table_unseen.md (headline), table_seen.md, thr*_report_* | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "week3: regression report"
