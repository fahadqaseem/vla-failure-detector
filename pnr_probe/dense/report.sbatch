#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=02:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Dense report: 13_report.py at 2.5% and 5% (unseen, seen), ranking (summary.py), replay pass rates and the primary
# comparison (dense/report.py), then commit and push pnr_probe/results/dense to pnr-probe only.
source slurm/common.sh
R=${OUTR:-pnr_probe/results/dense}
DENSE=${DENSE:-pnr_probe/data/dense}
for split in unseen seen; do
    P=""; for s in a b; do [ -f $R/${split}_$s/per_episode.json ] && P="$P $R/${split}_$s"; done
    for k in "fixed 0.025" "fixed 0.05"; do
        [ -n "$P" ] && python pnr_probe/13_report.py --pred $P --key "$k" --headline "fixed 0.025" "fixed 0.05" --out "$R/${split}_report_${k// /_}.md"
    done
done
python pnr_probe/summary.py --results $R --sets a b --out $R/ranking.md
python pnr_probe/dense/report.py --dense $DENSE --labels pnr_probe/results/unseen_t1/per_episode.json \
    --episodes pnr_probe/dense/all_episodes.txt --results $R --out $R/summary.md
C=$(git rev-parse --short HEAD)
echo "| $(date +%F) | dense report ($R, replays $DENSE) | $C | $R/summary.md, $R/*_report_*.md | job $SLURM_JOB_ID |" >> pnr_probe/results/LOG.md
[ "$(git branch --show-current)" = pnr-probe ] || { echo "not on pnr-probe, not pushing"; exit 1; }
find $R -type f -size +50M -printf "too big, not committed: %p\n"
git add $(find $R -type f -size -50M) pnr_probe/results/LOG.md pnr_probe/dense
git -c user.name="Fahad Qaseem Khawar" commit -qm "pnr_probe: dense report $R

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || echo "nothing to commit"
for try in 1 2; do git push -q -u origin pnr-probe && { echo pushed; exit 0; }; sleep 30; done
echo "PUSH FAILED" | tee -a $R/push_failures.txt
