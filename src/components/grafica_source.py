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
    "Tarifa Total": "TotalBill",
    "Promedio de Días Rentados": "RDays"
}

# Contar la frecuencia de cada fuente de reserva
frecuencia_source = df["Source"].value_counts().reset_index()
frecuencia_source.columns = ["Empresa", "Cantidad de Vehículos Rentados"]

def mostrar_datos_y_analisis(data, columna, es_dinero, es_promedio, variable_nombre):
    top_5 = data.nlargest(5, "Cantidad de Vehículos Rentados")

    if not top_5.empty:
        mas_frecuente = top_5.iloc[0]
        if es_dinero:
            valor = f"${mas_frecuente['Cantidad de Vehículos Rentados']:,.2f}"
        elif es_promedio:
            valor = f"{mas_frecuente['Cantidad de Vehículos Rentados']:.2f} días"
        else:
            valor = mas_frecuente["Cantidad de Vehículos Rentados"]

        descripcion = "dinero recaudado" if es_dinero else "días rentados en promedio" if es_promedio else "rentas"
        st.write(f"La empresa con más {descripcion} por **{variable_nombre}** es **{mas_frecuente[columna]}**, con un total de **{valor}**.")

        if len(top_5) > 1:
            st.write("Otras empresas destacadas son:")
            for i, row in top_5.iloc[1:].iterrows():
                if es_dinero:
                    valor = f"${row['Cantidad de Vehículos Rentados']:,.2f}"
                elif es_promedio:
                    valor = f"{row['Cantidad de Vehículos Rentados']:.2f} días"
                else:
                    valor = row["Cantidad de Vehículos Rentados"]
                st.write(f"- **{row[columna]}**: {valor}.")

    else:
        st.write("No hay datos suficientes para realizar un análisis.")
    
    if es_dinero:
        columnas_a_mostrar = ["Empresa", "Dinero Recaudado ($USD)"]
    elif es_promedio:
        columnas_a_mostrar = ["Empresa", "Promedio de Días Rentados"]
    else:
        columnas_a_mostrar = ["Empresa", "Cantidad de Vehículos Rentados"]

    st.write(top_5[columnas_a_mostrar])

# Generar Gráfico
def grafica_source():
    st.header("Análisis de Rentas y Recaudación por Empresa")
    
    variable_seleccionada = st.selectbox(
        "Métrica a analizar",
        ("Cantidad de Rentas", "Tarifa Básica", "Extras Gastados", "Tarifa Total", "Promedio de Días Rentados")
    )

    if variable_seleccionada == "Cantidad de Rentas":
        data = frecuencia_source
        es_dinero = False
        es_promedio = False
    elif variable_seleccionada == "Promedio de Días Rentados":
        columna_real = variable_mapping[variable_seleccionada]
        data = df.groupby("Source")[columna_real].mean().reset_index()
        data.columns = ["Empresa", "Cantidad de Vehículos Rentados"]
        data["Cantidad de Vehículos Rentados"] = data["Cantidad de Vehículos Rentados"].round(2)
        data["Promedio de Días Rentados"] = data["Cantidad de Vehículos Rentados"].apply(lambda x: f"{x:.2f} días")
        es_dinero = False
        es_promedio = True
    else:
        columna_real = variable_mapping[variable_seleccionada]
        data = df.groupby("Source")[columna_real].sum().reset_index()
        data.columns = ["Empresa", "Cantidad de Vehículos Rentados"]
        data["Cantidad de Vehículos Rentados"] = data["Cantidad de Vehículos Rentados"].round(2)
        data["Dinero Recaudado ($USD)"] = data["Cantidad de Vehículos Rentados"].apply(lambda x: f"${x:,.2f}")
        es_dinero = True
        es_promedio = False
        
    titulo = (
        f"Promedio de Días Rentados según la Empresa" if es_promedio else
        f"Dinero recaudado por {variable_seleccionada} según la Empresa" if es_dinero else
        "Rentas generadas según la Empresa"
    )

    fig = px.bar(
        data, 
        x="Empresa", 
        y="Cantidad de Vehículos Rentados", 
        color="Empresa", 
        color_discrete_sequence=rojo(),
        title=titulo,
        text="Promedio de Días Rentados" if es_promedio else "Dinero Recaudado ($USD)" if es_dinero else "Cantidad de Vehículos Rentados",
        labels={
            "Cantidad de Vehículos Rentados": "Días Promedio" if es_promedio else "Monto ($USD)" if es_dinero else "Cantidad de Vehículos Rentados", 
            "Empresa": "Empresa"
        }
    )
        
    st.plotly_chart(fig)
    
    with st.expander("Análisis detallado de Empresas"):
        mostrar_datos_y_analisis(data, "Empresa", es_dinero, es_promedio, variable_seleccionada)