# Running on WSU Grid

Status: env built and `slurm/check.sbatch` passes on an L40S (Oct 17). Record every working command here.

## Official WSU rules for VS Code (KB article "How to SSH to the Grid in Visual Studio Code",
https://services.wayne.edu/TDClient/277/Portal/KB/ArticleDet?ID=20349)

- Login host: `grid.wayne.edu` (login node "Warrior"), user = WSU AccessID, password = AccessID password.
- NEVER connect VS Code to Warrior. Warrior is for light work only; heavy processes are killed.
  VS Code must connect to a COMPUTE NODE through a jump config:
  1. On the Grid (plain ssh or Grid OnDemand > Clusters > HPC Grid Access): add the
     "VSCode compatibility setup" block from the KB article to ~/.bashrc (sets
     VSCODE_SERVER_CUSTOM_GLIBC_LINKER, VSCODE_SERVER_CUSTOM_GLIBC_PATH,
     VSCODE_SERVER_PATCHELF_PATH=/wsu/apps/vscode/patchelf/0.19.1/bin/patchelf), then `source ~/.bashrc`.
  2. Copy the Grid key ~/.ssh/id_ed25519 to the Mac as ~/.ssh/id_ed25519_<AccessID> (chmod 600).
  3. On the Grid run `/wsu/apps/scripts/generate_vscode_ssh_jump_config.sh`; copy the generated
     `vscode_ssh_config` into the Mac's ~/.ssh/config.
  4. On the Grid: `cp /wsu/el7/scripts/tutorial/vscode_job .` then `sbatch vscode_job`; find the node
     in the NODELIST column of `qme`. If you change the job time limit, change its `sleep` too.
  5. VS Code: Cmd+Shift+P > Remote-SSH: Connect to Host > the node name.
- Compute nodes have internet (pypi.org and huggingface.co answer HTTP 200 from mdt83), so pip,
  Hugging Face downloads and Claude Code work on the VS Code node.

## Facts (checked Oct 17, 2026 from CPU node mdt83)

- User `hr4625`, home `/wsu/home/hr/hr46/hr4625`, Slurm account `wsu`.
  QoS available: debug, express, gpu, highmem, primary, requeue, secondary.
- OS on all nodes (GPU nodes too): CentOS 7.9, glibc 2.17. Many new pip wheels need glibc 2.28
  and pip then silently builds from source. Install with `--only-binary :all:` and pin older
  versions that still ship `manylinux2014` / `manylinux_2_17` wheels (pins in results/LOG.md).
- GPU partitions (QoS must be `gpu`; no partition time limit, QoS gpu caps jobs at 30 days):

  | partition | GPUs | nodes | request |
  |---|---|---|---|
  | `galhp` | 4x L40S 46 GB per node | alh1-alh6 (64 CPUs, 750 GB RAM) | `-p galhp -q gpu --gres=gpu:nvidia_l40s:1` |
  | `gmsap` | 4x H200 per node | msa1-msa4 (128 CPUs, 750 GB RAM) | `-p gmsap -q gpu --gres=gpu:nvidia_h200:1` |
  | `reqp` | mixed, preemptible (jobs get requeued) | many | `-p reqp -q requeue` |

  On Oct 17 alh1-5 and msa1 were draining; only alh6 took L40S jobs. Check with
  `sinfo -p galhp,gmsap -N -o "%N %G %t"`. To switch to H200, edit the two lines in each sbatch.
- GPU driver 580.119.02 (CUDA 13.0) on alh6. The torch 2.2.0+cu121 wheel brings its own CUDA,
  so no `module load cuda` is needed.
- Modules: `cuda/11.8` to `cuda/12.4` (default), `python/2.7` to `python/3.11`, `gnu7` (gcc 7.3.0,
  loaded by default), `gnu9/9.1.0`, `apptainer/1.2.2`, `singularity` (also in /usr/bin).
  Apptainer is the fallback if glibc 2.17 ever blocks a package.
- Conda: the system conda 22.9 from `module load python/3.7`. Our env `openvla-oft` (Python 3.10)
  lives in `~/.conda/envs/openvla-oft` (about 15 GB). `slurm/common.sh` loads and activates it.
- Repos: `~/vla-failure-detector`, `~/openvla-oft` (e4287e9), `~/LIBERO` (8f1084e).
  LIBERO config: `~/.libero/config.yaml` (defaults).

## Storage

- Home quota: 4000 GB (`wsuquota`, Oct 17: 39.23 GB used, 110,992 files). Check usage with
  `wsuquota`; `df` (47 GB) and `quota` (empty) are misleading here.
- `HF_HOME=~/.cache/huggingface`. Checkpoint `moojink/openvla-7b-oft-finetuned-libero-10`,
  revision 95220f9, is 19 GB there.
- Scratch: only `/wsu/tmp` (shared, world-writable, same filesystem, may be purged). Used for the
  pip cache only: `PIP_CACHE_DIR=/wsu/tmp/hr4625/pip`. No `/scratch` or project space found.
- With 4 TB in home, rollouts, hidden features and scans can all stay in `data/` under the repo.

## Jobs

- Templates in `slurm/` use `galhp`, QoS `gpu`, one L40S. Output goes to `logs/` (git-ignored).
- `sbatch slurm/check.sbatch` prints `nvidia-smi`, then runs `00_check_env.py` (about 3 min;
  model load about 100 s because 15 GB is read from home).
- `ARGS="--tasks 0 --episodes 1" sbatch slurm/collect.sbatch` (default: 10 tasks x 3 episodes).
- `EP=data/rollouts/<id>.npz sbatch slurm/replay.sbatch`.
- `squeue -u $USER` before resubmitting. Never run the model on the login node.
- Headless rendering: `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl` (set in common.sh; works on alh6).
- Run Claude Code CLI in the Grid terminal (over VS Code Remote-SSH the extension panel is less reliable).

## Discovery commands (rerun to check)

```bash
sinfo -o "%P %G %l %D %a"
sacctmgr -nP show assoc user=$USER format=account,partition,qos
sacctmgr -nP show qos format=name,maxwall,maxtrespu
scontrol show partition galhp
module avail 2>&1 | grep -iE "cuda|python|gcc|gnu|apptainer"
wsuquota
du -sh ~/.conda/envs/* ~/.cache/huggingface
```
