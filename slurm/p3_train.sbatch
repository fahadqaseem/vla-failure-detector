#!/bin/bash
#SBATCH --job-name=p3-train
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Pi0.5 regression at failure thresholds 50, 70, 80% (Fahad, Nov 4): one held-out group and one model per array task, CPU only. Data and labels as
# results/pi05/all_* (DATA=all: natural + gate-passed perturbed incl. seed 1). THR=50 (tau 0.5 rule), 70 or 80; SPLIT=unseen (0-9) or seen (0-4).
# Output data/pi05_reg/thr$THR/$SPLIT/$MODEL/g$G; preempted tasks restart from the top.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
G=$SLURM_ARRAY_TASK_ID
SP=""; [ "$SPLIT" = seen ] && SP="--split episode"
FT=""; [ "$THR" != 50 ] && FT="--fail_thr 0.$((THR / 10))"
EPS=("data/pi05/natural/*/*.npz")
for d in data/pi05/perturbed/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
python scripts/06_train_predictor.py --scans "data/pi05/full_scans/*.json" "data/pi05/perturbed_scans/*.json" --episodes "${EPS[@]}" \
    --prechecks data/pi05/perturbed/prechecks --phys data/pi05/physical --alphas 0.025 0.05 0.10 0.20 --models $MODEL $SP $FT \
    --only_group $G --out data/pi05_reg/thr$THR/$SPLIT/$MODEL/g$G
