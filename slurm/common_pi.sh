# Sourced by Track 2 jobs (Pi0 / Pi0.5): the separate env ~/envs/pi (slurm/t2_env.sbatch), LIBERO on the path.
# PI_ENV (Oct 29 diagnosis): pi (default; ~/LIBERO, robosuite 1.4.1, mujoco 3.3.0), pi_hf (LeRobot's documented
# hf-libero 0.1.4, robosuite 1.4.0, bddl 1.0.1, mujoco 3.3.0) or pi_hf237 (same with mujoco 2.3.7); both on top of ~/envs/pi.
PI_ENV=${PI_ENV:-pi}
source $HOME/envs/$PI_ENV/bin/activate
if [ "$PI_ENV" = pi ]; then
    export PYTHONPATH="$HOME/LIBERO:$SLURM_SUBMIT_DIR${PYTHONPATH:+:$PYTHONPATH}"
else
    export PYTHONPATH="$SLURM_SUBMIT_DIR"
    export LIBERO_CONFIG_PATH=$HOME/.libero_$PI_ENV
fi
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export CUBLAS_WORKSPACE_CONFIG=:4096:8
export TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1  # torch 2.6: LIBERO init-state files (official repo) hold numpy arrays
export TORCHDYNAMO_DISABLE=1  # no torch.compile (inductor gcc build fails on CentOS 7, Oct 26)
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"
export PNR_POLICY=${PNR_POLICY:-pi0}
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs
