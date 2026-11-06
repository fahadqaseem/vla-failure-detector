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
# Nov 6 item 5: realistic inputs vs gru_phys_ttp and progress (seed 0), results/realistic.
O=results/realistic; mkdir -p $O
for P in oft pi05; do R0=data/week3_reg; [ $P = pi05 ] && R0=data/pi05_reg
for T in 50 80; do for SP in unseen seen; do n=10; [ $SP = seen ] && n=5
  D=data/realistic/$P/thr$T/$SP
  for M in gru_robot_ttp gru_robotcontact_ttp; do python scripts/28_merge_groups.py --dir $D/$M --groups $n || exit 1; done
  python - $R0/thr$T/$SP $D <<'P' || exit 1
import json, os, sys
r0, d = sys.argv[1:]
rows = [r for r in json.load(open(os.path.join(r0, "per_episode.json"))) if r["model"] in ("progress", "gru_phys_ttp")]
for m in ("gru_robot_ttp", "gru_robotcontact_ttp"):
    rows += json.load(open(os.path.join(d, m, "per_episode.json")))
os.makedirs(os.path.join(d, "merged"), exist_ok=True)
json.dump(rows, open(os.path.join(d, "merged", "per_episode.json"), "w"), indent=0)
P
  for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $D/merged --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/${P}_thr${T}_${SP}_report_${k// /_}.md" || exit 1
  done
  python scripts/46_paired_alarms.py --pred $D/merged --out $O/${P}_thr${T}_${SP}_alarms.md || exit 1
done; done; done
echo "| $(date +%F) | Nov 6 item 5: gru_robot_ttp (eef position, rotation, gripper width) and gru_robotcontact_ttp (+ gripper touches a task object, robosuite check_contact, max over slots), seed 0, 50% and 80%, unseen and seen (n6_train.sbatch, data/realistic; Pi0.5 robot state 33_robot_state.py -> data/pi05/robot_state); 13_report.py, 46_paired_alarms.py | $(git rev-parse --short HEAD) | results/realistic/*_report_fixed_*.md, *_alarms.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "realistic inputs report"
