#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=12:00:00
#SBATCH --output=pnr_probe/logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# One held-out group (array index) of train_fold.py; MERGE=1 instead merges all folds. Data as DATA=all
# (natural + perturbed 7 tasks + perturbed_v2 gate-pass tasks, refined labels). Env: PHYS, NAME, ARGS.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
D=$HOME/vla-failure-detector/data
EPS=("$D/natural/*/*.npz" "$D/perturbed/task0[0145678]/*.npz")
for d in $D/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
if [ "${MERGE:-0}" = 1 ]; then G="--merge"; else G="--only_group $SLURM_ARRAY_TASK_ID"; fi
python pnr_probe/micro_phys/train_fold.py --scans "$D/full_scans/*.json" "$D/perturbed_scans/*.json" "$D/perturbed_v2_scans/*.json" \
    --episodes "${EPS[@]}" --prechecks $D/perturbed/prechecks $D/perturbed_v2/prechecks --refine $D/week2_refine \
    --phys $PHYS --alphas 0.025 0.05 0.10 0.20 --models progress gru_phys gru_phys_cusum $ARGS $G \
    --out pnr_probe/results/micro_phys/$NAME
