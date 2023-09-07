import boto3
import json
# import decimal

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('GeneratedReport')

with open("reports.json") as json_file:
    reports = json.load(json_file)
    for report in reports:
        docId = report['doc_id']
        reportType = report['report_type']
        language = report['language']
        status = report['status']

        print("Add Report:", docId, reportType)

        table.put_item(
           Item={
               'doc_id': docId,
               'report_type': reportType,
               'language': language,
               'status': status,
            }
        )