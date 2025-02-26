import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuesta Interactiva", layout="wide")

# Título de la aplicación
st.title("Encuesta Interactiva sobre Canciones")

# Instrucciones para los usuarios
st.write("Selecciona las palabras que asocias con los sentimientos de una canción:")

# Lista de 25 palabras para la encuesta
palabras = [
    "Feliz", "Triste", "Energético", "Melancólico", "Romántico",
    "Nostálgico", "Divertido", "Reflexivo", "Apasionado", "Relajante",
    "Motivador", "Desgarrador", "Esperanzador", "Sorpresivo", "Dulce",
    "Intenso", "Sutil", "Profundo", "Alegre", "Desolador",
    "Fuerte", "Suave", "Rítmico", "Lento", "Rápido"
]

# Crear dos columnas: una para las palabras y otra para los resultados
col1, col2 = st.columns([1, 2])

# Columna de palabras
with col1:
    st.subheader("Selecciona las palabras:")
    seleccionadas = st.multiselect("Palabras:", palabras)

# Columna de resultados
with col2:
    st.subheader("Resultados")
    if st.button("Enviar"):
        if seleccionadas:
            st.success("Has seleccionado: " + ", ".join(seleccionadas))
        else:
            st.error("Por favor, selecciona al menos una palabra.")
