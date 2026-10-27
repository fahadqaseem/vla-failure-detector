#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=3-00:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# One 06_train_predictor.py run (copy in pnr_probe/, unchanged) on all data (DATA=all of slurm/w2_train.sbatch:
# natural + perturbed 7 tasks + perturbed_v2 gate-pass tasks, refined labels), with --phys = one feature set.
# Env: PHYS (feature dir), NAME (output in pnr_probe/results/), ARGS (extra flags).
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
D=$HOME/vla-failure-detector/data
EPS=("$D/natural/*/*.npz" "$D/perturbed/task0[0145678]/*.npz")
for d in $D/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS+=("$d/*.npz"); done
python pnr_probe/06_train_predictor.py --scans "$D/full_scans/*.json" "$D/perturbed_scans/*.json" "$D/perturbed_v2_scans/*.json" \
    --episodes "${EPS[@]}" --prechecks $D/perturbed/prechecks $D/perturbed_v2/prechecks --refine $D/week2_refine \
    --phys $PHYS --alphas 0.025 0.05 0.10 0.20 --models progress mlp_phys mlp_phys_cusum gru_phys gru_phys_cusum \
    $ARGS --out pnr_probe/results/$NAME
