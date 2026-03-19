import paho.mqtt.client as mqtt
import time, random

client = mqtt.Client()
client.connect("localhost", 1883)

print("Simulator running...")

while True:
    temp = round(random.uniform(25, 45), 2)
    humidity = round(random.uniform(40, 80), 2)
    smoke = random.choice([0, 1])

    client.publish("factory/sensors/temperature", temp)
    client.publish("factory/sensors/humidity", humidity)
    client.publish("factory/sensors/smoke", smoke)

    print(f"Published → temp: {temp}, humidity: {humidity}, smoke: {smoke}")
    time.sleep(3)