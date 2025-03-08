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

def decodificar_datos(df, decodificacion, aplicar):
    if aplicar == "Sí":
        for col, mapping in decodificacion.items():
            if col in df.columns:
                df[col] = df[col].map(mapping).fillna(df[col])
    return df

def generar_grafico(df, columna, titulo, eje_x):
    fig = px.bar(
        df,
        x=columna, 
        y='Count', color=columna,
        color_discrete_sequence=rojo(),
        title=titulo, text='Count')
    
    fig.update_layout(
        xaxis_title=eje_x,
        yaxis_title="Vehículos Rentados"
    )

    st.plotly_chart(fig)

def mostrar_analisis(data, columna, nombre):
    top = data.nlargest(5, 'Count')
    st.write(f"**Análisis de {nombre}:**")
    for _, row in top.iterrows():
        st.write(f"- **{row[columna]}**: {row['Count']} vehículos rentados")
    st.write(f"**Tabla de datos:**")
    st.write(top)

def grafica_class():
    st.header("Vehículos más Rentados según su Clasificación")
    df = cargar_datos()
    decodificacion = obtener_decodificacion()
    
    col1, col2 = st.columns(2)
    with col1:
        grafica_config_es = st.selectbox(
                    "Elemento a analizar", 
                    ("Clasificación", "Categoría", "Tipo de Vehículo", "Transmisión", "Combustible y Aire")
        )
    
    with col2:
        datos_config = st.selectbox(
                    "Mostrar datos decodificados", 
                    ("Sí", "No"),
                    disabled=(grafica_config_es=="Clasificación")
        )
    
    # Convertir el nombre en español al nombre real de la columna en df
    grafica_config = column_mapping[grafica_config_es]

    df = decodificar_datos(df, decodificacion, datos_config)
    frecuencia = df[grafica_config].value_counts().reset_index()
    frecuencia.columns = [grafica_config, 'Count']
    
    generar_grafico(frecuencia, grafica_config, f'Vehículos mas rentados según su {grafica_config_es}', grafica_config_es)
    
    with st.expander("Detalles y Análisis"):
        mostrar_analisis(frecuencia, grafica_config, grafica_config_es)