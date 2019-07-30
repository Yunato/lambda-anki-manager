import datetime
import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    region = ""
    session = Session(
            region_name=region
    )
    dynamodb = session.resource('dynamodb')

    table_name = ''
    table = dynamodb.Table(table_name)

    query_key = ''
    stamp = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp())
    fe = Key(query_key).lte(stamp)
    
    scan_response = table.scan(
        FilterExpression=fe
    )

    sort_key = ''
    scan_response['Items'] = sorted(scan_response['Items'], key=lambda x:x[sort_key], reverse=False)
    return scan_response


