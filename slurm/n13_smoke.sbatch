#!/bin/bash
#SBATCH --job-name=n13-smoke
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
# Smoke test of 60_regression.py and 61_regression_report.py (2 epochs, held-out task 0, pi05 and oft), output in data/regression_v2_smoke.
source slurm/common.sh
export OMP_NUM_THREADS=8
set -e
for P in pi05 oft; do for M in gru_phys_frac safe_lin safe_mlp safe_lstm gru_physvla_frac baselines; do
  /usr/bin/time -f "$P $M %e s %M KB" python scripts/60_regression.py --policy $P --model $M --held_out 0 --seed 0 --smoke --out data/regression_v2_smoke/$P
done; done
python - <<'P'
import json; d = json.load(open("data/regression_v2_smoke/pi05/gru_phys_frac/s0/g0.json"))
r = [x for x in d["rows"] if not x["success"]][0]; print(d["counts"]); print(r["eid"], r["t50"], r["t70"], r["K"][:5], r["target"][:5], r["pred"][:5])
P
echo smoke ok
