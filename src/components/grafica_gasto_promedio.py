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
variable_mapping = {
    "Tarifa Básica": "TotalRate",
    "Gasto Diario": "AvgRateDay",
    "Extras Gastados": "TotalExtras",
    "Tarifa Total": "TotalBill"
}

def decodificar_datos(df, decodificacion, aplicar):
    if aplicar == "Sí":
        for col, mapping in decodificacion.items():
            if col in df.columns:
                df[col] = df[col].map(mapping).fillna(df[col])
    return df

def generar_grafico(df, columna, titulo, eje_x):
    df["Promedio Formateado"] = df["Promedio"].apply(lambda x: f"${x}")

    fig = px.bar(
        df,
        x=columna, 
        y="Promedio",  
        color=columna,
        color_discrete_sequence=rojo(),
        title=titulo,
        text="Promedio Formateado",
        hover_data={columna: True, "Promedio Formateado": True}
    )

    fig.update_layout(
        xaxis_title=eje_x,
        yaxis_title="Gasto Promedio ($USD)"
    )

    st.plotly_chart(fig)

def mostrar_analisis(data, columna, nombre, variable_nombre):
    top = data.nlargest(5, 'Promedio')
    st.write(f"**Análisis de {nombre} basado en {variable_nombre}:**")
    for _, row in top.iterrows():
        st.write(f"- **{row[columna]}**: ${row['Promedio']} en promedio")
    st.write(f"**Tabla de datos:**")
    st.write(top)

def grafica_gasto_promedio():
    st.header("Análisis de Variables de Gasto")

    df = cargar_datos()
    decodificacion = obtener_decodificacion()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        grafica_config_es = st.selectbox(
            "Elemento a analizar", 
            ("Clasificación", "Categoría", "Tipo de Vehículo", "Transmisión", "Combustible y Aire"),
            key="grafica_config_es"
        )
    
    with col2:
        datos_config = st.selectbox(
            "Mostrar datos decodificados", 
            ("Sí", "No"),
            disabled=(grafica_config_es == "Clasificación"),
            key="datos_config"
        )
    
    with col3:
        variable_seleccionada = st.selectbox(
            "Variable a analizar",
            ("Tarifa Básica", "Gasto Diario", "Extras Gastados", "Tarifa Total"),
            key="variable_seleccionada"
        )

    grafica_config = column_mapping[grafica_config_es]
    variable_seleccionada = variable_mapping[variable_seleccionada]

    df = decodificar_datos(df, decodificacion, datos_config)
    
    # Calcular el promedio de la variable seleccionada
    promedio_variable = df.groupby(grafica_config)[variable_seleccionada].mean().round(2).reset_index()
    promedio_variable.columns = [grafica_config, 'Promedio']

    generar_grafico(
        promedio_variable, 
        grafica_config, 
        f'Promedio de {variable_seleccionada} por {grafica_config_es}', 
        grafica_config_es
    )
    
    with st.expander("Detalles y Análisis"):
        mostrar_analisis(promedio_variable, grafica_config, grafica_config_es, variable_seleccionada)