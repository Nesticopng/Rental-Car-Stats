import streamlit as st
import plotly.express as px
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Cargar datos
df = cargar_datos()

# Análisis Automatizado
def generar_analisis(df_analisis, metrica):
    top_5 = df_analisis.nlargest(5, "Valor") if metrica == "Dinero Generado (USD)" else df_analisis.nlargest(5, "Cantidad de Rentas")

    analisis_texto = f"**Las 5 locaciones con mayor {metrica}:**\n\n"
    for _, row in top_5.iterrows():
        valor_formateado = f"{row['Cantidad de Rentas']:,.0f}" if metrica == "Cantidad de Rentas" else row["Dinero Generado ($USD)"]
        analisis_texto += f"- **{row['Locación']}**: {valor_formateado}\n"

    columnas_a_mostrar = ["Locación", "Cantidad de Rentas"] if metrica == "Cantidad de Rentas" else ["Locación", "Dinero Generado ($USD)"]

    return analisis_texto, top_5[columnas_a_mostrar]

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
        df_analisis = df[columna_analisis].value_counts().reset_index()
        df_analisis.columns = ["Locación", "Cantidad de Rentas"]
        df_analisis = df_analisis.sort_values(by="Cantidad de Rentas", ascending=False)
        columna_valor = "Cantidad de Rentas"
        texto_valor = "Cantidad de Rentas"
    else:
        df_analisis = df.groupby(columna_analisis)["TotalBill"].sum().reset_index()
        df_analisis.columns = ["Locación", "Valor"]
        df_analisis = df_analisis.sort_values(by="Valor", ascending=False)
        df_analisis["Dinero Generado ($USD)"] = df_analisis["Valor"].apply(lambda x: f"${x:,.2f}")
        columna_valor = "Valor"  
        texto_valor = "Dinero Generado ($USD)"

    # Título dinámico
    titulo = f"{metrica} según Locaciones de {config_loc_in_out}"

    # Configuración del Gráfico
    fig = px.bar(
        df_analisis, x="Locación", y=columna_valor, color="Locación",
        color_discrete_sequence=rojo(),
        title=titulo,
        text=texto_valor,
        labels={columna_valor: metrica, "Locación": label_locacion}
    )

    st.plotly_chart(fig)

    analisis_texto, top_5_tabla = generar_analisis(df_analisis, metrica)

    with st.expander(f"Análisis detallado de {config_loc_in_out}"):
        st.markdown(analisis_texto)
        st.write(top_5_tabla)
