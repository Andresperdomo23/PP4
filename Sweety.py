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
    
    # Mapeo de respuestas a descripciones sensoriales
    descripciones = {
        "Algo envolvente y armonioso": "Una combinación que te abraza con cada bocado, con un equilibrio perfecto entre dulzura y frescura.",
        "Un contraste fuerte y marcado": "Una explosión de sabores intensos que despiertan todos tus sentidos.",
        "Una mezcla de matices inesperados": "Un perfil de sabor que cambia con cada mordida, dejándote descubrir nuevas notas con cada degustación.",
        "Un equilibrio entre lo clásico y lo innovador": "Un viaje entre lo familiar y lo sorpresivo, combinando tradición con un giro inesperado."
    }
    
    fruta_seleccionada = frutas.get(respuestas["sensación_cuerpo"], ("Fresa", "Limón"))
    fruta_extra = frutas.get(respuestas["imagen_recuerdo"], ("Piña", "Mango"))
    topping_seleccionado = toppings.get(respuestas["impacto_cancion"], "Coco rallado")
    descripcion_sabor = descripciones.get(respuestas["sensación_melodía"], "Una experiencia sensorial única que combina lo mejor de cada emoción musical.")
    
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Generar pista de sabor sin mencionar las frutas directamente
    pista_sabor = f"Podrás encontrar un toque de lo que madura bajo el sol con una chispa de lo exótico y vibrante." if "Maracuyá" in fruta_extra or "Piña" in fruta_extra else \
                   f"Un balance entre lo suave y aterciopelado con un trasfondo dulce y envolvente." if "Pera" in fruta_extra or "Mango" in fruta_extra else \
                   f"Un perfil de sabor audaz con un toque vibrante que despierta los sentidos." if "Frutos rojos" in fruta_extra or "Frambuesa" in fruta_extra else \
                   f"Una mezcla intrigante de dulzura natural con notas profundas y complejas."
    
    # Guardar en un archivo CSV
    df = pd.DataFrame([{
        "Fecha y Hora": fecha_hora_actual,
        "Nombre": respuestas["nombre"],
        "Canción": respuestas["cancion"],
        "Frutas": f"{fruta_seleccionada[0]} y {fruta_extra[1]}",
        "Topping": topping_seleccionado
    }])
    df.to_csv("combinaciones_generadas.csv", mode="a", index=False, header=False)
    
    return {
        "Descripción Sensorial": descripcion_sabor,
        "Pista de sabor": pista_sabor,
        "Experiencia complementaria": f"Ideal para acompañar con {topping_seleccionado.lower()} y disfrutar con la música adecuada." 
    }

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

sensacion_melodía = st.selectbox("Si pudieras transformar una melodía en una sensación tangible, ¿cómo la describirías?", 
    ["Algo envolvente y armonioso", "Un contraste fuerte y marcado", "Una mezcla de matices inesperados", "Un equilibrio entre lo clásico y lo innovador"])

if st.button("Generar Experiencia Sensorial"):
    respuestas_usuario = {
        "nombre": nombre,
        "cancion": cancion,
        "sensación_cuerpo": sensacion_cuerpo,
        "imagen_recuerdo": imagen_recuerdo,
        "impacto_cancion": impacto_cancion,
        "sensación_melodía": sensacion_melodía
    }
    resultado = generar_mermelada(respuestas_usuario)
    st.subheader("🎶 Tu experiencia sensorial:")
    st.write(f"**Descripción:** {resultado['Descripción Sensorial']}")
    st.write(f"**Pista de sabor:** {resultado['Pista de sabor']}")
    st.write(f"**Experiencia complementaria:** {resultado['Experiencia complementaria']}")

