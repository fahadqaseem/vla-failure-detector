# Running on WSU Grid

Status: to be filled in while setting up (Oct 17-18). Record every working command here.

Known so far:
- Slurm cluster; L40S GPUs (H200 available).
- Headless rendering needs `MUJOCO_GL=egl` and `PYOPENGL_PLATFORM=egl`.
- Job templates in `slurm/` (partition and conda env are TODO).
- Never run the model on the login node. Use `sbatch` or an interactive GPU session.
- Run Claude Code CLI in the Grid terminal (over VS Code Remote-SSH the extension panel is less reliable).

To fill in: login host, partition names, GPU request syntax, module names (cuda, conda),
scratch/storage paths and quotas, Hugging Face cache location, time limits.
