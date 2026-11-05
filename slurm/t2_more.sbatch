#!/bin/bash
#SBATCH --job-name=t2-more
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 (Fahad, Nov 2): more failures on the 6 natural-gate tasks until $TARGET are scanned. Round R = 50 episodes per task, own gate:
# 2 to 3 cm seeds 1, 2 (600 episodes), then level 2 (4 to 6 cm, 30 degrees, data/$P/perturbed_l2, reported separately), at most 4 rounds.
# STAGE=collect: stop and train, or collect + pre-check for round R. STAGE=scan: scan list of the round (cut at the target), then round R + 1.
source slurm/common.sh
source slurm/t2_fail.sh
TARGET=40
ROUNDS=(perturbed:1 perturbed:2 perturbed_l2:11 perturbed_l2:12 perturbed_l2:13 perturbed_l2:14)
TL="ALL=0,1,4,5,6,7 EVEN=0,4,6 ODD=1,5,7"  # only for these split_tasks calls (Nov 4: exported, they leaked into pifs-chunks via t2_train_submit)
source slurm/t2_split.sh
HAVE=$(python scripts/43_more_report.py --policy $P | tail -1)
C=$(git rev-parse --short HEAD)
log() { echo "| $(date +%F) | t2_more round $R $STAGE: $1 | $C | $HAVE of $TARGET scanned failures | job $SLURM_JOB_ID (auto) |" >> results/LOG.md; }
if [ "$STAGE" = collect ]; then
    if [ "$HAVE" -ge "$TARGET" ] || [ "$R" -ge "${#ROUNDS[@]}" ]; then
        X=$(sbatch --parsable --export=ALL,P=$P slurm/t2_train_submit.sbatch)
        log "stopped, training $X, results/$P/more_failures.md"
        bash slurm/w2_push.sh "$P: more failures done"
        exit 0
    fi
    KIND=${ROUNDS[$R]%:*}; SEED=${ROUNDS[$R]#*:}
    F=$(bash slurm/gpu_free.sh)
    E=$(env $TL bash -c 'source slurm/t2_split.sh; split_tasks "$@"' _ "t2-collect-$P-$KIND-s$SEED" "ALL,PNR_POLICY=$P,KIND=$KIND,SEED=$SEED,START=0,N=50,GATE=1" "" "$F" slurm/t2_collect.sbatch) || exit 1
    Q=$(env $TL bash -c 'source slurm/t2_split.sh; split_tasks "$@"' _ "t2-precheck-$P-$KIND-s$SEED" "ALL,PNR_POLICY=$P,KIND=$KIND,SEED=$SEED" "afterany:$E" "$F" slurm/t2_precheck.sbatch) || exit 1
    N=$(sbatch --parsable --dependency=afterany:$Q --export=ALL,P=$P,R=$R,STAGE=scan slurm/t2_more.sbatch) || exit 1
    log "$KIND seed $SEED, collect $E, pre-check $Q, next $N"
else
    KIND=${ROUNDS[$R]%:*}; SEED=${ROUNDS[$R]#*:}
    OUT=data/$P/${KIND}_scans
    T=results/$P/${KIND}_scans/targets_s$SEED.txt
    python scripts/scan_targets.py --root data/$P/$KIND --n_success 0 --prechecks data/$P/$KIND/prechecks --require_gate --out $T.all || exit 1
    while read -r EP; do [ -f "$OUT/$(basename "$EP" .npz).json" ] || echo "$EP"; done < $T.all | head -n $((TARGET - HAVE)) > $T
    rm $T.all
    NT=$(grep -c . $T)
    DEP=""; S=none
    if [ "$NT" -gt 0 ]; then
        F=$(bash slurm/gpu_free.sh)
        S=$(split_scan "t2-scan-$P-$KIND-s$SEED" "$NT" "ALL,PNR_POLICY=$P,TARGETS=$T,OUT=$OUT" "" "$F") || exit 1
        DEP="--dependency=afterany:$S"
    fi
    N=$(sbatch --parsable $DEP --export=ALL,P=$P,R=$((R + 1)),STAGE=collect slurm/t2_more.sbatch) || exit 1
    log "$KIND seed $SEED, $NT scans $S, next $N"
fi
bash slurm/w2_push.sh "$P: t2_more round $R $STAGE"
