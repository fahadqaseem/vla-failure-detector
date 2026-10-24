#!/bin/bash
#SBATCH --job-name=t2-env
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 feasibility (Oct 23): a separate env "pi" for Pi0 / Pi0.5 (LeRobot PyTorch ports) next to our LIBERO stack.
# CentOS 7 has glibc 2.17, so only manylinux2014 wheels work: torch 2.6.0+cu124 (torchvision 0.21, required by lerobot 0.4.4).
set -x
# Not every node has Lmod / conda: make a venv from the openvla-oft env's Python 3.10 instead.
ENV=$HOME/envs/pi
[ -d $ENV ] || $HOME/.conda/envs/openvla-oft/bin/python -m venv $ENV
source $ENV/bin/activate
pip install -q --upgrade pip
export PIP_CACHE_DIR=/wsu/tmp/hr4625/pip
pip install torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124 || exit 1
# lerobot without its deps: av 15 and torchcodec have no glibc 2.17 wheels (video datasets only, not needed for
# inference); pynput, rerun-sdk and wandb (no 2.17 wheel either) are for teleop, visualisation and training logs. The rest of its requirements, then the "pi" extra.
pip install lerobot==0.4.4 --no-deps || exit 1
pip install "datasets>=4.0.0,<5.0.0" "diffusers>=0.27.2,<0.36.0" "huggingface-hub[cli,hf-transfer]>=0.34.2,<0.36.0" \
    "accelerate>=1.10.0,<2.0.0" "setuptools>=71,<81" "einops>=0.8.0,<0.9.0" "opencv-python-headless>=4.9.0,<4.12.0" \
    "jsonlines>=4,<5" "packaging>=24.2,<26" "pyserial>=3.5,<4" "draccus==0.10.0" "gymnasium>=1.1.1,<2" \
    "deepdiff>=7.0.1,<9" "imageio[ffmpeg]>=2.34.0,<3" "termcolor>=2.4.0,<4" \
    "torch==2.6.0" "torchvision==0.21.0" "scipy>=1.10.1,<1.15" "tokenizers>=0.21,<0.22" "safetensors>=0.4.3" regex \
    --only-binary=:all: || exit 1   # wheels only: pip falls back to versions that still have glibc 2.17 wheels
pip install --no-deps "transformers @ git+https://github.com/huggingface/transformers.git@fix/lerobot_openpi" || exit 1
pip install robosuite==1.4.1 mujoco==3.3.0 bddl==3.6.0 easydict==1.13 gym==0.26.2 "numpy<2" numba==0.60.0 llvmlite==0.43.0 --prefer-binary || exit 1
pip install --force-reinstall --no-deps --only-binary=:all: pillow || exit 1
pip install --only-binary=:all: "matplotlib<3.10" || exit 1   # LIBERO env_wrapper imports matplotlib (found Oct 24)
pip install --no-deps --only-binary=:all: av==14.0.1 || exit 1   # lerobot imports av at import time; 14.0.1 is the last 2.17 wheel (we never decode video)
pip check | head -20
pip install -e $HOME/LIBERO --no-deps || exit 1
pip list 2>/dev/null | grep -iE "^(torch|torchvision|transformers|lerobot|numpy|mujoco|robosuite|libero|av|gymnasium) "
python -c "import torch; print('torch', torch.__version__, torch.version.cuda); from lerobot.policies.pi0.modeling_pi0 import PI0Policy; from lerobot.policies.pi05.modeling_pi05 import PI05Policy; import robosuite, libero.libero; print('IMPORTS OK')"
