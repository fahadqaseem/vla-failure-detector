#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=01:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Gate after the per-chunk dense replays (Fahad, Oct 28): pass rates by class first (pushed), then, only if timed failures
# pass at least 90% and every episode has a replay file, submit features -> gru (a), (b) unseen + seen -> report,
# all into pnr_probe/results/dense_chunk (same features, models and primary comparison as pnr_probe/results/dense).
source slurm/common.sh
R=pnr_probe/results/dense_chunk; DENSE=pnr_probe/data/dense_chunk; FEAT=pnr_probe/data/dense_chunk_feat
mkdir -p $R
python pnr_probe/dense/report.py --dense $DENSE --labels pnr_probe/results/unseen_t1/per_episode.json \
    --episodes pnr_probe/dense/all_episodes.txt --results $R --out $R/pass_rates.md --pass_only --timed_rate_out $R/timed_pass_rate.txt
RATE=$(cat $R/timed_pass_rate.txt); MISSING=$(grep -c "No dense replay file" $R/pass_rates.md || true)
GO=$(python -c "print(int($RATE >= 0.90 and $MISSING == 0))")
if [ "$GO" = 1 ]; then
    sub() { sbatch --parsable "$@"; }
    F=""
    for split in unseen seen; do
        s=$([ $split = unseen ] && echo task || echo episode)
        F="$F:$(sub -p mdtp -q primary -c 4 --mem 48G -t 12:00:00 -J probe-chunk-feat-$split -o pnr_probe/logs/%x-%j.out \
            --mail-type=FAIL --mail-user=hr4625@wayne.edu --wrap "source slurm/common.sh; export OMP_NUM_THREADS=4; python pnr_probe/dense/dense_features.py --split $s --dense $DENSE --micro pnr_probe/data/$split/micro --out $FEAT/$split")"
    done
    IDS=""
    for split in unseen seen; do
        X=$([ $split = seen ] && echo "--split episode" || echo "")
        for set in a b; do
            IDS="$IDS:$(sub --dependency=afterok$F -J probe-chunk-$split-$set --export=ALL,PHYS=$PWD/$FEAT/$split/$set,NAME=${split}_$set,ARGS="$X",OUTR=$R,PASSED=$FEAT/unseen/passed.txt pnr_probe/dense/train.sbatch)"
        done
    done
    REP=$(sub --dependency=afterany$IDS -J probe-chunk-report --export=ALL,OUTR=$R,DENSE=$DENSE pnr_probe/dense/report.sbatch)
    MSG="timed pass $RATE >= 0.90: submitted features ${F//:/ } train ${IDS//:/ } report $REP"
else
    MSG="timed pass $RATE, missing replay files $MISSING: gate NOT passed, nothing submitted"
fi
echo "$MSG" | tee $R/gate.txt
echo "$(date +%F) dense_chunk gate: $MSG" >> pnr_probe/results/jobs.txt
echo "| $(date +%F) | dense_chunk gate: report.py --pass_only | $(git rev-parse --short HEAD) | $R/pass_rates.md, $R/gate.txt | job $SLURM_JOB_ID: $MSG |" >> pnr_probe/results/LOG.md
[ "$(git branch --show-current)" = pnr-probe ] || { echo "not on pnr-probe, not pushing"; exit 1; }
git add $R pnr_probe/results/jobs.txt pnr_probe/results/LOG.md pnr_probe/dense
git -c user.name="Fahad Qaseem Khawar" commit -qm "pnr_probe: dense_chunk replay pass rates (gate)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || echo "nothing to commit"
for try in 1 2; do git push -q -u origin pnr-probe && { echo pushed; exit 0; }; sleep 30; done
echo "PUSH FAILED" | tee -a $R/push_failures.txt
