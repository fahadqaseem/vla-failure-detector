#!/bin/bash
#SBATCH --job-name=w2-precheck
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --array=0-6%3
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase A: pre-check (09_precheck.py) of one task's new failures, only if its replay gate passed.
source slurm/common.sh
TASKS=(0 1 4 5 6 7 8)
D=data/perturbed_v2/task$(printf "%02d" ${TASKS[$SLURM_ARRAY_TASK_ID]})
if [ ! -f $D/GATE_PASS ]; then echo "no GATE_PASS in $D: skipped"; exit 0; fi
python scripts/09_precheck.py --episodes "$D/*.npz" --out data/perturbed_v2/prechecks
