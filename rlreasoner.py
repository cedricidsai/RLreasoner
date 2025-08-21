# rlreasoner.py
import random
from opencompass.models.base import BaseModel
from opencompass.registry import MODELS

@MODELS.register_module(name='rlreasoner.RLReasoner')
class RLReasoner(BaseModel):
    """A minimal RL reasoning agent that:
       - receives a prompt
       - simulates reasoning via a loop
       - queries an underlying model (passed in config)
    """

    def __init__(self, model, max_steps=3, **kwargs):
        super().__init__()
        self.model = model      # underlying LLM backend (e.g. HF or API)
        self.max_steps = max_steps

    def generate(self, prompts, **kwargs):
        outputs = []
        for prompt in prompts:
            # RL-style loop (simplified for now)
            state = prompt
            trace = []
            for step in range(self.max_steps):
                # simulate "thinking step"
                action = f"think_step_{step}"
                trace.append(action)

            # final answer = just delegate to underlying model
            answer = self.model.generate([state], **kwargs)[0]
            outputs.append(answer)

            # (Optional) log trace if you want to inspect later
            print(f"[TRACE] {trace} → {answer}")
        return outputs


from opencompass.registry import MODELS
print(MODELS)
print(MODELS.module_dict.keys())