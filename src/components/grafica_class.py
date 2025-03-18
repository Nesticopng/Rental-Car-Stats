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
    elif metrica == "Gasto Promedio ($USD)":
        df["Gasto Promedio ($USD)"] = df["Promedio"].apply(lambda x: f"${x:,.2f}")
        y_axis = "Promedio"
        text_col = "Gasto Promedio ($USD)"
        y_label = "Gasto Promedio ($USD)"
    else:
        df["Promedio de Días Rentados"] = df["Promedio"].astype(int).apply(lambda x: f"{x} días")
        y_axis = "Promedio"
        text_col = "Promedio de Días Rentados"
        y_label = "Promedio de Días Rentados"
    
    fig = px.bar(
        df, x=columna, y=y_axis, color=columna,
        color_discrete_sequence=rojo(),
        title=titulo, text=text_col
    )

    fig.update_layout(xaxis_title=eje_x, yaxis_title=y_label)

    st.plotly_chart(fig)

# Análisis Automatizado
def mostrar_analisis(data, columna, nombre, metrica):
    st.write("### Análisis Estadístico")

    data_tabla = data.rename(columns={columna: f"{nombre}"})

    # Análisis estadístico
    total_registros = len(data)
    media = data.iloc[:, 1].mean()
    mediana = data.iloc[:, 1].median()
    desviacion = data.iloc[:, 1].std()
    max_valor = data.iloc[:, 1].max()
    min_valor = data.iloc[:, 1].min()
    top_categoria = data.iloc[0, 0]
    min_categoria = data.iloc[0,-1]
    top_valor = data.iloc[0, 1]
    min_indice = data.iloc[:, -1].idxmin()
    min_categoria = data.iloc[min_indice, 0]

    st.write(f"📊 **Total de registros analizados:** {total_registros:,}")
    st.write(f"📈 **Promedio de {metrica}:** {media:,.2f}")
    st.write(f"📊 **Mediana de {metrica}:** {mediana:,.2f}")
    st.write(f"📉 **Desviación estándar de {metrica}:** {desviacion:,.2f}")
    if metrica == "Vehículos Rentados":
        st.write(f"🔽 **Los Vehículos menos demandados son:** {min_categoria} con {min_valor:,} resgistros")
        st.write(f"🏆 **Los Vehículos más demandados son:** {top_categoria} con {max_valor:,} resgistros")

    else:
        st.write(f"🔝 **Mayor {metrica}:** {top_categoria} con {top_valor:,.2f}")
        st.write(f"🔽 **Menor valor registrado:** {min_valor:,.2f}")
        st.write(f"🏆 **Mayor valor registrado:** {max_valor:,.2f}")
        
    # Interpretaciones
    if desviacion > media * 0.5:
        st.write("⚠️ **Alta variabilidad:** Existen grandes diferencias entre categorías en esta métrica.")

    else:
        st.write("✅ **Distribución estable:** No hay grandes diferencias extremas en la métrica analizada.")
    
    if max_valor > media * 1.5:
        st.write(f"🚀 **{top_categoria} tiene valores significativamente superiores a la media.**")
    
    if min_valor < media * 0.5:
        st.write("🔻 **Algunas categorías están muy por debajo del promedio.**")
    
    data_tabla = data.rename(columns={columna: f"{nombre}"})

    if metrica in ["Gasto Promedio ($USD)", "Promedio de Días Rentados"]:
        data_tabla = data_tabla.drop(columns=["Promedio"])

    st.write("### Tabla de Datos")
    st.write(data_tabla)


def grafica_vehiculos():
    st.header("Análisis de Vehículos Rentados")

    df = cargar_datos()

    decodificacion = obtener_decodificacion()
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        grafica_config_es = st.selectbox(
            "Variable a analizar",
            column_mapping.keys()
        )

    with col2:
        datos_config = st.selectbox(
            "Mostrar datos decodificados", 
            ("Sí", "No"),
            disabled=(grafica_config_es == "Clasificación")
        )

    with col3:
        metrica = st.selectbox(
            "Métrica a analizar", 
            ("Vehículos Rentados", "Gasto Promedio ($USD)", "Promedio de Días Rentados")
        )
    
    grafica_config = column_mapping[grafica_config_es]

    df = decodificar_datos(df, decodificacion, datos_config)
    
    if metrica == "Vehículos Rentados":
        datos_analisis = df[grafica_config].value_counts().reset_index()
        datos_analisis.columns = [grafica_config, "Cantidad"]

    elif metrica == "Gasto Promedio ($USD)":
        variable_seleccionada = st.selectbox("Variable de gasto", gasto_mapping.keys())
        variable_seleccionada = gasto_mapping[variable_seleccionada]
        datos_analisis = df.groupby(grafica_config)[variable_seleccionada].mean().round(2).reset_index()
        datos_analisis.columns = [grafica_config, "Promedio"]
        variable_seleccionada_es = gasto_mapping_es[variable_seleccionada]
        
    else:
        datos_analisis = df.groupby(grafica_config)["RDays"].mean().round(2).reset_index()
        datos_analisis.columns = [grafica_config, "Promedio"]
    
    # Título Dinámico
    titulo = (f"Análisis de {metrica} de {variable_seleccionada_es} según {grafica_config_es} "
          if metrica == "Gasto Promedio ($USD)"
          else f"Análisis de {metrica} según {grafica_config_es}")

    # Generar Gráfico y Análisis
    generar_grafico(datos_analisis, grafica_config, titulo, grafica_config_es, metrica)
    
    with st.expander("Análisis Detallado"):
        mostrar_analisis(datos_analisis, grafica_config, grafica_config_es, metrica)