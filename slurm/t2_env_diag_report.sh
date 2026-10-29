source slurm/common.sh
for P in pi0 pi05; do python scripts/26_pi_diag_table.py --dir results/$P/diag --out results/$P/diag.md; done
echo "| $(date +%F) | Track 2 env diagnosis: lerobot-eval (default settings) for pi0 and pi05, tasks 0 and 8, initial states 0 to 9, in our env, LeRobot's documented env (hf-libero 0.1.4, robosuite 1.4.0, bddl 1.0.1, mujoco 3.3.0) and the same with mujoco 2.3.7 (PI_ENV in slurm/common_pi.sh); 26_pi_diag_table.py | $(git rev-parse --short HEAD) | results/pi0/diag.md, results/pi05/diag.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "pi0/pi05: env diagnosis tables"
