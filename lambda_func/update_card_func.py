import datetime
import json
import boto3
import botocore.exceptions
from boto3.session import Session

def lambda_handler(event, context):
    region = "ap-northeast-1"
    session = Session(
        region_name=region
    )
    dynamodb = session.resource('dynamodb')

    anki_table_name = ''
    anki_table = dynamodb.Table(anki_table_name)
    
    content_name = []
    for sub_event in event:
        data = sub_event
        stamp = 0
        next_date = 0
        consecutive = 0
        state = 0
        
        if state == 1:
            consecutive += 1
        elif state != 0:
            consecutive = 0
        
        one_day_interval = 24 * 60 * 60
        if consecutive < 4:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp())
        elif consecutive < 9:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp()) + 1 * one_day_interval
        elif consecutive < 13:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp()) + 6 * one_day_interval
        else:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp()) + 30 * one_day_interval
        
        anki_table.update_item(
            Key={
                content_name[0]: stamp,
            },
            UpdateExpression=f"set {content_name[1]}=:r, {content_name[2]}=:p",
            ExpressionAttributeValues={
                ':r': next_date,
                ':p': consecutive
            },
            ReturnValues="UPDATED_NEW"
        )

    json_data = {'result':'200'}
    return json.dumps(json_data)
