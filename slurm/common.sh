# Sourced by every job.
# No module load cuda: the pip torch wheel (2.2.0+cu121) ships its own CUDA runtime.
if type module >/dev/null 2>&1; then
    module load python/3.7       # provides the system conda (22.9); env lives in ~/.conda/envs
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate openvla-oft
else  # some nodes have no Lmod (mdt20, Oct 20 2026): use the env's python directly
    export PATH="$HOME/.conda/envs/openvla-oft/bin:$PATH"
fi
export OFT_ROOT="$HOME/openvla-oft"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export CUBLAS_WORKSPACE_CONFIG=:4096:8   # deterministic cuBLAS (pnr/sim.py, Fahad Oct 19)
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"   # home; quota not yet confirmed (checkpoint ~15 GB)
cd "$SLURM_SUBMIT_DIR"
mkdir -p logs
