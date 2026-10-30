#!/bin/bash
#SBATCH --job-name=w2-train
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=3-00:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2: one 06_train_predictor.py run into ${OUTROOT:-results/week2}/$NAME. DATA=old: natural + perturbed (7 of 10 tasks);
# DATA=all: also perturbed_v2 (tasks whose replay gate passed) and the K 16 refined labels. Extra flags in ARGS.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
SCANS=("data/full_scans/*.json" "data/perturbed_scans/*.json")
EPS=("data/natural/*/*.npz" "data/perturbed/task0[0145678]/*.npz")
PRE=(data/perturbed/prechecks)
if [ "$DATA" = "all" ]; then
    SCANS+=("data/perturbed_v2_scans/*.json")
    for d in data/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
    PRE+=(data/perturbed_v2/prechecks)
    REF="--refine data/week2_refine"
fi
echo "DATA=$DATA episodes: ${EPS[*]}"
python scripts/06_train_predictor.py --scans "${SCANS[@]}" --episodes "${EPS[@]}" --prechecks "${PRE[@]}" \
    ${REF:-} $ARGS --out ${OUTROOT:-results/week2}/$NAME
