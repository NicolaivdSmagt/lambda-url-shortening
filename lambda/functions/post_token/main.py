from __future__ import print_function

import boto3
import json
import random
import string

print('Loading function')
        
def lambda_handler(event, context):

    try:
        if not event['auth'] == '{{PASS}}':
            raise Exception('Authentication failed')
    except:
        raise Exception('Authentication failed')
        
    print("Received event: " + json.dumps(event, indent=2))

    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1').Table('redir_urls')

    url = event['url']
    token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
    shorturl = 'http://{{YOURDOMAIN}}/' + token

    print('URL is ' + url + ', token is ' + token + ', shorturl is ' + shorturl)
    
    response = dynamodb.put_item(
       Item={
            'token': token,
            'destination_url': url,
            'shorturl': shorturl
       }
    )
    return {"shorturl": shorturl}
