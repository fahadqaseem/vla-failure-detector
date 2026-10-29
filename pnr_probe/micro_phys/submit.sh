#!/bin/bash
# micro_phys (Oct 29 2026), CPU only, jobs probe-*: combine inputs -> one array task per held-out group
# (unseen 10 tasks, seen 5 folds) -> merge per split -> report + figure (pushes pnr_probe/results/micro_phys).
set -e
cd ~/vla-probe; mkdir -p pnr_probe/logs pnr_probe/results/micro_phys
sub() { sbatch --parsable "$@"; }
C=$(sub -p mdtp -q primary -c 1 --mem 4G -t 1:00:00 -J probe-mp-combine -o pnr_probe/logs/%x-%j.out --mail-type=FAIL --mail-user=hr4625@wayne.edu \
    --wrap "source slurm/common.sh; for s in unseen seen; do python pnr_probe/micro_phys/combine.py --micro pnr_probe/data/\$s/micro --out pnr_probe/data/micro_phys/\$s; done")
M=""
for split in unseen seen; do
    if [ $split = unseen ]; then X=""; N=9; else X="--split episode"; N=4; fi
    P=$PWD/pnr_probe/data/micro_phys/$split
    A=$(sub --dependency=afterok:$C --array=0-$N -J probe-mp-$split --export=ALL,PHYS=$P,NAME=$split,ARGS="$X" pnr_probe/micro_phys/fold.sbatch)
    M="$M:$(sub --dependency=afterok:$A -J probe-mp-merge-$split -c 4 --mem 32G -t 2:00:00 -o pnr_probe/logs/%x-%j.out --export=ALL,PHYS=$P,NAME=$split,ARGS="$X",MERGE=1 pnr_probe/micro_phys/fold.sbatch)"
    echo "$split folds $A"
done
R=$(sub --dependency=afterany$M -J probe-mp-report pnr_probe/micro_phys/report.sbatch)
echo "$(date +%F) micro_phys: combine $C merge ${M//:/ } report $R" | tee -a pnr_probe/results/jobs.txt
