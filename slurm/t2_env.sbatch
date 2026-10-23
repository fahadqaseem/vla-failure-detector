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
pip install "lerobot[pi]==0.4.4" "torch==2.6.0" "torchvision==0.21.0" || exit 1
pip install robosuite==1.4.1 mujoco==3.3.0 bddl==3.6.0 easydict==1.13 gym==0.26.2 "numpy<2" || exit 1
pip install -e $HOME/LIBERO --no-deps || exit 1
pip list 2>/dev/null | grep -iE "^(torch|torchvision|transformers|lerobot|numpy|mujoco|robosuite|libero|av|gymnasium) "
python -c "import torch; print('torch', torch.__version__, torch.version.cuda); from lerobot.policies.pi0.modeling_pi0 import PI0Policy; from lerobot.policies.pi05.modeling_pi05 import PI05Policy; import robosuite, libero.libero; print('IMPORTS OK')"
