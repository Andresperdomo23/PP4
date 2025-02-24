import streamlit as st
import random
from streamlit_dnd import dnd_container, dnd_item

# Diccionario de palabras clave y sabores
sabores = {
    "Melódica": "Frutos rojos con un toque de vainilla",
    "Rítmica": "Mango con chile",
    "Armoniosa": "Durazno y almendra",
    "Expresiva": "Frambuesa y menta",
    "Intensa": "Chocolate y cereza",
    "Suave": "Pera y miel",
    "Energética": "Maracuyá y naranja",
    "Relajante": "Lavanda y mora",
    "Nostálgica": "Manzana y canela",
    "Alegre": "Piña y coco",
    "Melancólica": "Arándanos y té verde",
    "Emotiva": "Ciruela y vainilla",
    "Vibrante": "Kiwi y limón",
    "Pegajosa": "Caramelo y plátano",
    "Hipnótica": "Higo y jengibre",
    "Dramática": "Uva y nuez",
    "Sentimental": "Moras y cardamomo",
    "Potente": "Café y avellana",
    "Innovadora": "Pitahaya y lima",
    "Clásica": "Fresa y crema",
    "Bailable": "Cereza y limón",
    "Electrizante": "Toronja y pimienta",
    "Atmosférica": "Nuez moscada y durazno",
    "Romántica": "Rosas y frambuesa",
    "Profunda": "Mango y cúrcuma",
    "Épica": "Maracuyá y chocolate",
    "Espiritual": "Jazmín y miel",
    "Reflexiva": "Pera y lavanda",
    "Oscura": "Zarzamora y anís",
    "Luminosa": "Mandarina y jengibre",
    "Distorsionada": "Melón y romero",
    "Serena": "Coco y lavanda",
    "Envolvente": "Naranja y avellana",
    "Dinámica": "Papaya y limón",
    "Hipnotizante": "Uva y jengibre",
    "Étnica": "Guayaba y canela",
    "Sofisticada": "Pistache y fresa",
    "Cinemática": "Cereza y chocolate",
    "Tranquila": "Almendra y vainilla",
    "Explosiva": "Maracuyá y chile",
    "Experimental": "Pitahaya y pimienta",
    "Pegadiza": "Kiwi y piña",
    "Psicodélica": "Nuez y caramelo",
    "Seductora": "Higo y chocolate",
    "Inspiradora": "Manzana y miel",
    "Caótica": "Lima y chile",
    "Elevadora": "Mango y menta",
    "Sorpresiva": "Mandarina y pimienta",
    "Íntima": "Fresa y coco",
    "Contagiosa": "Maracuyá y piña"
}

st.title("🎵 Encuesta de Sabores Musicales 🍯")
st.write("Arrastra las palabras que describan tu canción al círculo y descubre tu mermelada perfecta.")

# Sección de palabras clave (draggable)
st.subheader("Selecciona tus palabras:")

selected_words = []
with dnd_container():
    for word in sabores.keys():
        if dnd_item(word):
            selected_words.append(word)

# Área de drop (círculo)
st.subheader("🔵 Arrastra aquí tus palabras")
drop_area = dnd_container()
if drop_area:
    st.write("### 🍯 Tu sabor de mermelada 🍯")
    if selected_words:
        sabores_seleccionados = [sabores[word] for word in selected_words]
        st.success(f"Tu mermelada ideal es: {', '.join(set(sabores_seleccionados))}")
    else:
        st.warning("Arrastra al menos una palabra para generar un sabor.")

