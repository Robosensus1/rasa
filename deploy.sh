#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
python rasa train


echo "++++++++++ EXTRACT CREDENTIALS ++++++++++"
sh ./generate_credentials.sh > credentials.yml


echo "++++++++++ STARTING SERVER ++++++++++"
python rasa run
