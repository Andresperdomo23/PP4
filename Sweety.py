import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Encuesta de Música y Mermelada", layout="centered")

# Diccionario de relación palabra - sabor de mermelada y topping
sabores_mermelada = {
    "Melódica": ("Mango", "Nueces caramelizadas"),
    "Rítmica": ("Piña", "Coco rallado"),
    "Armoniosa": ("Cereza", "Yogur natural"),
    "Expresiva": ("Frambuesa", "Chocolate negro"),
    "Intensa": ("Maracuyá", "Menta fresca"),
    "Suave": ("Vainilla", "Almendras fileteadas"),
    "Energética": ("Naranja", "Jengibre confitado"),
    "Relajante": ("Lima", "Hierbabuena"),
    "Nostálgica": ("Manzana", "Canela en polvo"),
    "Alegre": ("Fresa", "Chispas de chocolate"),
    "Melancólica": ("Mora", "Crema batida"),
    "Emotiva": ("Higo", "Pistachos"),
    "Vibrante": ("Papaya", "Frutos secos"),
    "Pegajosa": ("Durazno", "Mermelada de higo"),
    "Hipnótica": ("Kiwi", "Semillas de chía"),
    "Dramática": ("Granada", "Frambuesas frescas"),
    "Sentimental": ("Coco", "Coco rallado"),
    "Potente": ("Guayaba", "Salsa de tamarindo"),
    "Innovadora": ("Tamarindo", "Chiles en polvo"),
    "Clásica": ("Limón", "Azúcar glass"),
    "Bailable": ("Fruta de la pasión", "Rodajas de limón"),
    "Electrificante": ("Cereza negra", "Salsa de chocolate"),
    "Atmosférica": ("Naranja sanguina", "Menta picada"),
    "Romántica": ("Rosa", "Pétalos de rosa"),
    "Profunda": ("Ciruela", "Nueces picadas"),
    "Épica": ("Melón", "Miel"),
    "Espiritual": ("Fruta estrella", "Semillas de girasol"),
    "Reflexiva": ("Pera", "Almendras"),
    "Oscura": ("Arándano", "Chocolate blanco"),
    "Luminosa": ("Mandarina", "Azúcar moreno"),
    "Distorsionada": ("Frambuesa azul", "Frutos del bosque"),
    "Serena": ("Mora azul", "Yogur griego"),
    "Envolvente": ("Papaya dulce", "Miel de abeja"),
    "Dinámica": ("Fruta del dragón", "Jengibre fresco"),
    "Hipnotizante": ⬤
