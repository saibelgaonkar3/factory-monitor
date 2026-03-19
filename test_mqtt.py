import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("factory/test")
client.loop_start()

import time
time.sleep(1)
client.publish("factory/test", "hello from laptop")
time.sleep(2)
client.loop_stop()