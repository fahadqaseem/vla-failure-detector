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
# Nov 12 add-one-signal: per policy, 47_combo.py OR for all groups and each group alone, merged into one per_episode.json, then 13_report.py, 46_paired_alarms.py.
O=results/single_signals; mkdir -p $O
for P in oft pi05; do
  R=data/single/$P/thr70
  for V in all goal pose contact gripper; do
    python scripts/47_combo.py --root $R/$V --progress_root $R --out $R/$V/merged > $O/${P}_thr70_levels_$V.txt || exit 1
  done
  python - $R <<'PY' || exit 1
import json, os, sys
r = sys.argv[1]
rows = [x for x in json.load(open(os.path.join(r, "all", "merged", "per_episode.json")))]
for v in ("goal", "pose", "contact", "gripper"):
    for x in json.load(open(os.path.join(r, v, "merged", "per_episode.json"))):
        if x["model"] == "gru_phys_ttp":
            rows.append(dict(x, model=f"ttp_{v}_only"))
        elif x["model"] == "or_progress_ttp":
            rows.append(dict(x, model=f"or_progress_{v}_only"))
os.makedirs(os.path.join(r, "merged"), exist_ok=True)
json.dump(rows, open(os.path.join(r, "merged", "per_episode.json"), "w"), indent=0)
PY
  for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $R/merged --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/${P}_thr70_report_${k// /_}.md" || exit 1
  done
  python scripts/46_paired_alarms.py --pred $R/merged --out $O/${P}_thr70_alarms.md > /dev/null || exit 1
done
echo "| $(date +%F) | Nov 12 add-one-signal: gru_phys_ttp with one physical group alone (06 --phys_keep; goal: goal_dist in_goal; pose: pos_ dz lifted tilt; contact; gripper: dist ddist grip_open) and each OR progress (47_combo.py), 70% rule, unseen, seed 0, both policies; progress and all-groups rerun on the same episodes (n12_single_submit.sh, n6_train.sbatch, data/single); 13_report.py, 46_paired_alarms.py | $(git rev-parse --short HEAD) | results/single_signals/*_report_*, *_alarms.md, *_levels_*.txt | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "single-signal report"
