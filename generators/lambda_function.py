import namegen
import sw_townspeople
import weapon_namer
import json

print('Loading Function')

def lambda_handler(event, context):
    path = event['pathParameters']['proxy']
    params = event['queryStringParameters']
    res = 'unknown method: ' + path
    status = '400'
    
    if path.lower() == 'weapon':
        res = weapon_namer.named_title()
        status = '200'

    if path.lower() == 'character':
        chardata = sw_townspeople.character()
        chardata['name'] = weapon_namer.name()
        res = chardata
        status = '200'
    
    return {
        'statusCode': status,
        'body': json.dumps(res),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-type': 'application/json'
        }
    }
