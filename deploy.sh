#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
python train.py 


echo "++++++++++ EXTRACT CREDENTIALS ++++++++++"
sh ./generate_credentials.sh > credentials.yml


echo "++++++++++ STARTING SERVER ++++++++++"
python rasa run
