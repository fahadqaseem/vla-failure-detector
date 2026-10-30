#!/bin/bash
#SBATCH --job-name=b3-train
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 3 baselines (Fahad, Oct 30): one held-out group per array task, data, labels and thresholds as T1all (DATA=all).
# SPLIT=unseen (array 0-9, one task each) or seen (array 0-4, one episode fold each). Preempted tasks restart from the top.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
G=$SLURM_ARRAY_TASK_ID
SP=""; [ "$SPLIT" = seen ] && SP="--split episode"
SCANS=("data/full_scans/*.json" "data/perturbed_scans/*.json" "data/perturbed_v2_scans/*.json")
EPS=("data/natural/*/*.npz" "data/perturbed/task0[0145678]/*.npz")
for d in data/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
python scripts/06_train_predictor.py --scans "${SCANS[@]}" --episodes "${EPS[@]}" \
    --prechecks data/perturbed/prechecks data/perturbed_v2/prechecks --refine data/week2_refine \
    --alphas 0.025 0.05 0.10 0.15 0.20 0.25 --models progress timer safe hideseek $SP --only_group $G \
    ${ARGS:-} --out ${ROOT:-results/week3/baselines}/$SPLIT/g$G
