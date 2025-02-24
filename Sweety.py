import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuentra el Sabor de tu Canción", layout="centered")

# Palabras descriptivas para la música
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

# Diseño de la app
st.title("🎵 Encuentra el Sabor de tu Canción 🎶")
st.write("Selecciona palabras que describen la canción y descubre el sabor de mermelada perfecto.")

# Selección de palabras
seleccionadas = st.multiselect("🔹 Elige hasta 5 palabras:", palabras_musicales, max_selections=5)

# Mostrar el sabor de la mermelada correspondiente
if seleccionadas:
    sabores_elegidos = [sabores_mermelada.get(p, "Desconocido") for p in seleccionadas]
    st.success(f"🍓 **Tu mermelada perfecta es:** {', '.join(set(sabores_elegidos))} 🎶")

# Mensaje cuando no hay selección
else:
    st.warning("Selecciona al menos una palabra para obtener el sabor de la mermelada.")


