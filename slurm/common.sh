# Sourced by every job.
# No module load cuda: the pip torch wheel (2.2.0+cu121) ships its own CUDA runtime.
module load python/3.7       # provides the system conda (22.9); env lives in ~/.conda/envs
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate openvla-oft
export OFT_ROOT="$HOME/openvla-oft"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"   # home; quota not yet confirmed (checkpoint ~15 GB)
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs
