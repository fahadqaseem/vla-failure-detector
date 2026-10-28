#!/bin/bash
# Dense replay experiment (Oct 28 2026), CPU only, jobs probe-*: replay array -> dense features (unseen, seen)
# -> gru (a) Track 1 + old micro, (b) a + dense, unseen and seen -> report (pushes pnr_probe/results/dense).
set -e
cd ~/vla-probe; mkdir -p pnr_probe/logs pnr_probe/results/dense
D=$HOME/vla-failure-detector/data
ls $D/natural/*/*.npz $D/perturbed/task0[0145678]/*.npz $D/perturbed_v2/task0[0147]/*.npz > pnr_probe/dense/all_episodes.txt
N=$(wc -l < pnr_probe/dense/all_episodes.txt); CHUNK=50
sub() { sbatch --parsable "$@"; }
A=$(sub --array=0-$(((N + CHUNK - 1) / CHUNK - 1)) -J probe-dense-replay --export=ALL,CHUNK=$CHUNK pnr_probe/dense/replay_array.sbatch)
F=""
for split in unseen seen; do
    s=$([ $split = unseen ] && echo task || echo episode)
    F="$F:$(sub --dependency=afterok:$A -p mdtp -q primary -c 4 --mem 48G -t 12:00:00 -J probe-dense-feat-$split -o pnr_probe/logs/%x-%j.out \
        --mail-type=FAIL --mail-user=hr4625@wayne.edu --wrap "source slurm/common.sh; export OMP_NUM_THREADS=4; python pnr_probe/dense/dense_features.py --split $s --micro pnr_probe/data/$split/micro --out pnr_probe/data/dense_feat/$split")"
done
IDS=""
for split in unseen seen; do
    X=$([ $split = seen ] && echo "--split episode" || echo "")
    for set in a b; do
        IDS="$IDS:$(sub --dependency=afterok$F -J probe-dense-$split-$set --export=ALL,PHYS=$PWD/pnr_probe/data/dense_feat/$split/$set,NAME=${split}_$set,ARGS="$X" pnr_probe/dense/train.sbatch)"
    done
done
R=$(sub --dependency=afterany$IDS -J probe-dense-report pnr_probe/dense/report.sbatch)
echo "$(date +%F) dense: $N episodes, replay $A features ${F//:/ } train ${IDS//:/ } report $R" | tee -a pnr_probe/results/jobs.txt
