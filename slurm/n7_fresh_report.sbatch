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
# Nov 7 item 2: fresh Pi0.5 test report (new episodes only, models from old episodes), results/pi05/fresh. Not merged into older tables.
O=results/pi05/fresh; mkdir -p $O
for T in 50 70 80; do for SP in unseen seen; do n=10; [ $SP = seen ] && n=1
  B=data/pi05_fresh/thr$T/$SP
  for S in 0 1 2 3 4; do python scripts/28_merge_groups.py --dir $B/s$S/gru_phys_ttp --groups $n > /dev/null || exit 1; done
  python scripts/28_merge_groups.py --dir $B/s0/progress --groups $n > /dev/null || exit 1
  mkdir -p $B/ens; for S in 0 1 2 3 4; do ln -sfn ../s$S/gru_phys_ttp $B/ens/s$S; done; ln -sfn ../s0 $B/ens_combo
  python scripts/50_ensemble.py --root $B/ens --combo $B/s0 --groups $n --out $B/merged_ens || exit 1
  python - $B <<'P' || exit 1
import json, os, sys
b = sys.argv[1]
rows = [r for r in json.load(open(os.path.join(b, "s0/progress/per_episode.json")))]
for s in range(5):
    rows += [dict(r, model=f"gru_phys_ttp_s{s}") for r in json.load(open(os.path.join(b, f"s{s}/gru_phys_ttp/per_episode.json")))]
rows += json.load(open(os.path.join(b, "merged_ens/per_episode.json")))
os.makedirs(os.path.join(b, "merged"), exist_ok=True)
json.dump(rows, open(os.path.join(b, "merged", "per_episode.json"), "w"), indent=0)
P
  for k in "fixed 0.05" "fixed 0.025"; do
    python scripts/13_report.py --pred $B/merged --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$O/thr${T}_${SP}_report_${k// /_}.md" || exit 1
  done
  python scripts/46_paired_alarms.py --pred $B/merged --out $O/thr${T}_${SP}_alarms.md > /dev/null || exit 1
done; done
echo "| $(date +%F) | Nov 7 item 2: fresh Pi0.5 test, models and thresholds from the old episodes (natural + perturbed seeds 0, 1), scored only on perturbed seeds 2 to 4 (06 --fresh, data/pi05_fresh); progress, gru_phys_ttp seeds 0 to 4 and the seed ensemble (50_ensemble.py); 13_report.py, 46_paired_alarms.py | $(git rev-parse --short HEAD) | results/pi05/fresh/thr*_{unseen,seen}_report_*, *_alarms.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "pi05: fresh test report"
