#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
python train.py --nlu --dial





echo "++++++++++ STARTING SERVER ++++++++++"
python -m rasa run 
