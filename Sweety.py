import streamlit as st

# Configurar la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="wide")

# Diccionario de palabras y su clasificación
palabras_clasificadas = {
    "Dulces": ["Alegre", "Vibrante", "Brillante", "Romántica", "Dulce", "Envolvente", "Festiva", "Suave", "Elevadora"],
    "Ácido-Dulces": ["Melancólica", "Profunda", "Explosiva", "Dramática", "Reflexiva", "Nostálgica", "Sofisticada"],
    "Ácidas": ["Oscura", "Intensa", "Hipnótica", "Caótica", "Contundente", "Triste", "Agresiva"]
}

# Lista de sabores organizados por dulzura
sabores_mermelada = {
    "Dulces": ["Mango", "Guanábana", "Brevas", "Remolacha", "Papayuela", "Pera Boyacense", "Durazno Criollo", "Guayaba", "Feijoa"],
    "Ácido-Dulces": ["Tomate de árbol", "Arándanos", "Fresas de Subachoque", "Ruibarbo y fresas", "Piña", "Mora", "Chontaduro", "Ciruela Criolla"],
    "Ácidas": ["Frutos Cítricos", "Lulo", "Uchuvas", "Tamarindo", "Naranja"]
}

# Toppings recomendados
toppings = {
    "Dulces": ["Chocolate blanco", "Miel", "Frutas caramelizadas"],
    "Ácido-Dulces": ["Almendras", "Nueces", "Yogur griego"],
    "Ácidas": ["Chocolate amargo", "Canela", "Queso azul"]
}

# Inicializar variables de sesión
if "seleccionadas" not in st.session_state:
    st.session_state["seleccionadas"] = []

# Datos del usuario
st.title("🎵 Encuesta: Descubre el Sabor de tu Canción 🎶")
st.write("Completa los siguientes campos y luego selecciona palabras que describan la canción")

nombre = st.text_input("Nombre Completo")
correo = st.text_input("Correo Electrónico")
spotify_link = st.text_input("Enlace de la canción en Spotify")

st.write("---")

# Simulación de Drag & Drop con selección de palabras
st.subheader("🔹 Selecciona 10 palabras que describan la canción")

# Crear tres columnas
col1, col2, col3 = st.columns(3)

# Mostrar palabras como botones interactivos en las columnas
for i, (categoria, lista_palabras) in enumerate(palabras_clasificadas.items()):
    for palabra in lista_palabras:
        # Determinar en qué columna colocar el botón
        if i % 3 == 0:
            col = col1
        elif i % 3 == 1:
            col = col2
        else:
            col = col3

        # Cambiar el color del botón si la palabra ya está seleccionada
        if palabra in st.session_state["seleccionadas"]:
            button_color = "success"  # Color verde para seleccionadas
        else:
            button_color = "primary"  # Color azul para no seleccionadas

        if col.button(palabra, key=palabra, help="Selecciona esta palabra"):
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 10:
                st.session_state["seleccionadas"].append(palabra)
            elif palabra in st.session_state["seleccionadas"]:
                st.session_state["seleccionadas"].remove(palabra)

st.write("---")

# Evaluar selección
if len(st.session_state["seleccionadas"]) == 10:
    st.subheader("🎯 Resultado")
    palabras = st.session_state["seleccionadas"]
    
    # Clasificar palabras según categorías
    predominantes = palabras[:3]
    secundarias = palabras[3:7]
    toppings_elegidos = palabras[7:]
    
    # Determinar sabores
    sabor_principal = next((sabor for categoria, sabores in sabores_mermelada.items() for palabra in predominantes if palabra in palabras_clasificadas[categoria] for sabor in sabores), "")
    sabor_secundario = next((sabor for categoria, sabores in sabores_mermelada.items() for palabra in secundarias if palabra in palabras_clasificadas[categoria] for sabor in sabores), "")
    
    # Determinar toppings
    topping_final = next((
