import datetime
import boto3
from boto3.session import Session

def lambda_handler(event, context):
    region = ""
    session = Session(
        regison_name=region
    )
    dynamodb = session.resource('dynamodb')

    anki_table_name = ''
    anki_table = dynamodb.Table(anki_table_name)
    category_table_name = ''
    category_table = dynamodb.Table(category_table_name)

    primary_key = ''
    content_name = []
    stamp = int(datetime.datetime.now().timestamp())
    put_card_response = anki_table.put_item(
        Item = {
            primary_key: stamp
            content_name[0]: event[content_name[0]]
        }
    )

    put_category_response = category_table.put_item(
        Item = {
            categories[0]: event[content_name[0]]
        }
    )
    
    scan_response = table.scan()
    scan_response['Items'] = sorted(scan_response['Items'], key=lambda x:x[primary_key], reverse=True)
    return scan_response
