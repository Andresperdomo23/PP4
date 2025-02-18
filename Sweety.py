import streamlit as st

def generar_mermelada(respuestas):
    """
    Genera una combinación de frutas y toppings según las respuestas de la encuesta.
    """
    # Mapeo de respuestas a combinaciones de frutas
    frutas = {
        "Algo ligero que fluye suavemente": ("Pera", "Lavanda"),
        "Un golpe de energía que despierta": ("Frambuesa", "Maracuyá"),
        "Una vibración profunda que te envuelve": ("Arándanos", "Cacao"),
        "Una sensación cambiante e impredecible": ("Piña", "Jengibre")
    }
    
    # Mapeo de respuestas a toppings
    toppings = {
        "Un día soleado y despreocupado": "Granola crujiente",
        "Una noche intensa y emocionante": "Trozos de chocolate oscuro",
        "Un momento íntimo y nostálgico": "Nueces caramelizadas",
        "Algo abstracto y difícil de definir": "Pétalos de rosa cristalizados"
    }
    
    fruta_seleccionada = frutas.get(respuestas["sensación_cuerpo"], ("Fresa", "Limón"))
    topping_seleccionado = toppings.get(respuestas["imagen_recuerdo"], "Coco rallado")
    
    return {
        "Frutas para la mermelada": fruta_seleccionada,
        "Topping recomendado": topping_seleccionado
    }

# Interfaz con Streamlit
st.title("🎶 Generador de Mermelada Musical 🍓")

sensacion_cuerpo = st.selectbox("Si una canción pudiera sentirse físicamente, ¿cómo crees que sería la sensación en tu cuerpo?", 
    ["Algo ligero que fluye suavemente", "Un golpe de energía que despierta", "Una vibración profunda que te envuelve", "Una sensación cambiante e impredecible"])

imagen_recuerdo = st.selectbox("Cuando escuchas tu música favorita, ¿qué tipo de recuerdo o imagen viene más a tu mente?", 
    ["Un día soleado y despreocupado", "Una noche intensa y emocionante", "Un momento íntimo y nostálgico", "Algo abstracto y difícil de definir"])

if st.button("Generar Mermelada"): 
    respuestas_usuario = {
        "sensación_cuerpo": sensacion_cuerpo,
        "imagen_recuerdo": imagen_recuerdo
    }
    resultado = generar_mermelada(respuestas_usuario)
    st.subheader("🍓 Tu mermelada personalizada:")
    st.write(f"**Frutas:** {resultado['Frutas para la mermelada'][0]} y {resultado['Frutas para la mermelada'][1]}")
    st.write(f"**Topping recomendado:** {resultado['Topping recomendado']}")
