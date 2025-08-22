mkdir opencompass/opencompass/configs/models/rlreasoner
mkdir opencompass/opencompass/custom
cp rlreasoner_config.py opencompass/opencompass/configs/models/rlreasoner/
cp rlreasoner.py opencompass/opencompass/models/
source ~/.bashrc
module load CUDA/12.2.2
conda activate rlreasoner
cd opencompass
python run.py \
  -a vllm \
  --models rlreasoner_config \
  --datasets gsm8k_gen \
  --debug
  #bbh_gen
