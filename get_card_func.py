import boto3
from boto3.session import Session

def lambda_handler(event, context):
    region = "ap-northeast-1"
    session = Session(
            region_name=region
    )
    dynamodb = session.resource('dynamodb')

    table_name = ''
    table = dynamodb.Table(table_name)

    primary_key = ''
    scan_response = table.scan()
    scan_response['Items'] = sorted(scan_response['Items'], key=lambda x:x[primary_key], reverse=True)
    return scan_response
