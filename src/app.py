import streamlit as st
from pages.dashboard import inicio
from pages.cargar_archivo import cargar_archivo
from pages.pdf import PDF
from pages.documentacion import documentacion
from src.components.sidebar import mostrar_sidebar

# Configuración de la página
st.set_page_config(
    page_title='Rent a Car Stats 📊',
    page_icon="car",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Mostrar la barra lateral personalizada
mostrar_sidebar()

if st.session_state.selected_page == "Inicio":
    inicio()
if st.session_state.selected_page == "Cargar Archivo":
    cargar_archivo()
if st.session_state.selected_page == "PDF":
    PDF()
if st.session_state.selected_page == "Documentación":
    documentacion()