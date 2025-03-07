import streamlit as st
from src.utils.helpers import cargar_datos
import plotly.express as px

# Configuraciones Gráfica Vehiculos según su Class
reds = [
    '#2A0000', '#450A0A', '#5F1A1A', '#7A2A2A', '#8B0000', '#A52A2A', '#B71C1C', 
    '#C62828', '#D32F2F', '#D84315', '#E53935', '#EF5350', '#F44336', '#E57373', 
    '#EF9A9A', '#FF6F61', '#FF8A80', '#FFAB91', '#FFCDD2', '#FFEBEE'
]

# Cargar datos
df = cargar_datos()

# Diccionarios de decodificación
decodificacion_categoria = {
    'M': 'Mini', 'N': 'Mini Elite', 'E': 'Económico', 'H': 'Económico Elite',
    'C': 'Compacto', 'D': 'Compacto Elite', 'I': 'Intermedio', 'J': 'Intermedio Elite',
    'S': 'Estándar', 'R': 'Estándar Elite', 'F': 'Tamaño completo', 'G': 'Tamaño completo Elite',
    'P': 'Premium', 'U': 'Premium Elite', 'L': 'Lujo', 'W': 'Lujo Elite', 'O': 'Tamaño extra', 'X': 'Especial'
}

decodificacion_tipo = {
    'B': '2-3 Puertas', 'C': '2-4 Puertas', 'D': '4-5 Puertas', 'W': 'Camioneta/Wagon',
    'V': 'Van de pasajeros', 'L': 'Limusina/Sedán', 'S': 'Deportivo', 'T': 'Convertible',
    'F': 'SUV', 'J': 'Todo Terreno', 'X': 'Especial', 'P': 'Pick Up (cabina simple/extendida) 2 puertas',
    'Q': 'Pick Up (doble cabina) 4 puertas', 'Z': 'Oferta especial', 'E': 'Coupé', 'M': 'Monoplaza',
    'R': 'Vehículo recreativo', 'H': 'Autocaravana', 'Y': 'Vehículo de 2 ruedas', 'N': 'Roadster',
    'G': 'Crossover', 'K': 'Van/Camión comercial'
}

decodificacion_transmision = {
    'M': 'Sincrónico (tracción no especificada)', 'N': 'Sincrónico 4WD', 'C': 'Sincrónico AWD',
    'A': 'Automático (tracción no especificada)', 'B': 'Automático 4WD', 'D': 'Automático AWD'
}

decodificacion_fuel = {
    'R': 'Combustible/Energía no especificada con aire', 'N': 'Combustible/Energía no especificada sin aire',
    'D': 'Diésel con aire', 'Q': 'Diésel sin aire', 'H': 'Híbrido con aire', 'I': 'Híbrido enchufable con aire',
    'E': 'Eléctrico', 'C': 'Eléctrico', 'L': 'Gas licuado (GLP) con aire', 'S': 'Gas licuado (GLP) sin aire',
    'A': 'Hidrógeno con aire', 'A': 'Hidrógeno sin aire', 'M': 'Múltiples combustibles/energías con aire',
    'F': 'Múltiples combustibles/energías sin aire', 'V': 'Gasolina con aire', 'Z': 'Gasolina sin aire',
    'U': 'Etanol con aire', 'X': 'Etanol sin aire'
}


