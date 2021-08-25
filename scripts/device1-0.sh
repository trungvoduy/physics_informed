#! /bin/bash
CUDA_VISIBLE_DEVICES=1 python3 run_pino3d.py \
--config_path configs/transfer/Re100to250-1s.yaml \
--start 0 \
--stop 40 \
--log;
CUDA_VISIBLE_DEVICES=1 python3 run_pino3d.py \
--config_path configs/transfer/Re200to250-1s.yaml \
--start 0 \
--stop 40 \
--log;
CUDA_VISIBLE_DEVICES=1 python3 run_pino3d.py \
--config_path configs/transfer/Re250to250-1s.yaml \
--start 0 \
--stop 40 \
--log;
