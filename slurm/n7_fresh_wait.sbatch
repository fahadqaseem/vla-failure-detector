#!/bin/bash
#SBATCH --job-name=n7-fresh-wait
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:10:00
#SBATCH --output=logs/%x-%j.out
# Nov 7 item 2 (plan addendum (c)): wait until t2_more has 70 scanned Pi0.5 failures and no t2 job is left, then start the fresh test:
# physical signals of the new episodes (perturbed seeds 2 to 4, gate-passed folders), then 06 with --fresh (train and thresholds on the old
# episodes only, natural + seeds 0 and 1), progress and gru_phys_ttp seeds 0 to 4, three rules, unseen (one task per array task) and seen.
# Checks again every hour, at most N_LEFT more times.
source slurm/common.sh
HAVE=$(python scripts/43_more_report.py --policy pi05 | tail -1)
LEFT=$(squeue -h -u $USER -o %j | grep -c '^t2-')
if [ "$HAVE" -lt 70 ] || [ "$LEFT" -gt 0 ]; then
    [ "${N_LEFT:-96}" -le 0 ] && { echo "| $(date +%F) | n7 fresh test: still $HAVE of 70 scanned failures after the last check, not started | $(git rev-parse --short HEAD) | waiting stopped | job $SLURM_JOB_ID |" >> results/LOG.md; bash slurm/w2_push.sh "log: fresh test not started"; exit 0; }
    sbatch --begin=now+60minutes --export=ALL,N_LEFT=$((${N_LEFT:-96} - 1)) slurm/n7_fresh_wait.sbatch
    echo "waiting: $HAVE of 70, $LEFT t2 jobs"; exit 0
fi
NEW=(); for d in data/pi05/perturbed/task??_s2 data/pi05/perturbed/task??_s3 data/pi05/perturbed/task??_s4; do [ -f $d/GATE_PASS ] && NEW+=("$d/*.npz"); done
X=$(sbatch --parsable -p reqp -q requeue --requeue -c 2 --mem 16G -t 08:00:00 -J n7-fresh-phys -o logs/%x-%j.out \
    --wrap "source slurm/common.sh; python scripts/20_physical_signals.py --episodes ${NEW[*]} --out data/pi05/physical")
FR="--fresh ${NEW[*]}"
IDS=""
for T in 50 70 80; do
  for M in progress gru_phys_ttp; do for S in 0 1 2 3 4; do
    [ $M = progress ] && [ $S != 0 ] && continue
    IDS="$IDS:$(sbatch --parsable --array=0-9 --dependency=afterok:$X -J n7-fresh-unseen --export="ALL,POL=pi05,THR=$T,SPLIT=unseen,MODEL=$M,SEED=$S,EXTRA=--save_calib $FR,OUT=data/pi05_fresh/thr$T/unseen/s$S/$M" slurm/n6_train.sbatch)"
    IDS="$IDS:$(sbatch --parsable --array=0 --dependency=afterok:$X -J n7-fresh-seen --export="ALL,POL=pi05,THR=$T,SPLIT=unseen,MODEL=$M,SEED=$S,EXTRA=--save_calib --fresh_mode seen $FR,OUT=data/pi05_fresh/thr$T/seen/s$S/$M" slurm/n6_train.sbatch)"
  done; done
done
R=$(sbatch --parsable --dependency=afterany$IDS slurm/n7_fresh_report.sbatch)
echo "| $(date +%F) | Nov 7 item 2: fresh Pi0.5 test started at $HAVE scanned failures: physical $X, 06 --fresh arrays ${IDS:1:8} to ${IDS: -8}, report $R; new episodes: ${NEW[*]} | $(git rev-parse --short HEAD) | submitted | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "log: fresh Pi0.5 test started"
