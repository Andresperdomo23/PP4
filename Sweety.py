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
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
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
    for palabra in list(sabores_mermelada.keys())[:len(sabores_mermelada)//2]:  # Primera mitad
        if st.button(palabra, key=palabra):
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 5:
                st.session_state["seleccionadas"].append(palabra)

# Sección de palabras disponibles (Columna Derecha)
with col2:
    st.subheader("🎤 Palabras disponibles (Derecha):")
    for palabra in list(sabores_mermelada.keys())[len(sabores_mermelada)//2:]:  # Segunda mitad
        if st.button(palabra, key=palabra):
            if palabra not in st.session_state["seleccionadas"] and len(st.session_state["seleccionadas"]) < 5:
                st.session_state["seleccionadas"].append(palabra)

# Sección del "Círculo Central" (entre las dos columnas de palabras)
with col3:
    st.subheader("🎯 Arrastra aquí tus palabras")
    st.markdown("⬇️ **Zona de Evaluación** ⬇️")

    if st.session_state["seleccionadas"]:
        st.write("**Palabras seleccionadas:**", ", ".join(st.session_state["seleccionadas"]))
        
        sabores_elegidos = [sabores_mermelada[p][0] for p in st.session_state["seleccionadas"]]
        toppings_elegidos = [sabores_mermelada[p][1] for p in st.session_state["seleccionadas"]]

        st.success(f"🍓 **Tu mermelada perfecta es:** {', '.join(set(sabores_elegidos))} 🎶")
        st.info(f"🥄 **Toppings sugeridos:** {', '.join(set(toppings_elegidos))}")

        # Guardar respuestas en Google Sheets
        if st.button("💾 Guardar Respuestas"):
            guardar_respuestas(st.session_state["seleccionadas"])
            st.success("✅ Respuestas guardadas en Google Sheets.")

        # Botón para limpiar selección
        if st.button("🔄 Reiniciar selección"):
            st.session_state["seleccionadas"] = []
    else:
        st.warning("Selecciona palabras para generar tu sabor de mermelada.")

# Columna adicional a la derecha (puedes usarla para más información o dejarla vacía)
with col4:
    st.write("")  # Puedes dejar esto vacío o agregar más contenido si lo deseas
