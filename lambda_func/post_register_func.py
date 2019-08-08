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
    category_table_name = ''
    category_table = dynamodb.Table(category_table_name)

    primary_key = ''
    content_name = []
    stamp = int(datetime.datetime.now().timestamp())
    one_day_interval = 24 * 60 * 60
    next_stamp = int(datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).timestamp()) + one_day_interval
    put_card_response = anki_table.put_item(
        Item = {
            primary_key: stamp,
            content_name[0]: event[content_name[0]]
        }
    )
    
    categories = []
    try:
        put_category_response = category_table.put_item(
            Item = {
                categories[0]: event[content_name[0]]
            },
            Expected = {
                categories[1]: {
                    "Exists": False
                }
            }
        )
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            print("Error: Duplicate")
        else:
            raise

    json_data = {'result':'200'}
    return json.dumps(json_data)
