import datetime
import json
import boto3
import botocore.exceptions
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    region = "ap-northeast-1"
    session = Session(
        region_name=region
    )
    dynamodb = session.resource('dynamodb')

    table_name = ''
    table = dynamodb.Table(table_name)

    content_name = ['']
    query_key = ''
    category = event[content_name[0]]
    fe = Key(query_key).eq(category)
    
    scan_response = table.scan(
        FilterExpression=fe
    )
    
    primary_key = ''
    target = ''
    for response in scan_response['Items']:
        table.update_item(
            Key={
                primary_key: response[''],
            },
            UpdateExpression=f"set {target}=:r",
            ExpressionAttributeValues={
                ':r': 0,
            },
            ReturnValues="UPDATED_NEW"
        )

    json_data = {'result':'200'}
    return json.dumps(json_data)
