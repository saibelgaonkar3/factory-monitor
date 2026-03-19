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
