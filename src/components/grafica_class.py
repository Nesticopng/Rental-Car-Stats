import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.decodificar_class import obtener_decodificacion
from src.utils.paleta_rojo import rojo

# Cargar datos
df = cargar_datos()

# Mapeo entre nombres en español y nombres reales en el DataFrame
column_mapping = {
    "Clasificación": "Class",
    "Categoría": "Category",
    "Tipo de Vehículo": "Type",
    "Transmisión": "Transmission",
    "Combustible y Aire": "Fuel"
}

# Mapeo de nombres de variables
gasto_mapping = {
    "Tarifa Básica": "TotalRate",
    "Gasto Diario": "AvgRateDay",
    "Extras Gastados": "TotalExtras",
    "Tarifa Total": "TotalBill"
}

# Inversa de las Variables (Para el Título)
gasto_mapping_es = {
    "TotalRate": "Tarifa Básica",
    "AvgRateDay": "Gasto Diario",
    "TotalExtras": "Extras Gastados",
    "TotalBill": "Tarifa Total"
}

# Decodificar datos de Class
def decodificar_datos(df, decodificacion, aplicar):
    if aplicar == "Sí":
        for col, mapping in decodificacion.items():
            if col in df.columns:
                df[col] = df[col].map(mapping).fillna(df[col])
    return df

# Configuraciones de la Gráfica
def generar_grafico(df, columna, titulo, eje_x, metrica):
    if metrica == "Vehículos Rentados":
        y_axis = "Cantidad"
        text_col = "Cantidad"
        y_label = "Vehículos Rentados"
    else:
        df["Gasto Promedio ($USD)"] = df["Promedio"].apply(lambda x: f"${x:,.2f}")
        y_axis = "Promedio"
        text_col = "Gasto Promedio ($USD)"
        y_label = "Gasto Promedio ($USD)"
    
    fig = px.bar(
        df, x=columna, y=y_axis, color=columna,
        color_discrete_sequence=rojo(),
        title=titulo, text=text_col
    )

    fig.update_layout(xaxis_title=eje_x, yaxis_title=y_label)

    st.plotly_chart(fig)

# Análisis Automatizado
def mostrar_analisis(data, columna, nombre, metrica):
    top = data.nlargest(5, "Cantidad" if metrica == "Vehículos Rentados" else "Promedio")
    data_analisis_renombrada = top.rename(columns={columna: f"{nombre}"})

    st.write(f"**Análisis de {nombre}:**")

    for _, row in top.iterrows():
        valor = f"{row["Cantidad"]} vehículos rentados" if metrica == "Vehículos Rentados" else f"${row["Promedio"]:,.2f} en promedio"
        st.write(f"- **{row[columna]}**: {valor}")

    if metrica == "Gasto Promedio ($USD)":
        data_analisis_renombrada = data_analisis_renombrada.drop(columns=["Promedio"])

    st.write(data_analisis_renombrada)

def grafica_vehiculos():
    st.header("Análisis de Vehículos Rentados")

    df = cargar_datos()

    decodificacion = obtener_decodificacion()
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        grafica_config_es = st.selectbox("Variable a analizar", column_mapping.keys())
    with col2:
        datos_config = st.selectbox("Mostrar datos decodificados", ("Sí", "No"), disabled=(grafica_config_es == "Clasificación"))
    with col3:
        metrica = st.selectbox("Métrica a analizar", ("Vehículos Rentados", "Gasto Promedio ($USD)"))
    
    grafica_config = column_mapping[grafica_config_es]

    df = decodificar_datos(df, decodificacion, datos_config)
    
    if metrica == "Vehículos Rentados":
        datos_analisis = df[grafica_config].value_counts().reset_index()
        datos_analisis.columns = [grafica_config, "Cantidad"]
    else:
        variable_seleccionada = st.selectbox("Variable de gasto", gasto_mapping.keys())
        variable_seleccionada = gasto_mapping[variable_seleccionada]
        datos_analisis = df.groupby(grafica_config)[variable_seleccionada].mean().round(2).reset_index()
        datos_analisis.columns = [grafica_config, "Promedio"]
        variable_seleccionada_es = gasto_mapping_es[variable_seleccionada]
    
    # Título Dinámico
    titulo = (f"Análisis de {metrica} de {variable_seleccionada_es} según {grafica_config_es} "
          if metrica == "Gasto Promedio ($USD)"
          else f"Análisis de {metrica} según {grafica_config_es}")

    # Generar Gráfico y Análisis
    generar_grafico(datos_analisis, grafica_config, titulo, grafica_config_es, metrica)
    
    with st.expander("Detalles y Análisis"):
        mostrar_analisis(datos_analisis, grafica_config, grafica_config_es, metrica)