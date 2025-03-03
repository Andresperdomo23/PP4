import streamlit as st
import pandas as pd

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
    "Ácido-Dulces": ["Almendras", "Nueces"],
    "Ácidas": ["Chocolate amargo", "Canela", "Queso azul"]
}

# Inicializar variables de sesión
if "seleccionadas" not in st.session_state:
    st.session_state["seleccionadas"] = []
if "mostrar_resultado" not in st.session_state:
    st.session_state["mostrar_resultado"] = False
if "guardar_respuesta" not in st.session_state:
    st.session_state["guardar_respuesta"] = False

# Datos del usuario
st.title("🎵 Encuesta: Descubre el Sabor de tu Canción 🎶")
st.write("Completa los siguientes campos y luego selecciona palabras que describan la canción")

nombre = st.text_input("Nombre Completo")
correo = st.text_input("Correo Electrónico")
spotify_link = st.text_input("Enlace de la canción en Spotify")

st.write("---")

# Simulación de Drag & Drop con selección de palabras
st.subheader("🔹 Selecciona entre 5 y 10 palabras que describan la canción")

# Crear tres columnas
col1, col2, col3 = st.columns(3)

# Mostrar palabras como botones interactivos en las columnas
for categoria, lista_palabras in palabras_clasificadas.items():
    for palabra in lista_palabras:
        # Determinar en qué columna colocar el botón
        if categoria == "Dulces":
            col = col1
        elif categoria == "Ácido-Dulces":
            col = col2
        else:
            col = col3

        display_text = f"✅ {palabra}" if palabra in st.session_state["seleccionadas"] else palabra

        if col.button(display_text, key=palabra, help="Selecciona esta palabra"):
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 10:
                st.session_state["seleccionadas"].append(palabra)
            elif palabra in st.session_state["seleccionadas"]:
                st.session_state["seleccionadas"].remove(palabra)

st.write("---")

# Evaluar selección
if 5 <= len(st.session_state["seleccionadas"]) <= 10:
    st.subheader("❓ ¿Quieres que tu sabor musical sea secreto hasta que llegue a ti?")
    col1, col2 = st.columns(2)
    
    if col1.button("🎵 Descubre tu Mermelada Musical 🎶"):
        st.session_state["mostrar_resultado"] = True
    
    if col2.button("🔒 Guardar respuesta en secreto"):
        st.session_state["guardar_respuesta"] = True
    
    if st.session_state["mostrar_resultado"]:
        st.subheader("🎯 Resultado")
        palabras = st.session_state["seleccionadas"]
        
        # Clasificar palabras según categorías
        predominantes = palabras[:3]
        secundarias = palabras[3:7]
        
        # Determinar sabores
        sabores_seleccionados = list({sabor for categoria, sabores in sabores_mermelada.items() for palabra in predominantes + secundarias if palabra in palabras_clasificadas[categoria] for sabor in sabores})
        
        if len(sabores_seleccionados) >= 2:
            sabor_principal, sabor_secundario = sabores_seleccionados[:2]
        elif len(sabores_seleccionados) == 1:
            sabor_principal, sabor_secundario = sabores_seleccionados[0], "Sin combinación"
        else:
            sabor_principal, sabor_secundario = "No determinado", "No determinado"
        
        st.success(f"🍓 **Tu mermelada ideal es:** {sabor_principal} con {sabor_secundario}")
    
    if st.session_state["guardar_respuesta"]:
        data = {
            "Nombre": [nombre],
            "Correo": [correo],
            "Spotify Link": [spotify_link],
            "Palabras Seleccionadas": [", ".join(st.session_state["seleccionadas"])],
            "Sabor Principal": [sabor_principal],
            "Sabor Secundario": [sabor_secundario]
        }
        
        df = pd.DataFrame(data)
        
        excel_file = "encuesta_musica_mermelada.xlsx"
        df.to_excel(excel_file, index=False)
        
        with open(excel_file, "rb") as file:
            st.download_button(label="Descargar Archivo", data=file, file_name=excel_file, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
