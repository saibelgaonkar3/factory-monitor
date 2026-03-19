FROM python:3.11-slim

WORKDIR /app

COPY backend/bridge.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "bridge.py"]