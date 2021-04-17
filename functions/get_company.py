import boto3, os, json
from boto3.dynamodb.conditions import Key

table = boto3.resource('dynamodb').Table(os.environ['DDBTableName'])

def handler(event, context):
    company = event['queryStringParameters']['q']



    dbResponse = table.query(
            KeyConditionExpression=Key('company').eq(company)
    )
            
    response = {
        "statusCode": 200,
        "body": json.dumps(dbResponse)
    }

    return response