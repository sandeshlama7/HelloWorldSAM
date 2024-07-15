import json, boto3, os

def lambda_handler(event, context):
    return{
        "statusCode": 200,
        "body": "Hello hello, Is there anybody in here?"
    }
