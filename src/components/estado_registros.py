import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

# Traducir los valores de la columna Status_
status_translation = {
    "UNKNOW": "Desconocidos",
    "SHOW": "Asistieron",
    "NO SHOW": "No Asistieron",
    "CANCELED": "Cancelados"
}

df["Status_Traducido"] = df["Status_"].map(status_translation)

# Contar la frecuencia de cada categoría
frecuencia_status = df["Status_Traducido"].value_counts().reset_index()
frecuencia_status.columns = ["Estado", "Cantidad"]

# Obtener totales
total_registros = frecuencia_status["Cantidad"].sum()

# Calcular porcentajes
frecuencia_status["Porcentaje"] = (frecuencia_status["Cantidad"] / total_registros) * 100

def generar_analisis(frecuencia_status):
    analisis = []
    
    for _, row in frecuencia_status.iterrows():
        estado = row["Estado"]
        porcentaje = row["Porcentaje"]
        
        if estado == "No Asistieron":
            analisis.append(f"- **{porcentaje:.1f}%** de las reservas no se concretaron porque los clientes no asistieron, lo que indica una posible ineficiencia en la planificación del inventario.")
        elif estado == "Asistieron":
            analisis.append(f"- **{porcentaje:.1f}%** de las reservas se completaron con éxito, reflejando un índice aceptable de conversión.")
        elif estado == "Cancelados":
            analisis.append(f"- **{porcentaje:.1f}%** de las reservas fueron canceladas, lo que podría sugerir problemas en la fidelización del cliente o factores externos que influyen en la decisión de alquiler.")
        elif estado == "Desconocidos":
            analisis.append(f"- **{porcentaje:.1f}%** de las reservas tienen un estado desconocido, lo que podría indicar datos inconsistentes o deficiencias en el sistema de seguimiento.")
    
    return "\n".join(analisis)

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
                "Desconocidos": "gray",
                "Asistieron": "green",
                "No Asistieron": "red",
                "Cancelados": "orange"
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

    with st.expander("Análisis detallado de los Estados de los Registros"):
        st.markdown(generar_analisis(frecuencia_status))