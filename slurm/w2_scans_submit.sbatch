#!/bin/bash
#SBATCH --job-name=w2-scans-submit
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:20:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase A: scan list (new failures whose pre-check says "scan"), the full-scan array on it (at most 3 at
# once), then the K 16 refinement step after it. The number of scans is only known here, so this job submits them.
source slurm/common.sh
T=results/week2/scans/targets.txt
python scripts/scan_targets.py --root data/perturbed_v2 --n_success 0 --prechecks data/perturbed_v2/prechecks --out $T
N=$(grep -c . $T)
DEP=""
if [ "$N" -gt 0 ]; then
    SCAN=$(sbatch --parsable --job-name=w2-scan --array=0-$((N - 1))%3 --mail-type=FAIL \
        --export=ALL,TARGETS=$T,OUT=data/perturbed_v2_scans slurm/scan_array.sbatch)
    echo "scan array $SCAN ($N targets)"; DEP="--dependency=afterany:$SCAN"
fi
sbatch $DEP slurm/w2_refine_submit.sbatch
bash slurm/w2_push.sh "week2: scan list"
