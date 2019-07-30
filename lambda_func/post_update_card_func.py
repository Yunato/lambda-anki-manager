import datetime
import json
import boto3
import botocore.exceptions
from boto3.session import Session

def lambda_handler(event, context):
    region = ""
    session = Session(
        region_name=region
    )
    dynamodb = session.resource('dynamodb')

    anki_table_name = ''
    anki_table = dynamodb.Table(anki_table_name)
    
    content_name = []
    ans = list()
    for sub_event in event:
        data = json.loads(event[sub_event])
        stamp = 0
        next_date = 0
        consecutive = 0
        is_correct = True
        
        if not is_correct:
            consecutive = 0
        else:
            consecutive += 1
        
        one_day_interval = 24 * 60 * 60
        if consecutive < 7:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp())
        elif consecutive < 14:
            next_date = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp()) + 2 * one_day_interval
        elif consecutive < 21:
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
