import streamlit as st
from sections.dashboard import inicio
from sections.cargar_archivo import cargar_archivo
from sections.pdf import PDF
from sections.documentacion import documentacion
from src.components.sidebar import mostrar_sidebar
from src.components.openai import ChatGPT

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
if st.session_state.selected_page == "Chat IA":
    ChatGPT()
if st.session_state.selected_page == "Documentación":
    documentacion()