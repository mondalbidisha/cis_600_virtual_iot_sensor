import json
import boto3
import time
from datetime import datetime, timedelta
from botocore.exceptions import ClientError
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IOTSensorData')

def lambda_handler(event, context):
    try:
        # The MQTT message will be inside the event. Records is the key when the event is triggered by IoT Rule
        print(f"Received event: {json.dumps(event)}")
        
        # Extract the MQTT message payload from the event
        message = event  # The payload is directly passed in the event
        if isinstance(message['timestamp'], (int, float)):
            timestamp = Decimal(str(message['timestamp']))  # Convert to Decimal if necessary
        else:
            # If timestamp is a string, parse it into a proper datetime object
            timestamp = Decimal(str(message['timestamp']))

        # Prepare the item to insert into DynamoDB
        item = {
            'sensor_id': str(message['sensor_id']),
            'timestamp': timestamp,
            'temperature': str(message['temperature']),
            'humidity': str(message['humidity']),
            'co2': str(message['co2'])
        }
        
        # Insert the item into DynamoDB
        response = table.put_item(Item=item)
        
        print(f"Data inserted successfully: {json.dumps(item)}")
        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully')
        }
    
    except ClientError as e:
        # Log error and return response
        print(f"Error inserting data into DynamoDB: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error inserting data into DynamoDB')
        }

