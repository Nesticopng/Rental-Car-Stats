import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Cargar Datos
df = cargar_datos()

# Mapeo de nombres de variables
variable_mapping = {
    "Cantidad de Rentas": "Cantidad",
    "Tarifa Básica": "TotalRate",
    "Extras Gastados": "TotalExtras",
    "Tarifa Total": "TotalBill"
}

# Contar la frecuencia de cada fuente de reserva
frecuencia_source = df["Source"].value_counts().reset_index()
frecuencia_source.columns = ["Empresa", "Cantidad de Vehículos Rentados"]

def mostrar_datos_y_analisis(data, columna, es_dinero, variable_nombre):
    top_5 = data.nlargest(5, "Cantidad de Vehículos Rentados")
    if not top_5.empty:
        mas_frecuente = top_5.iloc[0]
        valor = f"${mas_frecuente["Cantidad de Vehículos Rentados"]:,.2f}" if es_dinero else mas_frecuente["Cantidad de Vehículos Rentados"]
        st.write(f"La empresa con más {"dinero recaudado" if es_dinero else "rentas"} por **{variable_nombre}** es **{mas_frecuente[columna]}**, con un total de **{valor}**")
        if len(top_5) > 1:
            st.write("Otras empresas destacadas son:")
            for i, row in top_5.iloc[1:].iterrows():
                valor = f"${row["Cantidad de Vehículos Rentados"]:,.2f}" if es_dinero else row["Cantidad de Vehículos Rentados"]
                st.write(f"- **{row[columna]}**: {valor}.")
    else:
        st.write("No hay datos suficientes para realizar un análisis.")
    
    if es_dinero:
        st.write(top_5[["Empresa", "Dinero Recaudado ($USD)"]])
    else:
        st.write(top_5)

# Generar Gráfico
def grafica_source():
    st.header("Análisis de Rentas y Recaudación por Empresa")
    
    variable_seleccionada = st.selectbox(
        "Métrica a analizar",
        ("Cantidad de Rentas", "Tarifa Básica", "Extras Gastados", "Tarifa Total")
    )
    
    if variable_seleccionada == "Cantidad de Rentas":
        data = frecuencia_source
        es_dinero = False
    else:
        # Calcula el recaudado según la variable seleccionada
        columna_real = variable_mapping[variable_seleccionada]
        data = df.groupby("Source")[columna_real].sum().reset_index()
        data.columns = ["Empresa", "Cantidad de Vehículos Rentados"]
        data["Cantidad de Vehículos Rentados"] = data["Cantidad de Vehículos Rentados"].round(2)
        data["Dinero Recaudado ($USD)"] = data["Cantidad de Vehículos Rentados"].apply(lambda x: f"${x:,.2f}")
        es_dinero = True
        
    titulo = f"{"Dinero recaudado por " + variable_seleccionada + " según la Empresa" if es_dinero else "Rentas generadas según la Empresa"}"
        
    fig = px.bar(
        data, 
        x="Empresa", 
        y="Cantidad de Vehículos Rentados", 
        color="Empresa", 
        color_discrete_sequence=rojo(),
        title=titulo,
        text="Dinero Recaudado ($USD)" if es_dinero else "Cantidad de Vehículos Rentados",
        labels={"Cantidad de Vehículos Rentados": "Monto ($USD)" if es_dinero else "Cantidad de Vehículos Rentados", "Empresa": "Empresa"}
    )
        
    st.plotly_chart(fig)
    
    with st.expander("Análisis detallado de Empresas"):
        mostrar_datos_y_analisis(data, "Empresa", es_dinero, variable_seleccionada)