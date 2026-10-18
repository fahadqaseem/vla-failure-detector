#!/bin/bash
#SBATCH --job-name=pnr-onset
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Automatic t_onset from saved sim states (CPU only), plus t_onset - t_pnr for scanned failures.
source slurm/common.sh
python scripts/07_auto_onset.py --episodes "data/natural/*/*.npz" --scans "data/full_scans/*.json" --out results/auto_onset.csv
