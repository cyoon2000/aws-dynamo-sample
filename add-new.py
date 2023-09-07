import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('GeneratedReport')

docId = str(uuid.uuid4())
print(docId)

response = table.put_item(
   Item={
        'doc_id': docId,
        'report_type': "BioGenesis Report",
        'language': "German",
        'status': "Done"
    }
)

print("Add New Reord:")
print(json.dumps(response, indent=4))