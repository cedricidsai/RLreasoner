# rlreasoner_config.py
from opencompass.models.rlreasoner import RLReasoner
from opencompass.models import HuggingFaceCausalLM
import os



# Define the underlying base model (example: LLaMA-7B from HF)
base_model = dict(
    type=HuggingFaceCausalLM,
    path='meta-llama/Llama-2-7b-hf',
    max_out_len=512,
)

# Wrap our AGI around the base model
models = [
    dict(
        abbr='rlreasoner',
        type='HuggingFaceCausalLM',
        path='meta-llama/Llama-2-7b-hf',
        # model=base_model,
        model_kwargs={'token':os.environ['TOKEN'],'device':'auto'},
        max_out_len=512,
    )
]
#        max_steps=3,

