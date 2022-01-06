# Import AWS credentials from aws_secret_key.py
from aws_secret_key import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

for file in os.listdir('/Users/dhwanitjethava/Desktop/AWS_Data_Pipeline/Dataset/'):
    data = '/Users/dhwanitjethava/Desktop/AWS_Data_Pipeline/Dataset/Employees_3_1.json'

    if '.json' in file:
        upload_file_bucket = 'aws-learning-scaletech'
        upload_file_key = 'JSON_files/' + str(data)
        client.upload_file(data, upload_file_bucket, upload_file_key)
    else:
        print('Error: File is not found!')
