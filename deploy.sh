#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
python train.py --nlu --dial


echo "++++++++++ EXTRACT CREDENTIALS ++++++++++"
sh ./generate_credentials.sh > credentials.yml


echo "++++++++++ STARTING SERVER ++++++++++"
python rasa run
