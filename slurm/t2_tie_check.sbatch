#!/bin/bash
#SBATCH --job-name=t2-tie-check
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 (Oct 26): 24_pi_tie_check.py; OK -> cancel the dead pi0 jobs and rerun t2_start.sh pi0, else results/pi0/BLOCKED.md.
source slurm/common_pi.sh
C=$(git rev-parse --short HEAD)
OUT=$(python scripts/24_pi_tie_check.py 2>&1); RC=$?
LINES=$(echo "$OUT" | grep -E '^(make_task|embed_tokens)' | tr '\n' ' ')
if [ $RC = 0 ]; then
    scancel 40783643 40784661 2>/dev/null
    J=$(bash slurm/t2_start.sh pi0)
    echo "| $(date +%F) | Track 2 pi0 pre-check (24_pi_tie_check.py, job $SLURM_JOB_ID): $LINES TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1 in slurm/common_pi.sh. Cancelled 40783643, 40784661; t2_start.sh pi0: ${J#* T2 pi0 } | $C | resubmitted | auto |" >> results/LOG.md
    bash slurm/w2_push.sh "pi0: pre-check OK, chain resubmitted"
else
    mkdir -p results/pi0
    { echo "# Pi0 blocked ($(date +%F), job $SLURM_JOB_ID)"; echo; echo '```'; echo "$OUT" | grep -vi warn | tail -20; echo '```'; } > results/pi0/BLOCKED.md
    echo "| $(date +%F) | Track 2 pi0 pre-check FAILED (job $SLURM_JOB_ID): $LINES | $C | results/pi0/BLOCKED.md | auto; chain not resubmitted |" >> results/LOG.md
    git add results/pi0/BLOCKED.md
    bash slurm/w2_push.sh "pi0: BLOCKED"
fi
