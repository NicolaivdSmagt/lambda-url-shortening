from __future__ import print_function

import boto3
import json
import random
import string

print('Loading function')

def lambda_handler(event, context):

#    print("Received event: " + json.dumps(event, indent=2))

    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1').Table('redir_urls')

    token = event['token']
    
    try:
        response = dynamodb.get_item ( Key= {'token': token})
        url = response['Item']['destination_url']
        content = "<html><body>Moved: <a href=\"" + url + "\">" + url + "</a></body></html>"
    except:
        content = "<html><body><h1>Not Found</h1></body></html>"
        return {"content": content}

    return {"destination_url": url, "content": content}
