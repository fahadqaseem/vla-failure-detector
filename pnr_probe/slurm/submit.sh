#!/bin/bash
# Bio-inspired precursor features (Oct 27 2026), CPU only, all jobs named probe-*.
# features (unseen, seen) -> 7 feature sets x 2 splits training runs -> report (pushes to pnr-probe).
# bash pnr_probe/slurm/submit.sh
set -e
cd ~/vla-probe; mkdir -p pnr_probe/logs
sub() { sbatch --parsable "$@"; }
F=""
for split in unseen seen; do
    s=$([ $split = unseen ] && echo task || echo episode)
    F="$F:$(sub -p mdtp -q primary -c 4 --mem 32G -t 6:00:00 -J probe-feat-$split -o pnr_probe/logs/%x-%j.out --mail-type=FAIL \
        --mail-user=hr4625@wayne.edu --wrap "source slurm/common.sh; export OMP_NUM_THREADS=4; python pnr_probe/precursor_features.py --split $s --out pnr_probe/data/$split")"
done
IDS=""
for split in unseen seen; do
    A=$([ $split = seen ] && echo "--split episode" || echo "")
    for set in surprise csd ttc micro bio bioplus t1; do
        P=$PWD/pnr_probe/data/$split/$set; [ $set = t1 ] && P=$HOME/vla-failure-detector/data/physical
        IDS="$IDS:$(sub --dependency=afterok$F -J probe-$split-$set --export=ALL,PHYS=$P,NAME=${split}_$set,ARGS="$A" pnr_probe/slurm/train.sbatch)"
    done
done
R=$(sub --dependency=afterany$IDS -J probe-report pnr_probe/slurm/report.sbatch)
echo "$(date +%F) features ${F//:/ } train ${IDS//:/ } report $R" | tee -a pnr_probe/results/jobs.txt
