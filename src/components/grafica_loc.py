import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Cargar datos
df = cargar_datos()

# Análisis Automatizado
def generar_analisis(data, metrica):
    top_5 = data.nlargest(5, "Valor") if metrica == "Dinero Generado (USD)" else data.nlargest(5, "Cantidad de Rentas")

    analisis_texto = f"### Las 5 Locaciones con mayor **{metrica}:**\n\n"

    for i, row in top_5.iterrows():
        valor_formateado = f"{row['Cantidad de Rentas']:,.0f}" if metrica == "Cantidad de Rentas" else row["Dinero Generado ($USD)"]
        analisis_texto += f"- **{row['Locación']}**: {valor_formateado}\n"

    st.markdown(f"{analisis_texto}")

    columnas_a_mostrar = ["Locación", "Cantidad de Rentas"] if metrica == "Cantidad de Rentas" else ["Locación", "Dinero Generado ($USD)"]

    st.write("### Tabla de Datos")
    st.write(data[columnas_a_mostrar])

def grafica_loc():
    st.header("Análisis de Locaciones")

    # Filtros
    col1, col2, col3, col4 = st.columns(4)

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
            disabled=(datos_config_decode == "IATA")
        )

    with col4:
        metrica = st.selectbox(
            "Métrica a analizar",
            ("Cantidad de Rentas", "Dinero Generado (USD)")
        )

    # Definir la columna de ubicación según las selecciones
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

    # Calcular métrica seleccionada
    if metrica == "Cantidad de Rentas":
        data = df[columna_analisis].value_counts().reset_index()
        data.columns = ["Locación", "Cantidad de Rentas"]
        data = data.sort_values(by="Cantidad de Rentas", ascending=False)
        columna_valor = "Cantidad de Rentas"
        texto_valor = "Cantidad de Rentas"
    else:
        data = df.groupby(columna_analisis)["TotalBill"].sum().reset_index()
        data.columns = ["Locación", "Valor"]
        data = data.sort_values(by="Valor", ascending=False)
        data["Dinero Generado ($USD)"] = data["Valor"].apply(lambda x: f"${x:,.2f}")
        columna_valor = "Valor"  
        texto_valor = "Dinero Generado ($USD)"

    # Título dinámico
    titulo = f"{metrica} según Locaciones de {config_loc_in_out}"

    # Configuración del Gráfico
    fig = px.bar(
        data, x="Locación", y=columna_valor, color="Locación",
        color_discrete_sequence=rojo(),
        title=titulo,
        text=texto_valor,
        labels={columna_valor: metrica, "Locación": label_locacion}
    )

    st.plotly_chart(fig)


    with st.expander(f"Análisis detallado de {config_loc_in_out}"):
        generar_analisis(data, metrica)