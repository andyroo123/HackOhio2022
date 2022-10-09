# HackOhio2022
Our HackOhio Repository

# Packages Needed
pip install opencv-python
pip3 install matplotlib
pip install mediapipe
pip install aws-shell
pip install pyautogui
aws configure (need access key)
pip install pyautogui
pip install gTTs

# AWS Commands
aws rekognition create-collection --collection-id signLanguageRecognition_collection --region us-east-1

aws dynamodb create-table --table-name signLanguageRecognition --attribute-definitions AttributeName=RekognitionId,AttributeType=S --key-schema AttributeName=RekognitionId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --region us-east-1

aws s3 mb s3://signlanguage-images  --region us-east-1

# To Run
.\sim