from itertools import count
from select import select
from tracemalloc import start
import boto3
import uuid
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
from app.config import config

dynamodb = boto3.resource('dynamodb',
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
            region_name=config.region_name)
table = dynamodb.Table(config.db_table)

def put_item_db(json,result):
    table.put_item(    
        Item={
            'id': uuid.uuid4().hex ,
            'json': json,
            'result': result
        }
    )

def get_data_mutant_rows():
    query = table.scan(   
        Select="COUNT",
        FilterExpression=Attr('result').eq(True),
    )
    return query["Count"],query["ScannedCount"]