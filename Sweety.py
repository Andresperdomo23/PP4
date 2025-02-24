import streamlit as st

# Configurar la página
st.set_page_config(page_title="Encuentra el Sabor de tu Canción", layout="wide")

# Diccionario de palabras y sabores
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

# Lista de palabras disponibles
palabras = list(sabores_mermelada.keys())

# Diseño de la app con columnas (para simular un círculo)
st.title("🎵 Encuentra el Sabor de tu Canción 🎶")
st.write("Selecciona palabras que describan tu canción y descubre el sabor de mermelada perfecto.")

col1, col2, col3 = st.columns([2, 3, 2])

# Columna izquierda con palabras
with col1:
    st.subheader("🎤 Selecciona tus palabras:")
    seleccionadas = st.multiselect("🔹 Elige hasta 5 palabras:", palabras)

# Columna central con "círculo"
with col2:
    st.subheader("🎯 Zona de Evaluación")
    st.markdown("⬇️ **Aquí se mostrará el sabor de tu mermelada** ⬇️")
    
    if seleccionadas:
        sabores_elegidos = [sabores_mermelada[p] for p in seleccionadas]
        st.success(f"🍓 **Tu mermelada ideal es:** {', '.join(set(sabores_elegidos))} 🎶")
    else:
        st.warning("Selecciona al menos una palabra para obtener el sabor de la mermelada.")

# Columna derecha con más palabras para ayudar al usuario
with col3:
    st.subheader("🎶 Más palabras:")
    st.write(", ".join(palabras[:15]) + " ...")  # Muestra algunas palabras de ejemplo

# Pie de página
st.write("---")
st.write("💡 **Sugerencia:** Prueba combinaciones distintas para encontrar tu sabor ideal.")
