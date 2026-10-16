# Sourced by every job. Fill in the TODOs once (Claude Code can do it after running `sinfo` and `module avail`).
# module load cuda            # TODO: only if Grid needs it
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate openvla-oft    # TODO: your env name
export OFT_ROOT="$HOME/openvla-oft"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"   # TODO: point to scratch if home quota is small (checkpoint ~15 GB)
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs
