import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuesta Interactiva", layout="wide")

# Título de la aplicación
st.title("Encuesta Interactiva sobre Canciones")

# Instrucciones para los usuarios
st.write("Selecciona las palabras que asocias con los sentimientos de una canción:")

# Lista de palabras para la encuesta
palabras = [
    "Feliz", "Triste", "Energético", "Melancólico", "Romántico",
    "Nostálgico", "Divertido", "Reflexivo", "Apasionado", "Relajante",
    "Motivador", "Desgarrador", "Esperanzador", "Sorpresivo", "Dulce",
    "Intenso", "Sutil", "Profundo", "Alegre", "Desolador",
    "Fuerte", "Suave", "Rítmico", "Lento", "Rápido",
    "Bailable", "Melódico", "Experimental", "Clásico", "Moderno",
    "Folk", "Rock", "Pop", "Jazz", "Hip-Hop",
    "Electrónico", "Acústico", "Instrumental", "Vocal", "Coral"
]

# Selector múltiple para que los usuarios elijan palabras
seleccionadas = st.multiselect("Selecciona las palabras:", palabras)

# Botón para enviar respuestas
if st.button("Enviar"):
    if seleccionadas:
        st.success("Has seleccionado: " + ", ".join(seleccionadas))
    else:
        st.error("Por favor, selecciona al menos una palabra.")        
