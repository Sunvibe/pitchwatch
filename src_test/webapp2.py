import streamlit as st
from pathlib import Path
from PIL import Image

# Setze den Pfad zum Bilderordner
IMAGE_FOLDER = "bilder1"

# Titel der Anwendung
st.title("Bildgalerie")

# Hole alle Bilddateien aus dem Ordner
image_paths = list(Path(IMAGE_FOLDER).glob("*.jpg")) + list(Path(IMAGE_FOLDER).glob("*.png")) + list(Path(IMAGE_FOLDER).glob("*.jpeg"))

# Wenn keine Bilder gefunden wurden
if not image_paths:
    st.warning("Keine Bilder im Ordner gefunden!")
else:
    # Setze die Anzahl der Spalten für die Galerie
    cols = st.columns(3)  # Zeige 3 Bilder pro Zeile an

    # Bilder laden und in der Galerie anzeigen
    for idx, image_path in enumerate(image_paths):
        with cols[idx % 3]:
            img = Image.open(image_path)
            st.image(img, caption=image_path.name, use_container_width=True)
