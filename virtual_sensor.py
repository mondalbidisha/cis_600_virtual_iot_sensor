import paho.mqtt.client as mqtt
import json
import random
import time

AWS_IOT_ENDPOINT = "a3uy930aheaixl-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "VirtualSensor"
TOPIC = "environment/sensors"

CERTIFICATE_PATH = "b3c1b8d90e09fca845b45563816d9546ba71657c3ac199f4bc3a175ca213c242-certificate.pem.crt"
PRIVATE_KEY_PATH = "b3c1b8d90e09fca845b45563816d9546ba71657c3ac199f4bc3a175ca213c242-private.pem.key"
ROOT_CA_PATH = "AmazonRootCA1.pem"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to AWS IoT Core Successfully!")
    else:
        print(f"Connection failed with error code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published successfully!")

client = mqtt.Client(client_id=CLIENT_ID)
client.tls_set(ROOT_CA_PATH, CERTIFICATE_PATH, PRIVATE_KEY_PATH)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(AWS_IOT_ENDPOINT, 8883, 60)
client.loop_start()

while True:
    data = {
        "sensor_id": "VirtualSensorStation",
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2),
        "timestamp": time.time()
    }
    payload = json.dumps(data)
    result = client.publish(TOPIC, payload, qos=1)
    result.wait_for_publish()  
    print("Data Sent :-", payload)
    time.sleep(5)