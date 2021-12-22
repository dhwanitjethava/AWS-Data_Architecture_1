import json

def lambda_handler(event, context):
    # To do Implement
    print(event)
    return {
        'statusCode' : 200,
        'body' : json.dump('Hello from Lambda!')
    }