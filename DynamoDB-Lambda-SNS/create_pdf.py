from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

# Your project description
project_description = """
🚀 Serverless Notification System using DynamoDB + Lambda + SNS

This project demonstrates how to build a simple, real-world serverless application on AWS using DynamoDB, Lambda, and SNS. The goal is to store data (toy information) in a DynamoDB table and send an email notification every time a new item is added.

📘 Table of Contents

🧠 Project Idea

🧱 AWS Services Used

🎯 Objective

🛠️ Architecture Diagram

🪜 Step-by-Step Setup

🧪 Testing

🧹 Cleanup (Free Tier Safety)

📸 Screenshots

📎 Resources

🧠 Project Idea

Build a toy collection system where every time a new toy is added, it is saved in a DynamoDB table and a notification email is sent using SNS, triggered by a Lambda function.

🧱 AWS Services Used

Service

Purpose

DynamoDB

Store toy data in a fast, serverless NoSQL database

Lambda

Run a function to write data and send email notification

SNS

Send email alerts when new data is added

IAM

Manage permissions between services

🎯 Objective

Create a system that:

Accepts toy details (ToyID, ToyName) via Lambda

Stores them in DynamoDB

Sends an email notification via SNS

🛠️ Architecture Diagram

+---------+         +-----------+        +-----------+
|         |         |           |        |           |
|  User   +-------> |  Lambda   +------> |  DynamoDB |
|         |         | Function  |        |   Table   |
|         |         +-----+-----+        +-----------+
|         |               |
|         |               v
|         |          +----------+
|         |          |   SNS    |
|         |          |  Topic   |
|         |          +----+-----+
|         |               |
|         |               v
|         |          Email Notification
+---------+              📧

🪜 Step-by-Step Setup

1️⃣ Create DynamoDB Table

Name: ToyCollection

Partition Key: ToyID (String)

Billing Mode: Pay-per-request (Free Tier)

2️⃣ Create Lambda Function

Name: AddToyToDynamoDB

Runtime: Python 3.12

Role Permissions:

AmazonDynamoDBFullAccess

AmazonSNSFullAccess

Lambda Code:

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

3️⃣ Create SNS Topic

Name: ToyAlerts

Subscribe with your email

Confirm the subscription via email link

🧪 Testing

Go to Lambda → Click Test

Input Test JSON:

{
  "ToyID": "102",
  "ToyName": "LEGO Blocks"
}

Result:

Data is added to DynamoDB

Email notification is received with subject New Toy Added

🧹 Cleanup (Free Tier Safety)

Use these CLI commands to remove resources after testing:

Delete Lambda:

aws lambda delete-function --function-name AddToyToDynamoDB

Delete DynamoDB Table:

aws dynamodb delete-table --table-name ToyCollection

Delete SNS Topic:

aws sns delete-topic --topic-arn arn:aws:sns:ap-south-1:<ACCOUNT_ID>:ToyAlerts


📎 Resources

AWS DynamoDB Docs

AWS Lambda Docs

AWS SNS Docs

AWS Free Tier Info

📌 This project is part of my AWS hands-on journey. Uploaded to GitHub and shared on LinkedIn to document my learning. #AWS #Serverless #CloudProjects #DevOps #LearningByDoing


"""

# Create the PDF
doc = SimpleDocTemplate("AWS_Serverless_Project.pdf", pagesize=A4)
styles = getSampleStyleSheet()
flowables = []

# Add the project description
for paragraph in project_description.strip().split('\n\n'):
    flowables.append(Paragraph(paragraph.replace("\n", "<br />"), styles["Normal"]))
    flowables.append(Spacer(1, 12))

# Add screenshots
screenshot_dir = "./screenshots"
image_files = sorted([f for f in os.listdir(screenshot_dir) if f.endswith((".png", ".jpg", ".jpeg"))])

for image_file in image_files:
    img_path = os.path.join(screenshot_dir, image_file)
    img = Image(img_path, width=6*inch, height=3.5*inch)
    flowables.append(PageBreak())
    flowables.append(img)
    flowables.append(Spacer(1, 12))

# Build the PDF
doc.build(flowables)

print("✅ PDF generated successfully as 'AWS_Serverless_Project.pdf'")
