import streamlit as st
from src.utils.helpers import cargar_datos
from src.components.indicadores_dashboard import indicadores_dashboard
from src.components.grafica_class import grafica_class

df = cargar_datos()

def inicio():
    st.title("Rent a Car Stats")
    indicadores_dashboard()
    grafica_class()
    st.dataframe(df)