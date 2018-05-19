
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table for the first Login Page.
table = dynamodb.create_table(
    TableName='login_page_1',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
             'AttributeName': 'password',
             'KeyType': 'HASH'
         },
        {
            'AttributeName': 'first_name',
            'KeyType': 'RANGE'
        },
        {
             'AttributeName': 'last_name',
             'KeyType': 'RANGE'
         },
        {
             'AttributeName': 'email',
             'KeyType': 'RANGE'
         },
        {
             'AttributeName': 'zipcode',
             'KeyType': 'RANGE'
         },
        {
              'AttributeName': 'bio',
              'KeyType': 'RANGE'
          }
    ],
    AttributeDefinitions=[
       {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
       {
            'AttributeName': 'password',
            'AttributeType': 'S'
        },
       {
             'AttributeName': 'first_name',
             'AttributeType': 'S'
        },
       {
             'AttributeName': 'last_name',
             'AttributeType': 'S'
        },
       {
             'AttributeName': 'email',
             'AttributeType': 'S'
        },
       {
             'AttributeName': 'zipcode',
             'AttributeType': 'S'
        },
       {
             'AttributeName': 'bio',
             'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='login_page_1')

