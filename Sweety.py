import streamlit as st

# Configurar la página
st.set_page_config(page_title="Encuentra el Sabor de tu Canción", layout="centered")

# Diccionario de palabras musicales y sus sabores de mermelada
sabores_mermelada = {
    "Dulce": "Fresa", "Melancólica": "Mora", "Alegre": "Durazno", "Intensa": "Frambuesa",
    "Suave": "Vainilla", "Explosiva": "Maracuyá", "Misteriosa": "Higo", "Romántica": "Rosa",
    "Nostálgica": "Manzana", "Brillante": "Naranja", "Sombría": "Cereza negra", "Relajante": "Lavanda",
    "Densa": "Chocolate", "Fluida": "Miel", "Dramática": "Granada", "Energética": "Limón",
    "Épica": "Mango", "Serena": "Pera", "Majestuosa": "Uva", "Luminosa": "Piña",
    "Orgánica": "Higo", "Abstracta": "Kiwi", "Hipnótica": "Coco", "Caótica": "Guayaba",
    "Groovy": "Plátano", "Emotiva": "Arándano", "Clásica": "Frutilla", "Futurista": "Papaya",
    "Oscura": "Zarzamora", "Ligera": "Melón", "Envolvente": "Mandarina", "Radiante": "Maracuyá",
    "Agresiva": "Toronja", "Eterna": "Dátil", "Sofisticada": "Higo", "Retro": "Ciruela",
    "Íntima": "Avellana", "Mágica": "Lychee", "Festiva": "Frutas tropicales", "Refrescante": "Sandía",
    "Calmante": "Manzanilla", "Introspectiva": "Tamarindo", "Contundente": "Jengibre",
    "Delicada": "Nuez", "Vibrante": "Piña colada", "Exótica": "Pitahaya", "Brumosa": "Café",
    "Celestial": "Violeta", "Cálida": "Canela", "Fría": "Menta"
}

# Interfaz visual
st.title("🎵 Encuentra el Sabor de tu Canción 🎶")
st.write("Selecciona palabras que describan tu canción y descubre el sabor de mermelada perfecto.")

# Diseño visual: Columnas con palabras alrededor de un círculo en el centro
col1, col2, col3 = st.columns([2, 3, 2])

# Columna 1: Algunas palabras a la izquierda
with col1:
    st.subheader("🎤 Selección:")
    seleccionadas = st.multiselect("🔹 Elige hasta 5 palabras:", list(sabores_mermelada.keys()), max_selections=5)

# Columna 2 (Centro): Simulación del "círculo"
with col2:
    st.markdown("### 🎯 Arrastra aquí tus palabras")
    st.markdown("⬇️ ⭕ **Círculo Virtual** ⭕ ⬇️")
    
    if seleccionadas:
        sabores_elegidos = [sabores_mermelada.get(p, "Desconocido") for p in seleccionadas]
        st.success(f"🍓 **Tu mermelada perfecta es:** {', '.join(set(sabores_elegidos))} 🎶")
    else:
        st.warning("Selecciona al menos una palabra para obtener el sabor de la mermelada.")

# Columna 3: Otras palabras a la derecha (solo para diseño visual)
with col3:
    st.subheader("🎶 Más palabras disponibles:")

# Pie de página
st.write("---")
st.write("💡 **Sugerencia:** Experimenta con diferentes combinaciones para descubrir nuevos sabores.")
