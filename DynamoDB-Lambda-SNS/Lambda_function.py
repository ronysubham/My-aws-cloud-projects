import json
import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

table = dynamodb.Table('ToyCollection')
TOPIC_ARN = 'arn:aws:sns:ap-south-1:<ACCOUNT_ID>:ToyAlerts'  # Replace this

def lambda_handler(event, context):
    toy_id = event['ToyID']
    toy_name = event['ToyName']

    table.put_item(Item={"ToyID": toy_id, "ToyName": toy_name})

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="New Toy Added",
        Message=f"A new toy was added: {toy_name} (ID: {toy_id})"
    )

    return {
        'statusCode': 200,
        'body': json.dumps("Toy added and notification sent!")
    }