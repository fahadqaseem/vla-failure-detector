# Sourced by Track 2 jobs (Pi0 / Pi0.5): the separate env ~/envs/pi (slurm/t2_env.sbatch), LIBERO on the path.
source $HOME/envs/pi/bin/activate
export PYTHONPATH="$HOME/LIBERO:$SLURM_SUBMIT_DIR${PYTHONPATH:+:$PYTHONPATH}"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export CUBLAS_WORKSPACE_CONFIG=:4096:8
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"
export PNR_POLICY=${PNR_POLICY:-pi0}
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs
