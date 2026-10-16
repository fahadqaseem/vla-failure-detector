# Setup: VS Code + Claude Code on your MacBook (Grid later)

## 0. Can this Mac run it?

Apple menu > About This Mac. You need **Apple Silicon (M1 or newer) and macOS 14+**. Memory: 24 GB is
borderline (the 7B policy alone is about 15 GB). It should load if you quit other apps first, but the
Mac may swap and run slowly. 16 GB will not work; then we go straight to Grid.
About 30 GB of free disk is needed (checkpoint about 15 GB, plus Python packages).

## 1. VS Code + Claude Code (5 minutes)

1. VS Code 1.94 or newer. Install the **Claude Code** extension (publisher: Anthropic, id `anthropic.claude-code`).
2. Needs a paid Claude plan (Pro, Max, Team or Enterprise) or a Console API key. Open the Claude Code
   panel (spark icon) and click Sign in.
3. Unzip `vla-pnr.zip` (for example into `~/Projects/`), then File > Open Folder > `vla-pnr`.
4. Claude Code reads `CLAUDE.md` automatically at the start of each session (check with `/context`).
   `.claude/settings.json` pre-approves safe commands and asks before `rm`, `git push`, `scancel`.
5. Tips: `/plan` (or Shift+Tab in the terminal CLI) makes Claude plan before editing. Type `@` to
   mention a file. Session history button resumes old sessions.

Optional terminal CLI (same sessions/settings): `curl -fsSL https://claude.ai/install.sh | bash`, then `claude`.

## 2. Python environment on the Mac (Claude Code can drive this)

```bash
# Miniforge/conda if you do not have it:  brew install miniforge   (or download Miniforge3-MacOSX-arm64)
conda create -n openvla-oft python=3.10 -y && conda activate openvla-oft
pip install torch torchvision torchaudio                        # macOS wheels include MPS support
git clone https://github.com/moojink/openvla-oft.git ~/openvla-oft && cd ~/openvla-oft && pip install -e .
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git ~/LIBERO && pip install -e ~/LIBERO
pip install -r ~/openvla-oft/experiments/robot/libero/libero_requirements.txt
pip install -r ~/Projects/vla-pnr/requirements-extra.txt
python -c "import torch; print(torch.backends.mps.is_available())"   # must print True
```

- Skip flash-attention (training only, CUDA only).
- `export OFT_ROOT=~/openvla-oft` (add to `~/.zshrc`).
- LIBERO asks for a config path on first import; accept the defaults.
- Do NOT set `MUJOCO_GL` on the Mac. robosuite chooses `cgl` automatically.
- If a package pin fails to install on macOS (tensorflow or dlimp are the usual suspects), have Claude
  Code find the nearest working version and write what changed into results/LOG.md.

## 3. Later: Grid

The `slurm/` folder has job templates. Over VS Code Remote-SSH, run the Claude Code CLI in the remote
terminal (the extension panel is not reliable over Remote-SSH). Install it there with the same curl command.
