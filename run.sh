cp rlreasoner.py opencompass/opencompass/models/
mkdir opencompass/opencompass/configs/models/rlreasoner
cp rlreasoner_config.py opencompass/opencompass/configs/models/rlreasoner/
source ~/.bashrc
module load CUDA/12.2.2
conda activate rlreasoner
cd opencompass
python run.py \
  --models rlreasoner \
  --datasets gsm8k_gen bbh_gen
