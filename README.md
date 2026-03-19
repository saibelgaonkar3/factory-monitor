# Factory Hazard Monitor

IoT-based factory monitoring system with edge AI for fire and human detection.

## Team
- **Sai** — DevOps / Infrastructure (MQTT + Firebase bridge, Docker)
- **Tanya** — Flutter app (Firebase Firestore dashboard)
- **Isha** — Hardware (RPi 5, sensors, buzzer)
- **Saloni** — ML / Integration (YOLOv8n fire + human detection)

## Stack
- **MQTT Broker** — Mosquitto (Docker)
- **Bridge** — Python (paho-mqtt + firebase-admin)
- **Database** — Firebase Firestore
- **App** — Flutter (Android)
- **Edge AI** — YOLOv8n on Raspberry Pi 5

## MQTT Topics
| Topic | Publisher | Description |
|---|---|---|
| factory/sensors/temperature | Isha (RPi) | Temperature in °C |
| factory/sensors/humidity | Isha (RPi) | Humidity in % |
| factory/sensors/smoke | Isha (RPi) | 0 or 1 |
| factory/camera/detection | Saloni (RPi) | 0 or 1 |

## Firestore Collections
- `sensors` — temperature, humidity, smoke readings
- `alerts` — smoke_detected, human_detected events

## Setup
### Prerequisites
- Docker Desktop
- Python 3.11+
- Firebase project with Firestore enabled

### Run
1. Add `serviceAccount.json` to project root
2. Run `docker compose up --build`
3. Run simulator (for testing): `python simulator/fake_sensor.py`

### On Raspberry Pi
1. `git clone https://github.com/saibelgaonkar3/factory-monitor`
2. `cd factory-monitor`
3. Add `serviceAccount.json`
4. `docker compose up --build`


firebase output: 

<img width="1446" height="728" alt="image" src="https://github.com/user-attachments/assets/03c1219a-e69e-4996-a67d-f4acde026de0" />


ON HARDWARE :
On RPi, here's the full setup:

**Step 1 — Install Docker**
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo reboot
```

**Step 2 — Install Git and clone repo**
```bash
sudo apt install git -y
git clone https://github.com/saibelgaonkar3/factory-monitor.git
cd factory-monitor
```

**Step 3 — Add serviceAccount.json**
Copy `serviceAccount.json` to the Pi (via USB or `scp` from laptop):
```bash
# on your laptop run this
scp serviceAccount.json pi@<pi-ip>:~/factory-monitor/
```

**Step 4 — Run Docker**
```bash
docker compose up --build
```

**Step 5 — Isha runs her sensor script**
```bash
cd ~/
pip install paho-mqtt
python sensor_script.py  # her own script, not the simulator
```

**Step 6 — Saloni runs her ML script**
```bash
pip install ultralytics paho-mqtt opencv-python
python detection_script.py  # her own script
```

---

**Both Isha and Saloni** point their scripts to:
```python
client.connect("localhost", 1883)
```
Since Mosquitto runs on the Pi itself via Docker, `localhost` works fine.

---

NOTES FOR MEMBERS:

## MQTT Topics
| Topic | Publisher | Description |
|---|---|---|
| factory/sensors/temperature | Isha (RPi) | Temperature in °C |
| factory/sensors/humidity | Isha (RPi) | Humidity in % |
| factory/sensors/smoke | Isha (RPi) | 0 = no smoke, 1 = smoke detected |
| factory/camera/detection | Saloni (RPi) | 0 = no detection, 1 = human/fire detected |

## Saloni — Detection Script Guide
Publish to `factory/camera/detection` topic with:
- `1` — human or fire detected in frame
- `0` — nothing detected

Example:
```python
client.publish("factory/camera/detection", 1)  # when detected
client.publish("factory/camera/detection", 0)  # when clear
```
