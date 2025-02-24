import streamlit as st

# Configurar la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="centered")

# Diccionario de relación palabra - sabor de mermelada - topping
sabores_mermelada = {
    "Dulce": ("Fresa", "Hojuelas de almendra"),
    "Melancólica": ("Mora", "Chocolate amargo"),
    "Alegre": ("Durazno", "Granola"),
    "Intensa": ("Frambuesa", "Queso de cabra"),
    "Suave": ("Vainilla", "Yogur natural"),
    "Explosiva": ("Maracuyá", "Semillas de chía"),
    "Misteriosa": ("Higo", "Jengibre confitado"),
    "Romántica": ("Rosa", "Chocolate blanco"),
    "Nostálgica": ("Manzana", "Queso crema"),
    "Brillante": ("Naranja", "Menta picada"),
    "Sombría": ("Cereza negra", "Cacao en polvo"),
    "Relajante": ("Lavanda", "Miel de abejas"),
    "Densa": ("Chocolate", "Avellanas tostadas"),
    "Fluida": ("Miel", "Nueces picadas"),
    "Dramática": ("Granada", "Tiras de pollo"),
    "Energética": ("Limón", "Ralladura de limón"),
    "Épica": ("Mango", "Almendras caramelizadas"),
    "Serena": ("Pera", "Yogur griego"),
    "Majestuosa": ("Uva", "Queso feta"),
    "Luminosa": ("Piña", "Semillas de girasol"),
    "Caótica": ("Pimentón y Jalapeño", "Tiras de tocino crujiente"),
    "Pegajosa": ("Guayaba", "Rebanadas de plátano"),
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

    if st.session_state["seleccionadas"]:
        st.write("**Palabras seleccionadas:**", ", ".join(st.session_state["seleccionadas"]))
        
        sabores_elegidos = [sabores_mermelada[p][0] for p in st.session_state["seleccionadas"]]
        toppings_elegidos = [sabores_mermelada[p][1] for p in st.session_state["seleccionadas"]]

        st.success(f"🍓 **Tu mermelada perfecta es:** {', '.join(set(sabores_elegidos))} 🎶")
        st.info(f"🥄 **Toppings sugeridos:** {', '.join(set(toppings_elegidos))}")

        # Botón para limpiar selección
        if st.button("🔄 Reiniciar selección"):
            st.session_state["seleccionadas"] = []
    else:
        st.warning("Selecciona palabras para generar tu sabor de mermelada.")
