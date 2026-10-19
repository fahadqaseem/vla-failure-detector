"""Task embedding for the task-conditioned predictor (Fahad, Oct 19 2026, experiment for unseen tasks).

One vector per LIBERO-10 task: the mean of the VLA's last-layer LLM hidden states over the tokens of the
task instruction. Text only: the policy's prompt "In: What action should the robot take to {task}?\\nOut:"
goes through the fine-tuned Llama backbone of OpenVLA-OFT without image or proprio tokens, so the vector
depends on the task alone (the same for every episode and step of a task). Runs on CPU (no simulator).
Output: one npz with emb (10, 4096) float32 and the 10 instructions.

python scripts/11_task_embedding.py --episodes "data/natural/*/*.npz" --out data/task_embedding.npz
"""

import argparse
import glob
import os
import sys

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pnr.sim import DEVICE, Policy  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", default=["data/natural/*/*.npz"])
p.add_argument("--out", default="data/task_embedding.npz")
args = p.parse_args()

# The instruction of each task, from the first recorded episode of that task.
instructions = {}
for f in sorted(f for pat in args.episodes for f in glob.glob(pat)):
    ep = np.load(f, allow_pickle=True)
    instructions.setdefault(int(ep["task_id"]), str(ep["description"]))
tasks = sorted(instructions)

policy = Policy()
tokenizer = policy.processor.tokenizer
emb = np.zeros((len(tasks), 4096), np.float32)
for i, t in enumerate(tasks):
    text = instructions[t].lower()
    prompt = f"In: What action should the robot take to {text}?\nOut:"  # as in openvla-oft get_vla_action
    enc = tokenizer(prompt, return_offsets_mapping=True, return_tensors="pt")
    start, end = prompt.index(text), prompt.index(text) + len(text)
    offsets = enc.pop("offset_mapping")[0]
    is_instruction = (offsets[:, 1] > start) & (offsets[:, 0] < end)  # tokens that overlap the instruction text
    with torch.no_grad():
        out = policy.model.language_model(input_ids=enc["input_ids"].to(DEVICE), output_hidden_states=True)
    hidden = out.hidden_states[-1][0].float().cpu()
    emb[i] = hidden[is_instruction].mean(0).numpy()
    tokens = tokenizer.convert_ids_to_tokens(enc["input_ids"][0][is_instruction])
    print(f"task {t}: {int(is_instruction.sum())} instruction tokens {tokens}; norm {np.linalg.norm(emb[i]):.2f}", flush=True)

norm = emb / np.linalg.norm(emb, axis=1, keepdims=True)
print("cosine similarity between tasks:\n" + np.array2string(norm @ norm.T, precision=2))
np.savez(args.out, emb=emb, task_ids=np.array(tasks), instructions=np.array([instructions[t] for t in tasks]))
print("saved", args.out)
