import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

# Traducir los valores de la columna Status_
status_translation = {
    "UNKNOW": "Desconocido",
    "SHOW": "Asistió",
    "NO SHOW": "No Asistió",
    "CANCELED": "Cancelado"
}

df["Status_Traducido"] = df["Status_"].map(status_translation)

# Contar la frecuencia de cada categoría
frecuencia_status = df["Status_Traducido"].value_counts().reset_index()
frecuencia_status.columns = ["Estado", "Cantidad"]

# Obtener totales
total_registros = frecuencia_status["Cantidad"].sum()

# Calcular porcentajes
frecuencia_status["Porcentaje"] = (frecuencia_status["Cantidad"] / total_registros) * 100

# Generar Gráfico
def estado_registros():
    st.header("Análisis de Estados de Reservación")

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = px.bar(
            frecuencia_status,
            x="Estado",
            y="Cantidad",
            text="Cantidad",
            title="Distribución de Estados de Reservación",
            color="Estado",
            color_discrete_map={
                "Desconocido": "gray",
                "Asistió": "green",
                "No Asistió": "red",
                "Cancelado": "orange"
            }
        )
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        st.plotly_chart(fig)

    with col2:
        with st.container(border=True):
            st.markdown("### 📊 Datos Adicionales")
            st.divider()
            st.markdown("### 📌 Total de Registros")
            st.header(f"**{total_registros:,} Registros**")

    with st.expander("Análisis detallado de Estados"):
        for _, row in frecuencia_status.iterrows():
            st.write(f"⚫ **{row['Estado']}: {row['Cantidad']} registros ({row['Porcentaje']:.2f}%)**")