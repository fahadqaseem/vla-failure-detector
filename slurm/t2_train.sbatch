#!/bin/bash
#SBATCH --job-name=t2-train
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=3-00:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2: one 06_train_predictor.py run on policy $P's data into results/$P/$NAME. DATA=natural, all (natural +
# perturbed, pooled and said so in the summary) or l2 (all + level 2 perturbations). Extra flags in ARGS.
source slurm/common.sh
source slurm/t2_fail.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
SCANS=("data/$P/full_scans/*.json"); EPS=("data/$P/natural/*/*.npz"); PRE=()
if [ "$DATA" = all ]; then
    SCANS+=("data/$P/perturbed_scans/*.json")
    for d in data/$P/perturbed/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
    PRE=(--prechecks data/$P/perturbed/prechecks)
fi
if [ "$DATA" = l2 ]; then  # natural + perturbed + level 2, kept apart from "all"
    SCANS+=("data/$P/perturbed_scans/*.json" "data/$P/perturbed_l2_scans/*.json")
    for d in data/$P/perturbed/task* data/$P/perturbed_l2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
    PRE=(--prechecks data/$P/perturbed/prechecks data/$P/perturbed_l2/prechecks)
fi
python scripts/06_train_predictor.py --scans "${SCANS[@]}" --episodes "${EPS[@]}" "${PRE[@]}" $ARGS --out results/$P/$NAME
