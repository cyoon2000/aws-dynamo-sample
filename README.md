# aws-dynamo-sample

Local DevEnv setup for DynamoDB :
1. Prerequsite - Download AWS CLI client and configure (aws configure)
2. Download Dynamo for local
3. Run the following command in the terminal: java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
4. To view list of tables: aws dynamodb list-tables --endpoint-url http://localhost:8000
6. To view table content:
   aws dynamodb scan \
    --table-name GeneratedReport \
    --endpoint-url http://localhost:8000

Local Python IDE Env :
1. Create DynamoDB table (create.py)
2. Load Data (load.py)
3. Add Data (add-new.py)
4. Query Data (query.py)
