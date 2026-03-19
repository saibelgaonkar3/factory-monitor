import os
import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Firebase setup
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("factory/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"Received: {topic} → {payload}")

    data = {
        "value": payload,
        "timestamp": datetime.utcnow()
    }

    if "temperature" in topic:
        db.collection("sensors").add({**data, "type": "temperature"})
    elif "humidity" in topic:
        db.collection("sensors").add({**data, "type": "humidity"})
    elif "smoke" in topic:
        db.collection("sensors").add({**data, "type": "smoke"})
        if float(payload) == 1:
            db.collection("alerts").add({**data, "type": "smoke_detected"})
    elif "detection" in topic:
        db.collection("alerts").add({**data, "type": "human_detected"})

# MQTT setup
mqtt_host = os.environ.get("MQTT_HOST", "localhost")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_host, 1883)
client.loop_forever()