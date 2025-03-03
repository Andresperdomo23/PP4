import streamlit as st
import pandas as pd
import openpyxl

# Configurar la página
st.set_page_config(page_title="Encuesta: Descubre el Sabor de tu Canción", layout="wide")

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

# Inicializar variables de sesión
if "seleccionadas" not in st.session_state:
    st.session_state["seleccionadas"] = []
if "mostrar_resultado" not in st.session_state:
    st.session_state["mostrar_resultado"] = False
if "guardar_respuesta" not in st.session_state:
    st.session_state["guardar_respuesta"] = False
if "datos_guardados" not in st.session_state:
    st.session_state["datos_guardados"] = None
if "clave_ingresada" not in st.session_state:
    st.session_state["clave_ingresada"] = False

# Datos del usuario
st.title("🎵 Encuesta: Descubre el Sabor de tu Canción 🎶")
st.write("Completa los siguientes campos y luego selecciona palabras que describan la canción")

nombre = st.text_input("Nombre Completo", value=st.session_state.get("nombre", ""))
correo = st.text_input("Correo Electrónico", value=st.session_state.get("correo", ""))
spotify_link = st.text_input("Enlace de la canción en Spotify", value=st.session_state.get("spotify_link", ""))

yogur_griego = st.radio("¿Te gustaría que tu experiencia de sabor musical incluya yogur griego?", ["Sí", "No"], index=1)

st.session_state["nombre"] = nombre
st.session_state["correo"] = correo
st.session_state["spotify_link"] = spotify_link

st.write("---")

# Evaluar selección
if 5 <= len(st.session_state["seleccionadas"]) <= 10:
    st.subheader("❓ ¿Quieres que tu sabor musical sea secreto hasta que llegue a ti?")
    
    col1, col2 = st.columns(2)
    if col1.button("🎵 Descubre tu Mermelada Musical 🎶"):
        st.session_state["mostrar_resultado"] = True
    if col2.button("🔒 Guardar respuesta en secreto"):
        st.session_state["guardar_respuesta"] = True
    
    if st.session_state["mostrar_resultado"] or st.session_state["guardar_respuesta"]:
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
        
        # Guardar los datos
        st.session_state["datos_guardados"] = pd.DataFrame({
            "Nombre": [nombre],
            "Correo": [correo],
            "Spotify Link": [spotify_link],
            "Palabras Seleccionadas": [", ".join(st.session_state["seleccionadas"])],
            "Sabor Principal": [sabor_principal],
            "Sabor Secundario": [sabor_secundario],
            "Incluye Yogur Griego": [yogur_griego]
        })
        
        if st.session_state["mostrar_resultado"]:
            st.subheader("🎯 Resultado")
            st.success(f"🍓 **Tu mermelada ideal es:** {sabor_principal} con {sabor_secundario}")

# Clave para descargar
st.write("\n\n\n")  # Espacio en blanco para hacerlo menos perceptible
if st.session_state["datos_guardados"] is not None:
    clave = st.text_input("Ingrese la clave para descargar", type="password")
    if clave == "mermelada123":  # Clave secreta
        st.session_state["clave_ingresada"] = True
    
    if st.session_state["clave_ingresada"]:
        if st.button("⬇️ Descargar respuestas en Excel", key="descarga_oculta"):
            excel_file = "respuestas_encuesta.xlsx"
            st.session_state["datos_guardados"].to_excel(excel_file, index=False, engine='openpyxl')
            with open(excel_file, "rb") as file:
                st.download_button(label="Descargar Archivo", data=file, file_name=excel_file, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

