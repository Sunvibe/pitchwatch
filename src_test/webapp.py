import streamlit as st
import threading
import time

# Endlos-Task-Funktion
def background_task():
    while True:
        # Beispiel: Logik für die Hintergrundaufgabe
        print("Hintergrund-Task läuft...")
        time.sleep(5)  # Task-Intervall (5 Sekunden)

# Thread initialisieren und starten
def start_background_task():
    task_thread = threading.Thread(target=background_task, daemon=True)
    task_thread.start()

# Start des Tasks bei App-Start
start_background_task()

# Rest der Streamlit-App
st.title("Meine Streamlit App")
st.write("Dieser Text wird angezeigt, während der Hintergrund-Task läuft.")