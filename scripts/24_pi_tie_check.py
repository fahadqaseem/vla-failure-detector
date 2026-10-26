"""Track 2 pre-check (Oct 26): make_task(0) loads LIBERO init states, and Pi0's embed_tokens (reported "missing" when
the checkpoint loads) is the same tensor as another loaded weight, not random. Prints one line; exit 0 = OK."""
import sys

from lerobot.policies.pi0.modeling_pi0 import PI0Policy

from pnr.sim_pi import CHECKPOINT, make_task

env, desc, inits = make_task(0)
print(f"make_task(0) OK: {desc} | {len(inits)} init states")
m = PI0Policy.from_pretrained(CHECKPOINT).eval()
emb = m.model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight
tied = [n for n, p in m.named_parameters(remove_duplicate=False)
        if p.data_ptr() == emb.data_ptr() and "embed_tokens" not in n]
print(f"embed_tokens {tuple(emb.shape)} tied to: {', '.join(tied) if tied else 'NOTHING (random init)'}")
sys.exit(0 if tied else 1)
