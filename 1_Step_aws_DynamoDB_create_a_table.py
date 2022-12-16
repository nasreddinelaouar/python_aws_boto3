#In this step, you create a table named Movies. The primary key for the table is comprised of the following attributes:

#year - The partition key. The AttributeType is N for number.
#title – The sort key. The AttributeType is S for string.
#Copy the following program and paste it into a file named MoviesCreateTable.py. Change the region us-west-2 to the same region as the Cloud9 instance.

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
#In the create_table call, you specify the table name, primary key attributes, and its data types.

#The ProvisionedThroughput parameter is required.

#To run the program, enter the following command python MoviesCreateTable.py
