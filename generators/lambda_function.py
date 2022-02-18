from weapon_namer import named_title
import json

print('Loading Function')

def lambda_handler(event, context):
    return {
        'statusCode': '200',
        'body': json.dumps(named_title()),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-type': 'application/json'
        }
    }
