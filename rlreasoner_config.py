# rlreasoner_config.py
from opencompass.models.rlreasoner import RLReasoner
from opencompass.models import HuggingFaceCausalLM
import os


# 'meta-llama/Llama-2-7b-hf'
# Define the underlying base model (example: LLaMA-7B from HF)
base_model = dict(
    type=HuggingFaceCausalLM,
    # path="deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    # path='meta-llama/Llama-2-7b-hf',
    path = 'Qwen/Qwen3-Embedding-0.6B',
    max_out_len=512,
)

# Wrap our AGI around the base model
models = [
    dict(
        abbr='rlreasoner',
        type='HuggingFaceCausalLM',
        path = 'Qwen/Qwen3-Embedding-0.6B',
        # path='meta-llama/Llama-2-7b-hf',
        # path="deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
        # model=base_model,
        model_kwargs={'token':os.environ['HF_TOKEN'], 'device_map':'cuda'},
        max_out_len=512,
    )
]
#        max_steps=3,

