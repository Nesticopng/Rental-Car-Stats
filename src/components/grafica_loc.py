import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Cargar datos
df = cargar_datos()

def grafica_loc():
    st.header("Locaciones que más Rentas han generado")
    col1, col2, col3 = st.columns(3)

    with col1:
        datos_config_decode = st.selectbox(
                "Formato de los Datos",
                ("IATA", "Decodificados"),
        )
        
    with col2:
        config_loc_in_out = st.selectbox(
                "Selecciona el tipo de ubicación",
                ("Sitio de Entrada", "Sitio de Salida"),
        )

    with col3:
        grafica_loc = st.selectbox(
                "Clasificar por",
                ("Ciudad", "País"),
                disabled=(datos_config_decode=="IATA")
        )

        columna_analisis = "LocIn" if config_loc_in_out == "Sitio de Entrada" else "LocOut"
    
    if datos_config_decode == "IATA":
            columna_analisis = "LocIn" if config_loc_in_out == "Sitio de Entrada" else "LocOut"
            label_locacion = "Ubicación (IATA)"
    else:
        if grafica_loc == "Ciudad":
                columna_analisis = "LocInCity" if config_loc_in_out == "Sitio de Entrada" else "LocOutCity"
                label_locacion = "Ciudad"
        else:
                columna_analisis = "LocInCountry" if config_loc_in_out == "Sitio de Entrada" else "LocOutCountry"
                label_locacion = "País"
    
    # Calcular las Frecuencias
    frecuencia_loc = df[columna_analisis].value_counts().reset_index()
    frecuencia_loc.columns = ["Locación", "Cantidad"]
    
    titulo = f"Locaciones de {config_loc_in_out} que más rentas han generado."
    fig = px.bar(
        frecuencia_loc, x='Locación', y='Cantidad', color='Locación',
        color_discrete_sequence=rojo(),
        title=titulo,
        text='Cantidad',
        labels={'Cantidad': 'Cantidad de Rentas Generadas', 'Locación': label_locacion}
    )

    st.plotly_chart(fig)
    
    with st.expander(f"Análisis detallado de {config_loc_in_out}"):
        tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
        
        with tab1:
            top_5 = frecuencia_loc.nlargest(5, 'Cantidad')
            st.write("**Las 5 locaciones más frecuentes:**")
            for _, row in top_5.iterrows():
                st.write(f"- **{row['Locación']}**: {row['Cantidad']} rentas")
            st.write("\n**Tabla de Datos:**")
            st.write(top_5)
            
        with tab2:
            st.write("**Análisis estadístico:**")
            st.write(f"- **Media:** {frecuencia_loc['Cantidad'].mean():.2f}")
            st.write(f"- **Mediana:** {frecuencia_loc['Cantidad'].median():.2f}")
            st.write(f"- **Moda:** {frecuencia_loc['Cantidad'].mode().values[0]}")
            st.write(f"- **Desviación estándar:** {frecuencia_loc['Cantidad'].std():.2f}")
            st.write(f"- **Mínimo:** {frecuencia_loc['Cantidad'].min()}")
            st.write(f"- **Máximo:** {frecuencia_loc['Cantidad'].max()}")
