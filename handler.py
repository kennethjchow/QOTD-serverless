import requests
import json
import boto3


def hello(event, context):
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'.format(response.json()['origin']))

hello(None,None)