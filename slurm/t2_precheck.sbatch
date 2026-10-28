#!/bin/bash
#SBATCH --job-name=t2-precheck
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --array=0-9
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 pre-check (09_precheck.py, no action noise) of one task's perturbed failures, if its replay gate passed.
source slurm/common_pi.sh
source slurm/t2_fail.sh
D=data/$PNR_POLICY/perturbed/task$(printf "%02d" $SLURM_ARRAY_TASK_ID)
[ -f $D/GATE_PASS ] || { echo "no GATE_PASS in $D"; exit 0; }
python scripts/09_precheck.py --episodes "$D/*.npz" --noise_std 0 --out data/$PNR_POLICY/perturbed/prechecks
