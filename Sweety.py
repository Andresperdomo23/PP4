import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

# Inicializar la sesión para almacenar palabras seleccionadas
if "seleccionadas" not in st.session_state:
    st.session_state["seleccionadas"] = []

# Función para guardar respuestas en Google Sheets
def guardar_respuestas(respuestas):
    # Autenticación con Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)  # Cambia la ruta si es necesario
    client = gspread.authorize(creds)

    # Abrir la hoja de cálculo
    sheet = client.open("Nombre de tu hoja de cálculo").sheet1

    # Guardar las respuestas
    sheet.append_row(respuestas)

st.title("🎵 Encuesta: Descubre el Sabor de tu Canción 🎶")
st.write("Arrastra palabras al área central para descubrir tu mermelada ideal.")

# Diseño de columnas para mostrar palabras y el área de combinación
col1, col2, col3, col4 = st.columns([1, 1, 2, 1])  # Dos columnas para palabras y dos para el área central

# Sección de palabras disponibles (Columna Izquierda)
with col1:
    st.subheader("🎤 Palabras disponibles (Izquierda):")
    palabras_izquierda = list(sabores_mermelada.keys())[:len(sabores_mermelada)//2]  # Primera mitad
    for palabra in palabras_izquierda:
        if st.button(palabra, key=palabra):
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 5:
                st.session_state["seleccionadas"].append(palabra)

# Sección de palabras disponibles (Columna Derecha)
with col2:
    st.subheader("🎤 Palabras disponibles (Derecha):")
    palabras_derecha = list(sabores_mermelada.keys())[len(sabores_mermelada)//2:]  # Segunda
