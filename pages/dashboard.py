import streamlit as st
from src.utils.helpers import cargar_datos
from src.components.indicadores_dashboard import indicadores_dashboard
from src.components.grafica_class import grafica_class
from src.components.grafica_source import grafica_source
from src.components.grafica_tiempo import grafica_tiempo
from src.components.grafica_loc import grafica_loc
from src.components.tasa_prepago import tasa_pregago

df = cargar_datos()

def inicio():
    st.title("Rent a Car Stats")

    indicadores_dashboard()

    st.markdown("<br>", unsafe_allow_html=True)

    grafica_class()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    grafica_source()

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    grafica_tiempo()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    grafica_loc()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    st.write("Mapa?")

    st.write("Variables Númericas")

    tasa_pregago()

    st.write("Configuraciones")

    st.dataframe(df)