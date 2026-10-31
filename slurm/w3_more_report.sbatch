#!/bin/bash
#SBATCH --job-name=w3-more-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Complementarity and grasp-check reports (Oct 31), logged and pushed. Waits for the 50% regression and grasp arrays.
source slurm/common.sh
C=results/week3/complementarity; G=results/week3/grasp; B=data/week3_grasp
python scripts/37_complementarity.py --out $C || exit 1
for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $C --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$C/report_${k// /_}.md"
done
python scripts/28_merge_groups.py --dir $B/unseen --groups 10 || exit 1
python scripts/28_merge_groups.py --dir $B/seen --groups 5 || exit 1
python scripts/38_grasp_report.py --dir $B/unseen --ref data/week3_reg/thr50/unseen
python scripts/38_grasp_report.py --dir $B/seen --ref data/week3_reg/thr50/seen
for sp in unseen seen; do
    for k in "fixed 0.05" "fixed 0.025"; do
        python scripts/13_report.py --pred $B/$sp --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$G/${sp}_report_${k// /_}.md"
    done
    python scripts/27_paper_metrics.py --pred $B/$sp --out $G/paper_metrics_$sp.md
done
H=$(git rev-parse --short HEAD)
echo "| $(date +%F) | Complementarity: 37_complementarity.py, 13_report.py | $H | $C/venn.md, report_fixed_0.05.md, report_fixed_0.025.md | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
echo "| $(date +%F) | Grasp-check features: gru_grasp, gru_graspreal, gru_graspphys (array, b3_train.sbatch), 38_grasp_report.py, 13_report.py, 27_paper_metrics.py | $H | $G/unseen_report_fixed_0.05.md (headline), paper_metrics_unseen.md, seen_* | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "week3: complementarity and grasp reports"
