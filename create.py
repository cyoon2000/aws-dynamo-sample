import boto3
from boto3.dynamodb.conditions import Key, Attr

# dynamodb_client = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('GeneratedReport')
table.delete()

# try:
response = dynamodb.create_table(
    TableName='GeneratedReport',
    KeySchema=[
        {
            'AttributeName': 'doc_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'report_type',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'doc_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'report_type',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
    )
print(response)

# except dynamodb_client.exceptions.ResourceInUseException:
#     print('table exist')
#     pass
