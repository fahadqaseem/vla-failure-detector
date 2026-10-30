#!/bin/bash
# Commit and push results/week2 and the LOG from a job (Fahad, Oct 23: report jobs push themselves).
# Only results/week2, week3, pi0, pi05 and results/LOG.md; files over 50 MB are left out. One retry, then give up (logged).
MSG=${1:-"week2 results"}
cd "$SLURM_SUBMIT_DIR"
LOCK=.git/w2_push.lock  # several jobs share this checkout: one git at a time (mkdir is atomic)
for i in $(seq 1 120); do mkdir $LOCK 2>/dev/null && break; sleep 5; done
trap 'rmdir $LOCK 2>/dev/null' EXIT
find results/week2 results/week3 results/pi0 results/pi05 -type f -size +50M 2>/dev/null -printf "too big, not committed: %p\n"
git add $(find results/week2 results/week3 results/pi0 results/pi05 -type f -size -50M 2>/dev/null) results/LOG.md 2>/dev/null
git -c user.name="Fahad Qaseem Khawar" commit -qm "$MSG" || { echo "nothing to commit"; exit 0; }
for try in 1 2; do
    git pull -q --rebase --autostash origin main && git push -q origin main && { echo "pushed: $MSG"; exit 0; }
done
echo "PUSH FAILED: $MSG" | tee -a results/week2/push_failures.txt
