#!/bin/bash
# Nov 12 add-one-signal (Fahad): gru_phys_ttp with ONE physical group alone (06 --phys_keep), and each alone OR progress (47_combo.py).
# 70% rule, unseen (leave-one-task-out), seed 0, both policies, CPU only. Regexes avoid glob characters (EXTRA is unquoted in n6_train). Progress and gru_phys_ttp with all groups are rerun here so every
# row uses the same episode set and calibration successes. Output data/single/{oft,pi05}/thr70, report results/single_signals.
cd ~/vla-failure-detector
declare -A KEEP=(
  [goal]='.+_goal_dist .+_in_goal'
  [pose]='.+_pos_. .+_dz .+_lifted .+_tilt'
  [contact]='.+_contact'
  [gripper]='(obj1|obj2|art)_d{0,1}dist grip_open'
)
ids=()
for P in oft pi05; do
  R=data/single/$P/thr70
  sub() { sbatch --parsable --array=0-9 --job-name=n12-$P-$1 --export=ALL,POL=$P,THR=70,SPLIT=unseen,SEED=0,MODEL=$2,OUT=$3,EXTRA="$4" slurm/n6_train.sbatch; }
  ids+=($(sub progress progress $R/progress "--save_calib"))
  ids+=($(sub all gru_phys_ttp $R/all/gru_phys_ttp "--save_calib"))
  for V in goal pose contact gripper; do
    ids+=($(sub $V gru_phys_ttp $R/$V/gru_phys_ttp "--save_calib --phys_keep ${KEEP[$V]}"))
  done
done
dep=$(IFS=:; echo "${ids[*]}")
rep=$(sbatch --parsable --job-name=n12-single-report --dependency=afterok:$dep slurm/n12_single_report.sbatch)
echo "train ${ids[*]} report $rep"
