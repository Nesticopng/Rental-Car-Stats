import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

df["PickUpDate"] = df["Pickupd"].astype(str).str[:10]
df["ReturnDate"] = df["Returnd"].astype(str).str[:10]
df["BookedDate"] = df["Booked"].astype(str).str[:10]


def grafica_tiempo():
    st.write(df)