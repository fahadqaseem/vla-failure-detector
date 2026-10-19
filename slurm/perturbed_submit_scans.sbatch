#!/bin/bash
#SBATCH --job-name=pnr-pscan-submit
#SBATCH --partition=mdtp
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:10:00
#SBATCH --output=logs/%x-%j.out
# Runs after the perturbed collection array (afterany): writes the scan list (failures whose pre-check
# says "scan") and submits the full-scan array on it, one array task per line, at most 4 at once.
source slurm/common.sh
python scripts/scan_targets.py --root data/perturbed --n_success 0 --prechecks data/perturbed/prechecks \
    --out results/perturbed_scans/targets.txt
N=$(grep -c . results/perturbed_scans/targets.txt)
if [ "$N" -eq 0 ]; then echo "nothing to scan"; exit 0; fi
sbatch --array=0-$((N - 1))%4 --export=ALL,TARGETS=results/perturbed_scans/targets.txt,OUT=data/perturbed_scans \
    slurm/scan_array.sbatch
