# CIS 600 - Virtual IoT Sensor

## Overview

This project implements an IoT system that collects sensor data (such as temperature, humidity, and CO2 levels) from IoT devices, processes it using AWS Lambda, and stores it in DynamoDB for future analysis. The system leverages MQTT for communication and AWS IoT Core for managing device communication. The primary focus is on the integration of AWS services (Lambda, DynamoDB, IoT Core) to build a scalable and reliable IoT data pipeline.

## Architecture

### IoT Devices:
- Devices send sensor data (temperature, humidity, CO2, timestamp) using MQTT protocol.

### AWS IoT Core:
- The devices publish messages to an MQTT topic.
- AWS IoT Core listens for messages on the topic and triggers an AWS Lambda function.

### AWS Lambda:
- The Lambda function is triggered by the MQTT message and processes the data.
- The Lambda function formats the data (converts numeric values to Decimal type for DynamoDB compatibility) and inserts the data into a DynamoDB table.

### DynamoDB:
- DynamoDB is used to store the processed sensor data, including attributes like `sensor_id`, `timestamp`, `temperature`, `humidity`, and `co2`.

## Prerequisites

- **AWS Account:** You need an AWS account to access AWS IoT Core, Lambda, and DynamoDB.
- **AWS CLI:** AWS Command Line Interface (CLI) should be installed and configured to interact with AWS resources.
- **IAM Roles:** Ensure that the Lambda function has permissions to access DynamoDB and IoT Core.
- **MQTT Broker:** Devices or simulators should be able to publish messages to an MQTT topic.
