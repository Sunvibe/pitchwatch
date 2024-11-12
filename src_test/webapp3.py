import streamlit as st
from pathlib import Path
from PIL import Image

# Setze den Pfad zum Bilderordner
IMAGE_FOLDER = "bilder3"

# Titel der Anwendung
st.title("Bildgalerie und Diashow")

# Hole alle Bilddateien aus dem Ordner
image_paths = sorted(list(Path(IMAGE_FOLDER).glob("*.jpg")) + list(Path(IMAGE_FOLDER).glob("*.png")) + list(Path(IMAGE_FOLDER).glob("*.jpeg")))

# Wenn keine Bilder gefunden wurden
if not image_paths:
    st.warning("Keine Bilder im Ordner gefunden!")
else:
    # Initialisiere den Index im Session State, falls er nicht existiert
    if 'image_index' not in st.session_state:
        st.session_state.image_index = 0

    # Galerie-Ansicht
    st.subheader("Galerie")
    cols = st.columns(3)  # Zeige 3 Bilder pro Zeile an

    for idx, image_path in enumerate(image_paths):
        with cols[idx % 3]:
            img = Image.open(image_path)
            st.image(img, caption=image_path.name, use_container_width=True)

    # Diashow-Ansicht
    st.subheader("Diashow")
    
    # Aktuelles Bild in der Diashow
    current_image = Image.open(image_paths[st.session_state.image_index])
    st.image(current_image, caption=f"Bild {st.session_state.image_index + 1} von {len(image_paths)}", use_container_width=True)
    
    # Buttons für die Steuerung der Diashow
    col1, col2, col3 = st.columns([1, 6, 1])
    
    # "Zurück"-Button
    with col1:
        if st.button("⬅️ Zurück"):
            st.session_state.image_index = (st.session_state.image_index - 1) % len(image_paths)
    
    # "Weiter"-Button
    with col3:
        if st.button("➡️ Weiter"):
            st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)
    
    # JavaScript für Tastatursteuerung (links/rechts Pfeiltasten)
    st.write(
        """
        <script>
        document.addEventListener('keydown', function(event) {
            if(event.key === "ArrowLeft") {
                window.parent.document.querySelector('button[aria-label="⬅️ Zurück"]').click();
            }
            else if(event.key === "ArrowRight") {
                window.parent.document.querySelector('button[aria-label="➡️ Weiter"]').click();
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )
