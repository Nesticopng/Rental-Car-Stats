import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

# Categorizar los datos
df["Pre_Deposito"] = df["res_prepagos"].apply(lambda x: "Hizo Pre-Depósito" if x > 0 else "No hizo Pre-Depósito")

# Contar la frecuencia de cada categoría
frecuencia_prepagos = df["Pre_Deposito"].value_counts().reset_index()
frecuencia_prepagos.columns = ["Pre_Deposito", "Count"]

# Obtener totales
total_registros = frecuencia_prepagos["Count"].sum()
hizo_pre = frecuencia_prepagos[frecuencia_prepagos["Pre_Deposito"] == "Hizo Pre-Depósito"]["Count"].sum()
no_hizo_pre = frecuencia_prepagos[frecuencia_prepagos["Pre_Deposito"] == "No hizo Pre-Depósito"]["Count"].sum()

# Calcular porcentajes
porcentaje_hizo_pre = (hizo_pre / total_registros) * 100 if total_registros > 0 else 0
porcentaje_no_hizo_pre = (no_hizo_pre / total_registros) * 100 if total_registros > 0 else 0

# Calcular el promedio de dinero gastado en pre-depósitos
promedio_predeposito = df[df["res_prepagos"] > 0]["res_prepagos"].mean()

# Crear el gráfico pie
def tasa_pregago():
    st.header("Tasa de Prepagos")

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = px.pie(
            frecuencia_prepagos, 
            names="Pre_Deposito", 
            values="Count", 
            title="Distribución de Prepagos en Reservas",
            color="Pre_Deposito",
            color_discrete_map={"Hizo Pre-Depósito": "blue", "No hizo Pre-Depósito": "#8B0000"}
        )
        st.plotly_chart(fig)

    with col2:
        st.markdown("### 📊 Datos Adicionales")

        st.divider()

        with st.container():
            if hizo_pre > 0:
                st.markdown("### 💰 Promedio de los Pre-Depósitos")
                st.header(f"**${promedio_predeposito:,.2f}**")
            else:
                st.write("⚠️ No hay registros con pre-depósito.")

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("### 📌 Total de Registros")
            st.header(f"**{total_registros:,} Registros**")

    with st.expander("Análisis detallado de Pre-Depósitos"):
        if hizo_pre == total_registros:
            st.write("🔴 **El 100% de los clientes realizaron un predepósito.** No hay registros sin prepago.")
        elif no_hizo_pre == total_registros:
            st.write("🔵 **El 100% de los clientes NO realizaron un predepósito.** No hay registros con prepago.")
        else:
            st.write(f"🔴 **{hizo_pre} clientes ({porcentaje_hizo_pre:.2f}%) hicieron un predepósito.**")
            st.write(f"🔵 **{no_hizo_pre} clientes ({porcentaje_no_hizo_pre:.2f}%) no hicieron un predepósito.**")