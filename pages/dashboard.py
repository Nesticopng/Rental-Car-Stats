import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

df = cargar_datos()

def inicio():
    st.title("Rent a Car Stats")
    st.dataframe(df)
    df_count = df.groupby('LocOut').count().reset_index()
    fig_pie_locout = px.pie(df_count, values="Confirm", names="LocOut", title="Sitio de Reserva")
    st.plotly_chart(fig_pie_locout)
    df_avg = df.groupby('Class')["TotalBill"].mean().reset_index()
    fig_bar_class = px.bar(df_avg, x="Class", y="TotalBill", color="Class")
    st.plotly_chart(fig_bar_class)