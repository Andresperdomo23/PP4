import streamlit as st
import pandas as pd
import os
from datetime import datetime

def generar_mermelada(respuestas):
    """
    Genera una experiencia sensorial basada en las respuestas de la encuesta.
    """
    # Mapeo de respuestas a combinaciones de frutas
    frutas = {
        "Algo ligero que fluye suavemente": ("Pera", "Lavanda"),
        "Un golpe de energía que despierta": ("Frambuesa", "Maracuyá"),
        "Una vibración profunda que te envuelve": ("Arándanos", "Cacao"),
        "Una sensación cambiante e impredecible": ("Piña", "Jengibre"),
        "Un día soleado y despreocupado": ("Durazno", "Naranja"),
        "Una noche intensa y emocionante": ("Ciruela", "Canela"),
        "Un momento íntimo y nostálgico": ("Mora", "Miel"),
        "Algo abstracto y difícil de definir": ("Higo", "Especias"),
        "Directo y explosivo": ("Limón", "Frutos rojos"),
        "Progresivo, algo que va creciendo lentamente": ("Manzana", "Canela"),
        "Sutil pero con una intensidad que se queda contigo": ("Pera", "Chocolate blanco"),
        "Impredecible, con giros inesperados": ("Maracuyá", "Romero")
    }
    
    # Mapeo de respuestas a toppings
    toppings = {
        "Como un flujo continuo, sin interrupciones": "Vainilla y miel",
        "Como un ciclo que regresa con familiaridad": "Fresa y limón rallado",
        "Como un viaje que cambia de rumbo": "Kiwi y hierbabuena",
        "Como una explosión breve pero intensa": "Maracuyá y chocolate oscuro"
    }
    
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Guardar en un archivo CSV
    archivo_csv = "combinaciones_generadas.csv"
    nuevo_registro = pd.DataFrame([{
        "Fecha y Hora": fecha_hora_actual,
        "Nombre": respuestas["nombre"],
        "Canción": respuestas["cancion"],
        "Frutas": f"{frutas[respuestas['sensación_cuerpo']][0]} y {frutas[respuestas['imagen_recuerdo']][1]}",
        "Topping": toppings.get(respuestas["impacto_cancion"], "Coco rallado")
    }])
    
    if not os.path.exists(archivo_csv):
        nuevo_registro.to_csv(archivo_csv, index=False)
    else:
        nuevo_registro.to_csv(archivo_csv, mode="a", index=False, header=False)
    
    return archivo_csv

# Interfaz con Streamlit
st.title("🎶 Generador de Experiencia Sensorial Musical 🍓")

# Campos de entrada para el usuario
nombre = st.text_input("📝 Ingresa tu nombre")
cancion = st.text_input("🎵 Pega el link de tu canción en Spotify")

sensacion_cuerpo = st.selectbox("Si una canción pudiera sentirse físicamente, ¿cómo crees que sería la sensación en tu cuerpo?", 
    ["Algo ligero que fluye suavemente", "Un golpe de energía que despierta", "Una vibración profunda que te envuelve", "Una sensación cambiante e impredecible"])

imagen_recuerdo = st.selectbox("Cuando escuchas tu música favorita, ¿qué tipo de recuerdo o imagen viene más a tu mente?", 
    ["Un día soleado y despreocupado", "Una noche intensa y emocionante", "Un momento íntimo y nostálgico", "Algo abstracto y difícil de definir"])

impacto_cancion = st.selectbox("¿Cómo describirías el impacto de una canción que realmente te emociona?", 
    ["Directo y explosivo", "Progresivo, algo que va creciendo lentamente", "Sutil pero con una intensidad que se queda contigo", "Impredecible, con giros inesperados"])

if st.button("Generar Experiencia Sensorial"):
    archivo_csv = generar_mermelada({
        "nombre": nombre,
        "cancion": cancion,
        "sensación_cuerpo": sensacion_cuerpo,
        "imagen_recuerdo": imagen_recuerdo,
        "impacto_cancion": impacto_cancion
    })
    st.success("✅ Tu experiencia ha sido registrada con éxito.")

# Autenticación y botón de descarga
codigo_secreto = st.text_input("🔑 Ingresa el código de administrador", type="password")
if codigo_secreto == "mermelada123":
    if os.path.exists("combinaciones_generadas.csv"):
        with open("combinaciones_generadas.csv", "rb") as file:
            st.download_button(
                label="📥 Descargar combinaciones generadas",
                data=file,
                file_name="combinaciones_generadas.csv",
                mime="text/csv"
            )
    else:
        st.error("⚠️ No hay combinaciones generadas aún.")
