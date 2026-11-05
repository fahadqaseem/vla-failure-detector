#!/bin/bash
#SBATCH --job-name=p3-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Pi0.5 regression report: join models per group, merge groups, 13_report.py, 34_reg_report.py, 40_intervals.py; logged and pushed.
source slurm/common.sh
source slurm/t2_fail.sh
B=data/pi05_reg; O=results/pi05/regression; mkdir -p $O
MODELS="progress gru_phys gru_phys_frac gru_phys_ttp"
for t in 50 70 80; do for s in unseen seen; do
    n=10; [ $s = seen ] && n=5
    python - $B/thr$t/$s $n $MODELS <<'P' || exit 1
import json, os, sys
d, n, models = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
for g in range(n):
    rows = [r for m in models for r in json.load(open(os.path.join(d, m, f"g{g}", "all_scores.json")))]
    os.makedirs(os.path.join(d, f"g{g}"), exist_ok=True)
    json.dump(rows, open(os.path.join(d, f"g{g}", "all_scores.json"), "w"))
P
    python scripts/28_merge_groups.py --dir $B/thr$t/$s --groups $n || exit 1
    for k in "fixed 0.05" "fixed 0.025"; do
        python scripts/13_report.py --pred $B/thr$t/$s --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/thr${t}_${s}_report_${k// /_}.md" || exit 1
    done
done; done
python scripts/34_reg_report.py --root $B --out $O --desc "Pi0.5: natural (500) + perturbed 2 to 3 cm, seeds 0 and 1, gate-passed tasks only, pooled." || exit 1
python scripts/40_intervals.py --dir $O --scores $B --thrs 50 70 80 --out $O/intervals.md || exit 1
echo "| $(date +%F) | Pi0.5 regression: 06_train_predictor.py --only_group (--fail_thr 0.7, 0.8; none = 50%), progress, gru_phys, gru_phys_frac, gru_phys_ttp, unseen and seen (slurm/p3_train.sbatch); 13_report.py, 34_reg_report.py, 40_intervals.py --thrs 50 70 80 | $(git rev-parse --short HEAD) | $O/table_unseen.md, table_seen.md, intervals.md, thr*_report_* | written by job $SLURM_JOB_ID (auto); scores in $B |" >> results/LOG.md
bash slurm/w2_push.sh "pi05: regression report"
