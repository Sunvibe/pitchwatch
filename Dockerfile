# Verwende ein schlankes Alpine-Image als Basis
FROM python:3.13-alpine

# Installiere Systemabhängigkeiten
RUN apk update && apk add --no-cache \
    libgl1-mesa-glx \
    libglib2.0-0 \
    bash

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Code in den Container
COPY . .

# Standardbefehl zum Ausführen des Containers
CMD ["python", "pitchwatch/capture.py"]