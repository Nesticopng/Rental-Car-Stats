import streamlit as st
import plotly.express as px
import numpy as np
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Análisis Automatizado
def generar_analisis(data, metrica):
    st.write("### Análisis Estadístico")

    analisis = []

    # Calcular valores clave
    total_registros = len(data)
    media = data.iloc[:, 1].mean()
    mediana = data.iloc[:, 1].median()
    desviacion = data.iloc[:, 1].std()
    max_valor = data.iloc[:, 1].max()
    min_valor = data.iloc[:, 1].min()
    top_locacion = data.iloc[0, 0]
    top_valor = data.iloc[0, 1]
    min_indice = data.iloc[:, -1].idxmin()
    min_categoria = data.iloc[min_indice, 0]

    if metrica == "Cantidad de Rentas":
        analisis.append(f"📊 **Total de Ubicaciones analizadas:** {total_registros:,}")
        analisis.append(f"📈 **Promedio de {metrica}:** {media:,.2f}")
        analisis.append(f"📊 **Mediana de {metrica}:** {mediana:,.0f}")
        analisis.append(f"📉 **Desviación estándar de {metrica}:** {desviacion:,.2f}")
        analisis.append(f"🏆 **Locación con mayor {metrica}:** {top_locacion} con {top_valor:,.0f}")
        analisis.append(f"🔽 **La Ubicación que menos {metrica} generó fue {min_categoria} :** {min_valor:,.0f}")
    
    if metrica == "Dinero Generado (USD)":
        analisis.append(f"📊 **Total de Ubicaciones analizadas:** {total_registros:,}")
        analisis.append(f"📈 **Promedio de {metrica}:** 💲{media:,.2f}")
        analisis.append(f"📊 **Mediana de {metrica}:** 💲{mediana:,.2f}")
        analisis.append(f"📉 **Desviación estándar de {metrica}:** 💲{desviacion:,.2f}")
        analisis.append(f"🏆 **Locación con mayor {metrica}:** {top_locacion} con 💲{top_valor:,.2f}")
        analisis.append(f"🔽 **Menor {metrica}:** 💲{min_valor:,.2f}")    

    # Análisis de dispersión
    if desviacion > media * 0.5:
        analisis.append(f"⚠️ **Alta variabilidad:** Existe una gran diferencia entre las locaciones en términos de {metrica}.")
    
    else:
        analisis.append(f"✅ **Distribución estable:** No hay grandes diferencias extremas en {metrica}.")

    # Análisis de concentración
    percentil_90 = np.percentile(data.iloc[:, 1], 90)
    percentil_10 = np.percentile(data.iloc[:, 1], 10)

    # Análisis de concentración
    if max_valor > percentil_90 * 1.5:
        analisis.append(f"🚀 **El valor máximo ({max_valor:,.2f}) es significativamente superior al percentil 90.** Esto sugiere que una o pocas locaciones dominan la métrica.")
    
    elif max_valor < percentil_90:
        analisis.append("📊 **El valor máximo no es muy superior al percentil 90.** Esto indica una distribución más uniforme.")

    if top_valor > percentil_90 * 1.5:
        analisis.append(f"🚀 **{top_locacion} está significativamente por encima del 90% de las locaciones.** Podría ser un punto estratégico clave.")
    
    if min_valor < percentil_10:
        analisis.append(f"🔻 **Existen locaciones con valores por debajo del percentil 10.** Es recomendable analizar si se requieren optimizaciones de estrategias para mejorar estas tendencias.")

    # Recomendaciones según tendencias
    if media > 1000 and metrica == "Dinero Generado (USD)":
        analisis.append("💰 **Los ingresos promedio son altos.** Se puede considerar estrategias para mantener esta tendencia positiva.")
    
    elif media < 500 and metrica == "Dinero Generado (USD)":
        analisis.append("📉 **Ingresos promedio bajos.** Evaluar promociones o mejorar la distribución de vehículos.")
    
    if top_valor > media * 2:
        analisis.append(f"🏆 **{top_locacion} es un líder {metrica}.** Se podría analizar su situación y estrategias para replicar en otras locaciones.")

    # Mostrar el análisis
    for linea in analisis:
        st.write(linea)

    columnas_a_mostrar = ["Locación", "Cantidad de Rentas"] if metrica == "Cantidad de Rentas" else ["Locación", "Dinero Generado ($USD)"]

    st.write("### Tabla de Datos")
    st.write(data[columnas_a_mostrar])

def grafica_loc():

    # Cargar datos
    df = cargar_datos()

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
            ("Sitio de Renta", "Sitio de Retorno"),
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
        columna_analisis = "LocIn" if config_loc_in_out == "Sitio de Renta" else "LocOut"
        label_locacion = "Ubicación (IATA)"
    else:
        if grafica_loc == "Ciudad":
            columna_analisis = "LocInCity" if config_loc_in_out == "Sitio de Renta" else "LocOutCity"
            label_locacion = "Ciudad"
        else:
            columna_analisis = "LocInCountry" if config_loc_in_out == "Sitio de Renta" else "LocOutCountry"
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


    with st.expander(f"Análisis Detallado"):
        generar_analisis(data, metrica)