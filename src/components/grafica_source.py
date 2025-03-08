import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Cargar Datos
df = cargar_datos()

# Contar la frecuencia de cada fuente de reserva
frecuencia_source = df['Source'].value_counts().reset_index()
frecuencia_source.columns = ['Source', 'Count']

def mostrar_datos_y_analisis(data, columna):
    top_5 = data.nlargest(5, 'Count')
    if not top_5.empty:
        mas_frecuente = top_5.iloc[0]
        st.write(f"La empresa con más rentas es **{mas_frecuente[columna]}**, con un total de **{mas_frecuente['Count']}** vehículos rentados.")
        if len(top_5) > 1:
            st.write("Otras empresas destacadas son:")
            for i, row in top_5.iloc[1:].iterrows():
                st.write(f"- **{row[columna]}**: {row['Count']} vehículos rentados.")
    else:
        st.write("No hay datos suficientes para realizar un análisis.")
    
    st.write(f"**Tabla de Datos con más coincidencias en {columna}:**")
    st.write(top_5)

# Crear el gráfico de barras
def grafica_source():
    st.header("Empresas que más Rentas han generado")
    
    fig = px.bar(
        frecuencia_source, 
        x='Source', 
        y='Count', 
        color='Source', 
        color_discrete_sequence=rojo(),
        title='Empresas que Más Rentas han Generado',
        text='Count',
        labels={'Count': 'Cantidad de Vehículos Rentados', 'Source': 'Empresa'}
    )

    st.plotly_chart(fig)

    with st.expander("Análisis detallado de Empresas"):
        mostrar_datos_y_analisis(frecuencia_source, 'Source')