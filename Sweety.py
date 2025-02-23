import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def autenticar_google_drive():
    """Autenticación en Google Drive usando credenciales JSON."""
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credenciales_drive.json")  # Cargar credenciales desde el archivo JSON
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    return GoogleDrive(gauth)

def guardar_en_drive(respuestas):
    """Guarda las respuestas en un archivo CSV y lo sube a Google Drive."""
    drive = autenticar_google_drive()
    
    archivo_csv = "respuestas_encuesta.csv"
    nuevo_registro = pd.DataFrame([{
        "Fecha y Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Nombre": respuestas["nombre"],
        "Canción": respuestas["cancion"],
        "Textura": respuestas["textura"],
        "Intensidad": respuestas["intensidad"],
        "Frutas Base": respuestas["frutas"],
        "Topping": respuestas["topping"]
    }])
    
    if os.path.exists(archivo_csv):
        nuevo_registro.to_csv(archivo_csv, mode="a", index=False, header=False)
    else:
        nuevo_registro.to_csv(archivo_csv, index=False)
    
    # Subir a Google Drive
    file_drive = drive.CreateFile({"title": archivo_csv, "parents": [{"id": "1UFkxlzexjA07woQy7RpUCgsEzTWtWRCm?hl=es"}]})
    file_drive.SetContentFile(archivo_csv)
    file_drive.Upload()
    
    return "✅ Datos guardados en Google Drive exitosamente."

# Interfaz con Streamlit
st.title("🎶 Generador de Experiencia Sensorial Musical 🍓")

# Opción para conocer el sabor y topping antes de la encuesta
if st.checkbox("🔍 Quiero conocer el sabor y topping antes de responder la encuesta"):
    st.write("Cada mermelada tiene una combinación única de frutas y toppings que reflejan sensaciones musicales. ¡Explora y elige la tuya!")
    fruta_demo = st.selectbox("Elige un perfil de sabor", ["Maracuyá, limón", "Manzana, pera", "Arándanos, moras", "Piña, tamarindo"])
    topping_demo = st.selectbox("Elige un topping complementario", ["Miel o vainilla", "Ralladura de cítricos", "Hierbas frescas", "Chocolate oscuro o especias"])
    st.success(f"Tu elección: **{fruta_demo}** con un toque de **{topping_demo}**")
    
# Continuar con la encuesta
st.subheader("🎤 Ahora responde para descubrir tu combinación personalizada")

# Campos de entrada para el usuario
nombre = st.text_input("📝 Ingresa tu nombre")
cancion = st.text_input("🎵 Pega el link de tu canción en Spotify")

sensacion_cuerpo = st.selectbox("Si una canción pudiera sentirse físicamente, ¿cómo crees que sería la sensación en tu cuerpo?", 
    ["Algo ligero y fluido", "Un golpe de energía", "Una vibración profunda", "Una sensación cambiante"])

imagen_recuerdo = st.selectbox("Cuando escuchas tu música favorita, ¿qué tipo de recuerdo o imagen viene más a tu mente?", 
    ["Día soleado y despreocupado", "Noche intensa y emocionante", "Momento íntimo y nostálgico", "Algo abstracto y difícil de definir"])

impacto_cancion = st.selectbox("¿Cómo describirías el impacto de una canción que realmente te emociona?", 
    ["Directo y explosivo", "Progresivo y creciente", "Sutil pero persistente", "Impredecible y cambiante"])

percepcion_tiempo = st.selectbox("¿Cómo sientes el paso del tiempo dentro de una canción que te gusta?", 
    ["Fluye sin interrupciones", "Ciclo que regresa", "Viaje con cambios de rumbo", "Explosión breve e intensa"])

if st.button("Generar Experiencia Sensorial"):
    respuestas_usuario = {
        "nombre": nombre,
        "cancion": cancion,
        "textura": sensacion_cuerpo,
        "intensidad": imagen_recuerdo,
        "frutas": impacto_cancion,
        "topping": percepcion_tiempo
    }
    resultado = guardar_en_drive(respuestas_usuario)
    st.success(resultado)
    st.write("📂 Tus datos han sido guardados en Google Drive.")
