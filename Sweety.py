import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="centered")

# Diccionario de relación palabra - sabor de mermelada
sabores_mermelada = {
    "Dulce": "Fresa",
    "Melancólica": "Mora",
    "Alegre": "Durazno",
    "Intensa": "Frambuesa",
    "Suave": "Vainilla",
    "Explosiva": "Maracuyá",
    "Misteriosa": "Higo",
    "Romántica": "Rosa",
    "Nostálgica": "Manzana",
    "Brillante": "Naranja",
    "Sombría": "Cereza negra"
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
