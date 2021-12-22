import json
import boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TO DO implement
    print(event)
    
    # Print S3 bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)
    
    # Print .json filename
    json_file = event['Records'][0]['s3']['object']['key']
    print(json_file)
    
    # Print file objects(metadata) of json_file
    json_file_obj = s3_client.get_object(Bucket=bucket, Key=json_file)
    print(json_file_obj)
    
    # Print the file content
    lines = json_file_obj['Body'].read().decode('utf-8').split()
    print(lines)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }