import csv
import boto3

#File to take in input from camera detection and compare it with the AWS database
with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'hot_air_baloon.jpg' #replace with current input image

client = boto3.client('rekognition',aws_access_key_id = access_key_id, 
                                    aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes': source_bytes},
                                MaxLabels=10,
                                MinConfidence = 95)

print(response)