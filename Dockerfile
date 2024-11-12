# Benutze ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Code in den Container
COPY . .

# Standardbefehl zum Ausführen des Containers
CMD ["python", "pitchwatch/capture.py"]
