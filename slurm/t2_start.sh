#!/bin/bash
# Track 2 chain for one policy (Oct 23): bash slurm/t2_start.sh pi0   (pi05 is started by pi0's chain)
# checks (GPU) -> feasibility collection, 20 episodes per task (GPU) -> verdict (CPU; on PASS it submits the rest).
set -e
P=$1
F=$(bash slurm/gpu_free.sh)
C=$(sbatch --parsable -J t2-checks-$P --export=ALL,PNR_POLICY=$P slurm/t2_checks.sbatch)
E=$(sbatch --parsable -J t2-collect-$P --array=0-9%$F --dependency=afterok:$C --export=ALL,PNR_POLICY=$P,KIND=natural,START=0,N=20,GATE=0 slurm/t2_collect.sbatch)
V=$(sbatch --parsable -J t2-feasibility-$P --dependency=afterany:$E --export=ALL,P=$P slurm/t2_feasibility.sbatch)
echo "$(date +%F) T2 $P checks $C collect20 $E verdict $V (gpu slots $F)" | tee -a results/week2/jobs.txt
