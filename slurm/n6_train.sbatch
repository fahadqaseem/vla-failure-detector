#!/bin/bash
#SBATCH --job-name=n6-train
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 6 plan (results/plan_nov06.md): one held-out group and one model per array task, CPU only. Data and labels as results/week3/regression
# (POL=oft) or results/pi05/regression (POL=pi05). THR 50 / 70 / 80, SPLIT unseen (0-9) / seen (0-4), SEED, EXTRA (e.g. --save_calib).
# Output $OUT/g$G; preempted tasks restart from the top.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
G=$SLURM_ARRAY_TASK_ID
SP=""; [ "$SPLIT" = seen ] && SP="--split episode"
FT=""; [ "$THR" != 50 ] && FT="--fail_thr 0.$((THR / 10))"
if [ "$POL" = oft ]; then
    SCANS=("data/full_scans/*.json" "data/perturbed_scans/*.json" "data/perturbed_v2_scans/*.json")
    EPS=("data/natural/*/*.npz" "data/perturbed/task0[0145678]/*.npz")
    for d in data/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
    D=(--prechecks data/perturbed/prechecks data/perturbed_v2/prechecks --refine data/week2_refine --phys data/physical --robot data/robot_state
       --alphas 0.025 0.05 0.10 0.15 0.20 0.25)
else
    SCANS=("data/pi05/full_scans/*.json" "data/pi05/perturbed_scans/*.json")
    EPS=("data/pi05/natural/*/*.npz")
    for d in data/pi05/perturbed/task?? data/pi05/perturbed/task??_s1; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done  # pre-registered: seeds 0 and 1 (Nov 7: seed 2 of item 6 stays out)
    D=(--prechecks data/pi05/perturbed/prechecks --phys data/pi05/physical --alphas 0.025 0.05 0.10 0.20)
    [ -d data/pi05/robot_state ] && D+=(--robot data/pi05/robot_state)  # written to a temp dir and renamed when complete (n6-pi05-robot)
fi
python scripts/06_train_predictor.py --scans "${SCANS[@]}" --episodes "${EPS[@]}" "${D[@]}" --models $MODEL $SP $FT --seed ${SEED:-0} \
    --only_group $G ${EXTRA:-} --out $OUT/g$G
