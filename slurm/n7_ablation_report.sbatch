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
# Nov 7 item 6: gru_phys_ttp without goal (goal_dist, in_goal), object pose (pos_, dz, lifted, tilt) or contact, seed 0, unseen, 50% and 70%.
O=results/ablation; mkdir -p $O
for P in oft pi05; do R0=data/week3_reg; [ $P = pi05 ] && R0=data/pi05_reg
for T in 50 70; do
  for V in goal pose contact; do python scripts/28_merge_groups.py --dir data/ablation/$P/thr$T/$V --groups 10 || exit 1; done
  python - $R0/thr$T/unseen data/ablation/$P/thr$T <<'P' || exit 1
import json, os, sys
r0, d = sys.argv[1:]
rows = [r for r in json.load(open(os.path.join(r0, "per_episode.json"))) if r["model"] in ("progress", "gru_phys_ttp")]
for v in ("goal", "pose", "contact"):
    rows += [dict(r, model=f"gru_phys_ttp_no_{v}") for r in json.load(open(os.path.join(d, v, "per_episode.json")))]
os.makedirs(os.path.join(d, "merged"), exist_ok=True)
json.dump(rows, open(os.path.join(d, "merged", "per_episode.json"), "w"), indent=0)
P
  for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred data/ablation/$P/thr$T/merged --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/${P}_thr${T}_report_${k// /_}.md" || exit 1
  done
  python scripts/46_paired_alarms.py --pred data/ablation/$P/thr$T/merged --out $O/${P}_thr${T}_alarms.md > /dev/null || exit 1
done; done
echo "| $(date +%F) | Nov 7 item 6: 06 --phys_drop (goal: goal_dist in_goal; pose: pos_ _dz lifted tilt; contact), gru_phys_ttp seed 0, unseen, 50% and 70% (n6_train.sbatch, data/ablation); 13_report.py, 46_paired_alarms.py | $(git rev-parse --short HEAD) | results/ablation/*_report_*, *_alarms.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "ablation report"
