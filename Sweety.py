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
    
    fruta_seleccionada = frutas.get(respuestas["sensación_cuerpo"], ("Fresa", "Limón"))
    fruta_extra = frutas.get(respuestas["imagen_recuerdo"], ("Piña", "Mango"))
    topping_seleccionado = toppings.get(respuestas["impacto_cancion"], "Coco rallado")
    
    return {
        "Frutas para la mermelada": (fruta_seleccionada[0], fruta_extra[1]),
        "Topping recomendado": topping_seleccionado
    }

# Interfaz con Streamlit
st.title("🎶 Generador de Mermelada Musical 🍓")

sensacion_cuerpo = st.selectbox("Si una canción pudiera sentirse físicamente, ¿cómo crees que sería la sensación en tu cuerpo?", 
    ["Algo ligero que fluye suavemente", "Un golpe de energía que despierta", "Una vibración profunda que te envuelve", "Una sensación cambiante e impredecible"])

imagen_recuerdo = st.selectbox("Cuando escuchas tu música favorita, ¿qué tipo de recuerdo o imagen viene más a tu mente?", 
    ["Un día soleado y despreocupado", "Una noche intensa y emocionante", "Un momento íntimo y nostálgico", "Algo abstracto y difícil de definir"])

impacto_cancion = st.selectbox("¿Cómo describirías el impacto de una canción que realmente te emociona?", 
    ["Directo y explosivo", "Progresivo, algo que va creciendo lentamente", "Sutil pero con una intensidad que se queda contigo", "Impredecible, con giros inesperados"])

if st.button("Generar Mermelada"): 
    respuestas_usuario = {
        "sensación_cuerpo": sensacion_cuerpo,
        "imagen_recuerdo": imagen_recuerdo,
        "impacto_cancion": impacto_cancion
    }
    resultado = generar_mermelada(respuestas_usuario)
    st.subheader("🍓 Tu mermelada personalizada:")
    st.write(f"**Frutas:** {resultado['Frutas para la mermelada'][0]} y {resultado['Frutas para la mermelada'][1]}")
    st.write(f"**Topping recomendado:** {resultado['Topping recomendado']}")
