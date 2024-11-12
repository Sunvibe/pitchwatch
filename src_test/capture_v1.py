import requests

# The player URL that is embedded on 
playerUrl = "https://livestream.com/accounts/4931571/events/5369913/player?width=1590&height=895&autoPlay=true&mute=true"

# Query
response = requests.get(playerUrl)

import re
import json

# HTML Inhalt vom Response lesen
html_content = response.text

# Extrahieren des JavaScript-Blocks mit Regex
pattern = r'window\.config\s*=\s*({.*?});'
match = re.search(pattern, html_content, re.DOTALL)

if match:
    # Der extrahierte JSON-String
    json_str = match.group(1)
    
    try:
        # In ein Python-Wörterbuch umwandeln
        config_data = json.loads(json_str)
        #print("Extrahierte Daten:", config_data)
    except json.JSONDecodeError:
        print("Fehler: JSON konnte nicht dekodiert werden.")
else:
    print("Fehler: JavaScript-Block nicht gefunden.")


import cv2
import time
from datetime import datetime

# URL des HLS- oder RTMP-Streams (beispielsweise .m3u8-Datei)
stream_url = config_data["event"]["stream_info"]["m3u8_url"]

# Funktion zum Verbinden mit dem Stream und Fehlerbehandlung
def connect_to_stream():
    cap = cv2.VideoCapture(stream_url)
    # Versuche, den Stream zu öffnen
    while not cap.isOpened():
        print("Fehler: Kann den Stream nicht öffnen. Versuche es erneut in 5 Sekunden...")
        time.sleep(5)  # Warte 5 Sekunden, bevor du es erneut versuchst
        cap = cv2.VideoCapture(stream_url)
    return cap

# Versuche, mit dem Stream zu verbinden
cap = connect_to_stream()


while True:
    # Lese das neueste Frame
    ret, frame = cap.read()

    if ret:
        # Prüfe, ob der Sekundenwert durch 10 teilbar ist
        current_time = datetime.now()
        print(f"Frame erhalten {current_time.second}")
        
        if current_time.second % 10 == 0:
            # Erzeuge einen Zeitstempel für den Dateinamen
            timestamp = current_time.strftime('%Y%m%d_%H%M%S')
            filename = f"frame_{timestamp}.jpg"
            
            # Speichere das Bild mit Zeitstempel im Dateinamen
            cv2.imwrite(filename, frame)
            print(f"Bild gespeichert als {filename}")
            
            # Warte ein wenig, um zu verhindern, dass das Bild mehrfach gespeichert wird, wenn mehrere Frames pro Sekunde kommen
            time.sleep(1)  # 1 Sekunde warten, bevor das nächste Frame geprüft wird
    else:
        # Fehler beim Frame-Handling, versuche erneut zu verbinden
        print("Fehler: Kann kein Frame lesen. Versuche, erneut zu verbinden...")
        cap.release()  # Schließe den aktuellen Stream
        cap = connect_to_stream()  # Versuche, erneut zu verbinden

# Stream freigeben (dies wird nicht erreicht, da die Schleife unendlich ist)
cap.release()
