import streamlit as st
import pandas as pd
import os
from datetime import datetime

def generar_mermelada(respuestas):
    """
    Genera una experiencia sensorial basada en las respuestas de la encuesta.
    """
    # Mapeo de respuestas a características de la mermelada
    texturas = {
        "Algo ligero y fluido": "Suave, cremosa",
        "Un golpe de energía": "Con trozos de fruta",
        "Una vibración profunda": "Densa, concentrada",
        "Una sensación cambiante": "Mezcla de texturas"
    }
    
    intensidades = {
        "Día soleado y despreocupado": "Dulce y fresco",
        "Noche intensa y emocionante": "Ácido o especiado",
        "Momento íntimo y nostálgico": "Dulce y cálido",
        "Algo abstracto y difícil de definir": "Mezcla inesperada"
    }
    
    frutas_base = {
        "Directo y explosivo": "Maracuyá, limón",
        "Progresivo y creciente": "Manzana, pera",
        "Sutil pero persistente": "Arándanos, moras",
        "Impredecible y cambiante": "Piña, tamarindo"
    }
    
    toppings = {
        "Fluye sin interrupciones": "Miel o vainilla",
        "Ciclo que regresa": "Ralladura de cítricos",
        "Viaje con cambios de rumbo": "Hierbas frescas (menta, albahaca)",
        "Explosión breve e intensa": "Chocolate oscuro o especias"
    }
    
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Determinar los atributos de la mermelada
    textura = texturas.get(respuestas["sensación_cuerpo"], "Desconocida")
    intensidad = intensidades.get(respuestas["imagen_recuerdo"], "Desconocida")
    fruta = frutas_base.get(respuestas["impacto_cancion"], "Desconocida")
    topping = toppings.get(respuestas["percepcion_tiempo"], "Desconocido")
    
    # Guardar en un archivo CSV
    archivo_csv = "combinaciones_generadas.csv"
    nuevo_registro = pd.DataFrame([{
        "Fecha y Hora": fecha_hora_actual,
        "Nombre": respuestas["nombre"],
        "Canción": respuestas["cancion"],
        "Textura": textura,
        "Intensidad": intensidad,
        "Frutas Base": fruta,
        "Topping": topping
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
    ["Algo ligero y fluido", "Un golpe de energía", "Una vibración profunda", "Una sensación cambiante"])

imagen_recuerdo = st.selectbox("Cuando escuchas tu música favorita, ¿qué tipo de recuerdo o imagen viene más a tu mente?", 
    ["Día soleado y despreocupado", "Noche intensa y emocionante", "Momento íntimo y nostálgico", "Algo abstracto y difícil de definir"])

impacto_cancion = st.selectbox("¿Cómo describirías el impacto de una canción que realmente te emociona?", 
    ["Directo y explosivo", "Progresivo y creciente", "Sutil pero persistente", "Impredecible y cambiante"])

percepcion_tiempo = st.selectbox("¿Cómo sientes el paso del tiempo dentro de una canción que te gusta?", 
    ["Fluye sin interrupciones", "Ciclo que regresa", "Viaje con cambios de rumbo", "Explosión breve e intensa"])

if st.button("Generar Experiencia Sensorial"):
    archivo_csv = generar_mermelada({
        "nombre": nombre,
        "cancion": cancion,
        "sensación_cuerpo": sensacion_cuerpo,
        "imagen_recuerdo": imagen_recuerdo,
        "impacto_cancion": impacto_cancion,
        "percepcion_tiempo": percepcion_tiempo
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
