import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurar la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="centered")

# Diccionario de relación palabra - sabor de mermelada - topping
sabores_mermelada = {
    # (mismos valores que antes)
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

# Diseño de columnas para simular Drag & Drop
col1, col2 = st.columns([2, 3])

# Sección de palabras disponibles (Columna Izquierda)
with col1:
    st.subheader("🎤 Palabras disponibles:")
    for palabra in sabores_mermelada.keys():
        if st.button(palabra, key=palabra):
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

        # Guardar respuestas en Google Sheets
        if st.button("💾 Guardar Respuestas"):
            guardar_respuestas(st.session_state["seleccionadas"])
            st.success("✅ Respuestas guardadas en Google Sheets.")

        #
