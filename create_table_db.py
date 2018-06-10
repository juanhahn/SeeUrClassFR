from __future__ import print_function  # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='asistencia_curso',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)