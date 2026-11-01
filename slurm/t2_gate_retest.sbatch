#!/bin/bash
#SBATCH --job-name=t2-gate-retest
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 (Fahad, Nov 1): tasks whose gate failed on e00 get the same gate on e01 (query 1 and the middle query, full
# replay, 10 mm limit). Pass -> GATE_PASS, and GATE_FAIL is kept as GATE_FAIL_e00. Fail -> GATE_FAIL stays. Output in results/$P/gate_retest.
source slurm/common_pi.sh
source slurm/t2_fail.sh
T=$(printf "%02d" $SLURM_ARRAY_TASK_ID)
D=data/$PNR_POLICY/natural/task$T
EP=$D/t${T}_e01_n0.npz
R=results/$PNR_POLICY/gate_retest
mkdir -p $R
: > $R/task$T.txt
for Q in 1 -1; do
    echo "=== $EP query $Q" | tee -a $R/task$T.txt
    python scripts/02_replay_test.py --episode "$EP" --query $Q --steps 80 --full > $R/.task$T.out
    rc=$?
    grep -E "^(restore query|replayed|full replay|PASS|FAIL)" $R/.task$T.out | tee -a $R/task$T.txt
    rm -f $R/.task$T.out
    if [ $rc != 0 ]; then
        echo "e01 query $Q failed too" >> $D/GATE_FAIL; echo "retest FAILED for task $T"; exit 0
    fi
done
mv $D/GATE_FAIL $D/GATE_FAIL_e00
touch $D/GATE_PASS
