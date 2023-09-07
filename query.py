import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('GeneratedReport')

print("List of Tables:")
print(list(dynamodb.tables.all()))

print("Query by docId:")

response = table.query(
    KeyConditionExpression=Key('doc_id').eq("ab9d39a7-85bc-4cc6-82e7-6684c3c734ef")
)

for i in response['Items']:
    print(i['doc_id'], " - Report Type : ", i['report_type'], ", Language : ", i['language'], ", Status : ", i['status'])