def grafica_class():
    col1, col2 = st.columns(2)

    with col1:
        grafica_config = st.selectbox(
                "Elementos de la Clasificación",
                ("Todos", "Categoría", "Tipo", "Transmisión", "Combustible y Aire Acondicionado"),
        )

    with col2:
        datos_config = st.selectbox(
                "Datos",
                ("Decodificados", "Originales"),
                disabled=(grafica_config == "Todos")
        )

    # Crear una copia del DataFrame para no modificar el original
    df_analisis = df.copy()

    # Decodificar las columnas si es necesario
    if datos_config == "Decodificados":
        df_analisis['Category'] = df_analisis['Category'].map(decodificacion_categoria).fillna(df_analisis['Category'])
        df_analisis['Type'] = df_analisis['Type'].map(decodificacion_tipo).fillna(df_analisis['Type'])
        df_analisis['Transmission'] = df_analisis['Transmission'].map(decodificacion_transmision).fillna(df_analisis['Transmission'])
        df_analisis['Fuel'] = df_analisis['Fuel'].map(decodificacion_fuel).fillna(df_analisis['Fuel'])

    # Recalcular frecuencias
    frecuencia_class = df_analisis['Class'].value_counts().reset_index()
    frecuencia_class.columns = ['Class', 'Count']

    frecuencia_category = df_analisis['Category'].value_counts().reset_index()
    frecuencia_category.columns = ['Category', 'Count']

    frecuencia_type = df_analisis['Type'].value_counts().reset_index()
    frecuencia_type.columns = ['Type', 'Count']

    frecuencia_transmission = df_analisis['Transmission'].value_counts().reset_index()
    frecuencia_transmission.columns = ['Transmission', 'Count']

    frecuencia_fuel = df_analisis['Fuel'].value_counts().reset_index()
    frecuencia_fuel.columns = ['Fuel', 'Count']

    # Función para mostrar datos con más coincidencias y análisis textual
    def mostrar_datos_y_analisis(data, columna, nombre_columna, datos_originales, mostrar_originales=True):
        top_5 = data.nlargest(5, 'Count')

        # Agregar columna con datos originales si es necesario
        if mostrar_originales:
            top_5['Original'] = top_5[columna].map(datos_originales)

        # Análisis textual automatizado
        st.write("**Análisis:**")
        if not top_5.empty:
            mas_frecuente = top_5.iloc[0]
            if mostrar_originales:
                st.write(f"La categoría más frecuente es **{mas_frecuente[columna]}** ({mas_frecuente['Original']}), con un total de **{mas_frecuente['Count']}** vehículos rentados.")
            else:
                st.write(f"La categoría más frecuente es **{mas_frecuente[columna]}**, con un total de **{mas_frecuente['Count']}** vehículos rentados.")
            if len(top_5) > 1:
                st.write(f"Otras categorías destacadas son:")
                for i, row in top_5.iloc[1:].iterrows():
                    if mostrar_originales:
                        st.write(f"- **{row[columna]}** ({row['Original']}): {row['Count']} vehículos rentados.")
                    else:
                        st.write(f"- **{row[columna]}**: {row['Count']} vehículos rentados.")
        else:
            st.write("No hay datos suficientes para realizar un análisis.")

        st.write(f"**Tabla de Datos con más coincidencias en {nombre_columna}:**")
        if mostrar_originales:
            st.write(top_5[[columna, 'Original', 'Count']])  # Mostrar solo las columnas relevantes
        else:
            st.write(top_5[[columna, 'Count']])  # Mostrar solo las columnas relevantes

    # Función para generar análisis estadístico
    def generar_analisis_estadistico(data, columna):
        st.write(f"**Análisis estadístico:**")
        st.write(f"- **Media:** {data[columna].mean():.2f}")
        st.write(f"- **Mediana:** {data[columna].median():.2f}")
        st.write(f"- **Moda:** {data[columna].mode().values[0]}")
        st.write(f"- **Desviación estándar:** {data[columna].std():.2f}")
        st.write(f"- **Mínimo:** {data[columna].min()}")
        st.write(f"- **Máximo:** {data[columna].max()}")

    if grafica_config == "Todos":
        fig = px.bar(frecuencia_class, x='Class', y='Count', color='Class',
                    color_discrete_sequence=reds,
                    title='Vehículos más rentados según su clasificación.',
                    text='Count',
                    labels={'Count': 'Cantidad de Vehículos Rentados', 'Class': 'Clasificación'})
        st.plotly_chart(fig)

        with st.expander("Análisis detallado de Clasificación"):
            tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
            with tab1:
                mostrar_datos_y_analisis(frecuencia_class, 'Class', 'Clasificación', {v: k for k, v in decodificacion_categoria.items()}, mostrar_originales=False)
            with tab2:
                generar_analisis_estadistico(frecuencia_class, 'Count')

    if grafica_config == "Categoría":
        fig = px.bar(frecuencia_category, x='Category', y='Count', color='Category',
                    color_discrete_sequence=reds,
                    title='Vehículos más rentados según su Categoría.',
                    text='Count',
                    labels={'Count': 'Cantidad de Vehículos Rentados', 'Category': 'Categoría'})
        st.plotly_chart(fig)

        with st.expander("Análisis detallado de Categoría"):
            tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
            with tab1:
                mostrar_datos_y_analisis(frecuencia_category, 'Category', 'Categoría', {v: k for k, v in decodificacion_categoria.items()}, mostrar_originales=(datos_config == "Decodificados"))
            with tab2:
                generar_analisis_estadistico(frecuencia_category, 'Count')

    if grafica_config == "Tipo":
        fig = px.bar(frecuencia_type, x='Type', y='Count', color='Type',
                    color_discrete_sequence=reds,
                    title='Vehículos más rentados según su Tipo.',
                    text='Count',
                    labels={'Count': 'Cantidad de Vehículos Rentados', 'Type': 'Tipo'})
        st.plotly_chart(fig)

        with st.expander("Análisis detallado de Tipo"):
            tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
            with tab1:
                mostrar_datos_y_analisis(frecuencia_type, 'Type', 'Tipo', {v: k for k, v in decodificacion_tipo.items()}, mostrar_originales=(datos_config == "Decodificados"))
            with tab2:
                generar_analisis_estadistico(frecuencia_type, 'Count')

    if grafica_config == "Transmisión":
        fig = px.bar(frecuencia_transmission, x='Transmission', y='Count', color='Transmission',
                    color_discrete_sequence=reds,
                    title='Vehículos más rentados según su Transmisión.',
                    text='Count',
                    labels={'Count': 'Cantidad de Vehículos Rentados', 'Transmission': 'Transmisión'})
        st.plotly_chart(fig)

        with st.expander("Análisis detallado de Transmisión"):
            tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
            with tab1:
                mostrar_datos_y_analisis(frecuencia_transmission, 'Transmission', 'Transmisión', {v: k for k, v in decodificacion_transmision.items()}, mostrar_originales=(datos_config == "Decodificados"))
            with tab2:
                generar_analisis_estadistico(frecuencia_transmission, 'Count')

    if grafica_config == "Combustible y Aire Acondicionado":
        fig = px.bar(frecuencia_fuel, x='Fuel', y='Count', color='Fuel',
                    color_discrete_sequence=reds,
                    title='Vehículos más rentados según su Combustible y Aire Acondicionado.',
                    text='Count',
                    labels={'Count': 'Cantidad de Vehículos Rentados', 'Fuel': 'Combustible y Aire Acondicionado'})
        st.plotly_chart(fig)

        with st.expander("Análisis detallado de Combustible y Aire Acondicionado"):
            tab1, tab2 = st.tabs(["Datos y Análisis", "Estadísticas"])
            with tab1:
                mostrar_datos_y_analisis(frecuencia_fuel, 'Fuel', 'Combustible y Aire Acondicionado', {v: k for k, v in decodificacion_fuel.items()}, mostrar_originales=(datos_config == "Decodificados"))
            with tab2:
                generar_analisis_estadistico(frecuencia_fuel, 'Count')