import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

# Categorizar los datos
df["Pre_Deposito"] = df["res_prepagos"].apply(lambda x: "Hizo Pre-Depósito" if x > 0 else "No hizo Pre-Depósito")

# Contar la frecuencia de cada categoría
frecuencia_prepagos = df["Pre_Deposito"].value_counts().reset_index()
frecuencia_prepagos.columns = ["Pre_Deposito", "Cantidad"]

# Obtener totales
total_registros = frecuencia_prepagos["Cantidad"].sum()
hizo_pre = frecuencia_prepagos[frecuencia_prepagos["Pre_Deposito"] == "Hizo Pre-Depósito"]["Cantidad"].sum()
no_hizo_pre = frecuencia_prepagos[frecuencia_prepagos["Pre_Deposito"] == "No hizo Pre-Depósito"]["Cantidad"].sum()

# Calcular porcentajes
porcentaje_hizo_pre = (hizo_pre / total_registros) * 100 if total_registros > 0 else 0
porcentaje_no_hizo_pre = (no_hizo_pre / total_registros) * 100 if total_registros > 0 else 0

# Calcular el promedio de dinero gastado en pre-depósitos
promedio_predeposito = df[df["res_prepagos"] > 0]["res_prepagos"].mean()

# Función para generar el análisis dinámico
def generar_analisis_prepagos():
    analisis = []
    
    if hizo_pre == total_registros:
        analisis.append("🔴 **El 100% de los clientes realizaron un predepósito.** Esto indica una política estricta de prepago o alta confianza en el modelo de pago anticipado.")
    elif no_hizo_pre == total_registros:
        analisis.append("🟢 **El 100% de los clientes NO realizaron un predepósito.** Esto puede indicar que el prepago no es un requisito o que los clientes prefieren pagar al momento del alquiler.")
    else:
        analisis.append(f"🔴 **{hizo_pre} clientes ({porcentaje_hizo_pre:.2f}%) hicieron un predepósito.** Esto puede reflejar confianza en el sistema o la necesidad de garantizar reservas.")
        analisis.append(f"🟢 **{no_hizo_pre} clientes ({porcentaje_no_hizo_pre:.2f}%) no hicieron un predepósito.** Esto sugiere que hay clientes que prefieren pagar en el momento de la renta o que no se les exige el pago anticipado.")
    
    # Interpretaciones adicionales según tendencias
    if porcentaje_hizo_pre > 70:
        analisis.append("✅ **Alta adopción del predepósito:** Un alto porcentaje de clientes realiza prepago, lo que indica que esta opción es popular y puede mejorar el flujo de caja.")
    elif porcentaje_no_hizo_pre > 70:
        analisis.append("⚠️ **Baja adopción del predepósito:** La mayoría de los clientes no usan el prepago, lo que podría indicar resistencia al pago anticipado o falta de incentivos.")
    
    if promedio_predeposito > 100:
        analisis.append(f"💰 **El promedio de predepósito es alto (${promedio_predeposito:,.2f}).** Esto indica que los clientes están dispuestos a adelantar una cantidad significativa por la reserva.")
    elif promedio_predeposito < 50 and promedio_predeposito > 0:
        analisis.append(f"🔎 **El promedio de predepósito es bajo (${promedio_predeposito:,.2f}).** Puede ser un indicador de que los clientes solo pagan montos mínimos por adelantado.")

    return analisis

# Generar el gráfico pie
def tasa_pregago():
    st.header("Tasa de Porcentual de los Pre-Depósitos")

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = px.pie(
            frecuencia_prepagos, 
            names="Pre_Deposito", 
            values="Cantidad", 
            title="Distribución de Prepagos en Reservas",
            color="Pre_Deposito",
            color_discrete_map={"Hizo Pre-Depósito": "green", "No hizo Pre-Depósito": "#8B0000"}
        )
        st.plotly_chart(fig)

    with col2:
        with st.container(border=True):
            st.markdown("### 📊 Datos Adicionales")

            st.divider()

            with st.container():
                if hizo_pre > 0:
                    st.markdown("### 💲 Promedio de los Pre-Depósitos")
                    st.header(f"**${promedio_predeposito:,.2f}**")
                else:
                    st.write("⚠️ No hay registros con pre-depósito.")

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("### 📌 Total de Registros")
                st.header(f"**{total_registros:,} Registros**")

    with st.expander("Análisis detallado de los Pre-Depósitos"):
        for linea in generar_analisis_prepagos():
            st.write(linea)