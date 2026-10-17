# Running on WSU Grid

Status: to be filled in while setting up (Oct 17-18). Record every working command here.

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
- Open question: whether compute nodes have internet (needed for pip, Hugging Face downloads and
  Claude Code). Check with `curl -sI https://pypi.org | head -1` on the node.

Known so far:
- Slurm cluster; L40S GPUs (H200 available).
- Headless rendering needs `MUJOCO_GL=egl` and `PYOPENGL_PLATFORM=egl`.
- Job templates in `slurm/` (partition and conda env are TODO).
- Never run the model on the login node. Use `sbatch` or an interactive GPU session.
- Run Claude Code CLI in the Grid terminal (over VS Code Remote-SSH the extension panel is less reliable).

To fill in: login host, partition names, GPU request syntax, module names (cuda, conda),
scratch/storage paths and quotas, Hugging Face cache location, time limits.
