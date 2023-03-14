# Required libraries
import boto3
import os

# Import AWS credentials from aws_secret_key.py
from aws_secret_key import access_key, secret_access_key

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

for files in os.listdir():   
    if '.json' in files:
        upload_file_bucket = '<bucket_name>'
        upload_file_key = 'JSON_files/' + str(files)
        client.upload_file(files, upload_file_bucket, upload_file_key)
