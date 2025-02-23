import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import datetime

# CONFIGURAR GOOGLE SHEETS
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("tu_archivo_credenciales.json", scope)
client = gspread.authorize(creds)
spreadsheet = client.open("Encuesta_Mermelada")  # Nombre del Google Sheets
worksheet = spreadsheet.sheet1  # Primera hoja del documento

# FUNCIÓN PARA GUARDAR RESPUESTAS EN GOOGLE SHEETS
def guardar_en_sheets(datos):
    worksheet.append_row(datos)

# INTERFAZ STREAMLIT
st.title("Encuesta Interactiva: ¡Descubre Tu Mermelada Perfecta! 🍓🍊")

# PEDIR NOMBRE Y CANCIÓN DE SPOTIFY
nombre = st.text_input("Tu nombre:")
spotify_link = st.text_input("Comparte un enlace de una canción de Spotify:")

# SECCIÓN DE SABOR Y TOPPING
st.subheader("Explora los Sabores y Toppings 🍯")
st.write("Antes de responder la encuesta, conoce los posibles sabores de mermeladas y toppings.")

if st.button("Descubrir sabores y toppings"):
    st.write("🔹 **Ejemplo de sabores:** Dulce con un toque cítrico, intenso y tropical, etc.")
    st.write("🔹 **Ejemplo de toppings:** Almendras caramelizadas, chips de chocolate, etc.")

st.subheader("Encuesta Interactiva")
pregunta1 = st.radio("¿Qué tipo de sabores prefieres?", ["Dulce", "Ácido", "Agridulce"])
pregunta2 = st.radio("¿Te gustan los sabores intensos o suaves?", ["Intensos", "Suaves"])
pregunta3 = st.radio("¿Qué textura prefieres?", ["Cremosa", "Con trozos de fruta"])
pregunta4 = st.radio("¿Prefieres mermeladas clásicas o con un giro innovador?", ["Clásicas", "Innovadoras"])
pregunta5 = st.radio("Elige un topping para acompañar tu mermelada:", ["Nueces", "Chispas de chocolate", "Semillas de chía", "Coco rallado"])

# GENERAR RESULTADO
if st.button("Descubrir mi combinación"):
    combinaciones = {
        ("Dulce", "Suaves", "Cremosa", "Clásicas"): "Fresa - Durazno",
        ("Dulce", "Suaves", "Cremosa", "Innovadoras"): "Mango - Maracuyá",
        ("Ácido", "Intensos", "Con trozos de fruta", "Clásicas"): "Frambuesa - Kiwi",
        ("Agridulce", "Intensos", "Cremosa", "Innovadoras"): "Piña - Naranja",
    }
    resultado = combinaciones.get((pregunta1, pregunta2, pregunta3, pregunta4), "Combinación única personalizada")

    # REGISTRAR RESPUESTAS CON FECHA Y HORA
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    respuestas = [fecha_hora, nombre, spotify_link, pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, resultado]
    guardar_en_sheets(respuestas)

    # MOSTRAR RESULTADO AL USUARIO
    st.success(f"¡Tu combinación perfecta es: **{resultado}**! 🍓🍊")

# DESCARGA DEL ARCHIVO SOLO PARA ADMINISTRADOR
st.subheader("Descarga de Resultados (Solo Administrador)")
password = st.text_input("Ingresa la clave de administrador:", type="password")

if password == "mermelada123":
    if st.button("Descargar respuestas"):
        data = worksheet.get_all_values()
        df = pd.DataFrame(data, columns=["Fecha", "Nombre", "Spotify", "Sabor", "Intensidad", "Textura", "Estilo", "Topping", "Combinación"])
        df.to_csv("respuestas.csv", index=False)
        st.download_button("Descargar respuestas", df.to_csv(index=False).encode("utf-8"), "respuestas.csv", "text/csv")

