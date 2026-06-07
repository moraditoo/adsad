import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    iframe {
        width: 100% !important;
        height: 100vh !important;
        border: none;
    }
    header {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# 1. Obtenemos la ruta exacta de la carpeta donde está guardado este main.py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Construimos la ruta segura hacia tu archivo HTML (asegúrate de que se llame exactamente así en GitHub)
ruta_html = os.path.join(directorio_actual, "elevador.html")

# 3. Abrimos el archivo usando la ruta segura
with open(ruta_html, "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=1000, scrolling=True)