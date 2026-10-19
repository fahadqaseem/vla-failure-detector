#!/bin/bash
#SBATCH --job-name=pnr-precheck
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --array=0-9
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Pre-check (09_precheck.py) on the perturbed failures of one LIBERO-10 task per array task. Submit with
# afterok on collect_perturbed.sbatch (its replay gate must pass) and after the natural rescan (Fahad, Oct 19).
source slurm/common.sh
T=$(printf "%02d" $SLURM_ARRAY_TASK_ID)
python scripts/09_precheck.py --episodes "data/perturbed/task$T/*.npz" --out data/perturbed/prechecks
