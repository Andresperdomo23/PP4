import streamlit as st

# Palabras que describen la canción
palabras_musicales = [
    "Dulce", "Melancólica", "Alegre", "Intensa", "Suave", "Explosiva", "Misteriosa",
    "Romántica", "Nostálgica", "Brillante", "Sombría", "Relajante", "Densa", "Fluida",
    "Dramática", "Energética", "Épica", "Serena", "Majestuosa", "Luminosa",
    "Orgánica", "Abstracta", "Hipnótica", "Caótica", "Groovy", "Emotiva", "Clásica",
    "Futurista", "Oscura", "Ligera", "Envolvente", "Radiante", "Agresiva", "Eterna",
    "Sofisticada", "Retro", "Íntima", "Mágica", "Festiva", "Refrescante", "Calmante",
    "Introspectiva", "Contundente", "Delicada", "Vibrante", "Exótica", "Brumosa", 
    "Celestial", "Cálida", "Fría"
]

# Relación de palabras con sabores de mermelada
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
    "Sombría": "Cereza negra",
    "Relajante": "Lavanda",
    "Densa": "Chocolate",
    "Fluida": "Miel",
    "Dramática": "Granada",
    "Energética": "Limón",
    "Épica": "Mango",
    "Serena": "Pera",
    "Majestuosa": "Uva",
    "Luminosa": "Piña",
    "Orgánica": "Higo",
    "Abstracta": "Kiwi",
    "Hipnótica": "Coco",
    "Caótica": "Guayaba",
    "Groovy": "Plátano",
    "Emotiva": "Arándano",
    "Clásica": "Frutilla",
    "Futurista": "Papaya",
    "Oscura": "Zarzamora",
    "Ligera": "Melón",
    "Envolvente": "Mandarina",
    "Radiante": "Maracuyá",
    "Agresiva": "Toronja",
    "Eterna": "Dátil",
    "Sofisticada": "Higo",
    "Retro": "Ciruela",
    "Íntima": "Avellana",
    "Mágica": "Lychee",
    "Festiva": "Frutas tropicales",
    "Refrescante": "Sandía",
    "Calmante": "Manzanilla",
    "Introspectiva": "Tamarindo",
    "Contundente": "Jengibre",
    "Delicada": "Nuez",
    "Vibrante": "Piña colada",
    "Exótica": "Pitahaya",
    "Brumosa": "Café",
    "Celestial": "Violeta",
    "Cálida": "Canela",
    "Fría": "Menta"
}

# Título de la app
st.title("🎵 Encuentra el Sabor de tu Canción 🎶")

# Instrucciones
st.markdown("💡 **Arrastra palabras al círculo central para descubrir el sabor de mermelada perfecto para tu canción.**")

# Diseño de la interfaz
col1, col2 = st.columns([2, 1])

# Sección de palabras
with col1:
    st.markdown("### 🎤 Describe tu canción con estas palabras:")
    seleccionadas = st.multiselect("Selecciona palabras que describan la canción:", palabras_musicales)

# Sección del círculo central
with col2:
    st.markdown("### 🎯 Tu selección:")
    st.write("Arrastra aquí las palabras que describen la canción")

    # Mostramos los sabores según las palabras seleccionadas
    if seleccionadas:
        sabores_elegidos = [sabores_mermelada.get(palabra, "Sin sabor definido") for palabra in seleccionadas]
        st.success(f"🥄 Tu mermelada perfecta es: {', '.join(set(sabores_elegidos))} 🎶")

