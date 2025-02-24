import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="centered")

# Diccionario de relación palabra - sabor de mermelada
sabores_mermelada = {
    "Melódica": "Mango",
    "Rítmica": "Piña",
    "Armoniosa": "Cereza",
    "Expresiva": "Frambuesa",
    "Intensa": "Maracuyá",
    "Suave": "Vainilla",
    "Energética": "Naranja",
    "Relajante": "Lima",
    "Nostálgica": "Manzana",
    "Alegre": "Fresa",
    "Melancólica": "Mora",
    "Emotiva": "Higo",
    "Vibrante": "Papaya",
    "Pegajosa": "Durazno",
    "Hipnótica": "Kiwi",
    "Dramática": "Granada",
    "Sentimental": "Coco",
    "Potente": "Guayaba",
    "Innovadora": "Tamarindo",
    "Clásica": "Limón",
    "Bailable": "Fruta de la pasión",
    "Electrificante": "Cereza negra",
    "Atmosférica": "Naranja sanguina",
    "Romántica": "Rosa",
    "Profunda": "Ciruela",
    "Épica": "Melón",
    "Espiritual": "Fruta estrella",
    "Reflexiva": "Pera",
    "Oscura": "Arándano",
    "Luminosa": "Mandarina",
    "Distorsionada": "Frambuesa azul",
    "Serena": "Mora azul",
    "Envolvente": "Papaya dulce",
    "Dinámica": "Fruta del dragón",
    "Hipnotizante": "Noni",
    "Étnica": "Guayaba rosa",
    "Sofisticada": "Litchi",
    "Cinemática": "Clementina",
    "Tranquila": "Cereza blanca",
    "Explosiva": "Fruta de la pasión",
    "Experimental": "Kumquat",
    "Pegadiza": "Cereza dulce",
    "Psicodélica": "Fruta de la pasión",
    "Seductora": "Mango maduro",
    "Inspiradora": "Fruta de la pasión",
    "Caótica": "Fruta de la pasión",
    "Elevadora": "Fruta de la pasión",
    "Sorpresiva": "Fruta de la pasión"
}

palabras = list(sabores_mermelada.keys())  # Lista de palabras

# Inicializar la sesión para almacenar palabras seleccionadas
if "seleccionadas" not in st.session_state:
    st.session_state["seleccionadas"] = []

st.title("🎵 Encuesta: Descubre el Sabor de tu Canción 🎶")
st.write("Arrastra palabras al área central para descubrir tu mermelada ideal.")

# Diseño de columnas para simular Drag & Drop
col1, col2 = st.columns([2, 3])

# Sección de palabras disponibles (Columna Izquierda)
with col1:
    st.subheader("🎤 Palabras disponibles:")
    for palabra in palabras:
        if st.button(palabra, key=palabra):  # Cada palabra es un botón interactivo
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 5:
                st.session_state["seleccionadas"].append(palabra)

# Sección del "Círculo Central" (Columna Derecha)
with col2:
    st.subheader("🎯 Arrastra aquí tus palabras")
    st.markdown("⬇️ **Zona de Evaluación** ⬇️")
    st.markdown("""
    <div style="border: 2px dashed #4CAF50; padding: 20px; text-align: center;">
        <h4>Palabras seleccionadas:</h4>
        <p style="font-size: 18px;">{}</p>
    </div>
    """.format(", ".join(st.session_state["seleccionadas"]) if st.session_state["seleccionadas"] else "Ninguna"), unsafe_allow_html=True)

    if st.session_state["seleccionadas"]:
        sabores_elegidos = [sabores_mermelada[p] for p in st.session_state["seleccionadas"]]
        st.success(f"🍓 **Tu mermelada perfecta es:** {', '.join(set(sabores_elegidos))} 🎶")

        # Botón para limpiar selección
        if st.button("🔄 Reiniciar selección"):
            st.session_state["seleccionadas"] = []
    else:
        st.warning("Selecciona palabras para generar tu sabor de mermelada.")
