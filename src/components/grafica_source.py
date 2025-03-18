import streamlit as st
import plotly.express as px
import numpy as np
from src.utils.helpers import cargar_datos
from src.utils.paleta_rojo import rojo

# Mapeo de nombres de variables
variable_mapping = {
    "Cantidad de Rentas": "Cantidad",
    "Dinero Recaudado por Tarifa Básica": "TotalRate",
    "Dinero Recaudado por Extras Gastados": "TotalExtras",
    "Dinero Recaudado por Tarifa Total": "TotalBill",
    "Promedio de Días Rentados": "RDays"
}

# Análisis Automatizado
def mostrar_datos_y_analisis(data, es_dinero, es_promedio, metrica):
    st.write("### Análisis Estadístico")
    analisis = []

    # Calcular estadísticas clave
    total_registros = len(data)
    media = data.iloc[:, 1].mean()
    mediana = data.iloc[:, 1].median()
    desviacion = data.iloc[:, 1].std()
    max_valor = data.iloc[:, 1].max()
    min_valor = data.iloc[:, 1].min()
    top_empresa = data.iloc[0, 0]
    top_valor = data.iloc[0, 1]

    # Calcular percentiles
    percentil_90 = np.percentile(data.iloc[:, 1], 90)
    percentil_10 = np.percentile(data.iloc[:, 1], 10)

    # Análisis General
    analisis.append(f"📊 **Total de Empresas Analizadas:** {total_registros:,}")
    analisis.append(f"📈 **Promedio de {metrica}:** {media:,.2f}")
    analisis.append(f"📊 **Mediana de {metrica}:** {mediana:,.2f}")
    analisis.append(f"📉 **Desviación estándar:** {desviacion:,.2f}")
    analisis.append(f"🔝 **Empresa con mayor {metrica}:** {top_empresa} con {top_valor:,.2f}")
    analisis.append(f"🔽 **Menor {metrica} en el registro:** {min_valor:,.2f}")
    analisis.append(f"🏆 **Mayor {metrica} en el registro:** {max_valor:,.2f}")

    # Análisis de dispersión
    if desviacion > media * 0.5:
        analisis.append(f"⚠️ **Alta variabilidad:** Existen grandes diferencias entre empresas en esta métrica de {metrica}.")
    else:
        analisis.append("✅ **Distribución estable:** No hay grandes diferencias extremas en la métrica analizada.")

    # Análisis de concentración
    if max_valor > percentil_90 * 1.5:
        analisis.append(f"🚀 **El valor máximo ({max_valor:,.2f}) es significativamente superior al percentil 90.** Esto sugiere que una o pocas empresas dominan la métrica.")
    elif max_valor < percentil_90:
        analisis.append("📊 **El valor máximo no es muy superior al percentil 90.** Esto indica una distribución más uniforme.")

    if min_valor < percentil_10:
        analisis.append(f"🔻 **Existen empresas con valores por debajo del percentil 10.** Es recomendable evaluar si requieren optimización.")

    # Recomendaciones estratégicas
    if media > 1000 and es_dinero:
        analisis.append("💰 **Los ingresos promedio son altos.** Se puede considerar estrategias para mantener esta tendencia positiva.")
    elif media < 500 and es_dinero:
        analisis.append("📉 **Ingresos promedio bajos.** Evaluar promociones o mejoras en estrategias de captación.")

    if top_valor > media * 2:
        analisis.append(f"🏆 **{top_empresa} es líder en {metrica}.** Se podría analizar su situación y estrategias para replicar en otras empresas.")

    # Mostrar el análisis línea por línea
    for linea in analisis:
        st.write(linea)

    if es_dinero:
        columnas_a_mostrar = ["Empresa", "Dinero Recaudado ($USD)"]

    elif es_promedio:
        columnas_a_mostrar = ["Empresa", "Promedio de Días Rentados"]

    else:
        columnas_a_mostrar = ["Empresa", "Cantidad de Vehículos Rentados"]

    st.write("### Tabla de Datos")
    st.write(data[columnas_a_mostrar])

# Generar Gráfico
def grafica_source():
    
    # Cargar Datos
    df = cargar_datos()
    
    # Contar la frecuencia de cada fuente de reserva
    frecuencia_source = df["Source"].value_counts().reset_index()
    frecuencia_source.columns = ["Empresa", "Cantidad de Vehículos Rentados"]

    st.header("Análisis de Rentas y Recaudación por Empresa")
    
    metrica = st.selectbox(
        "Métrica a analizar",
        ("Cantidad de Rentas", "Dinero Recaudado por Tarifa Básica", "Dinero Recaudado por Extras Gastados", "Dinero Recaudado por Tarifa Total", "Promedio de Días Rentados")
    )

    if metrica == "Cantidad de Rentas":
        data = frecuencia_source
        es_dinero = False
        es_promedio = False

    elif metrica == "Promedio de Días Rentados":
        columna_real = variable_mapping[metrica]
        data = df.groupby("Source")[columna_real].mean().reset_index()
        data.columns = ["Empresa", "Cantidad de Vehículos Rentados"]
        data["Cantidad de Vehículos Rentados"] = data["Cantidad de Vehículos Rentados"].round(2)
        data["Promedio de Días Rentados"] = data["Cantidad de Vehículos Rentados"].apply(lambda x: f"{x:.2f} días")
        es_dinero = False
        es_promedio = True

    else:
        columna_real = variable_mapping[metrica]
        data = df.groupby("Source")[columna_real].sum().reset_index()
        data.columns = ["Empresa", "Cantidad de Vehículos Rentados"]
        data["Cantidad de Vehículos Rentados"] = data["Cantidad de Vehículos Rentados"].round(2)
        data["Dinero Recaudado ($USD)"] = data["Cantidad de Vehículos Rentados"].apply(lambda x: f"${x:,.2f}")
        es_dinero = True
        es_promedio = False
        
    titulo = (
        f"Promedio de Días Rentados según la Empresa" if es_promedio else
        f"{metrica} según la Empresa" if es_dinero else
        "Rentas generadas según la Empresa"
    )

    fig = px.bar(
        data, 
        x="Empresa", 
        y="Cantidad de Vehículos Rentados", 
        color="Empresa", 
        color_discrete_sequence=rojo(),
        title=titulo,
        text="Promedio de Días Rentados" if es_promedio else "Dinero Recaudado ($USD)" if es_dinero else "Cantidad de Vehículos Rentados",
        labels={
            "Cantidad de Vehículos Rentados": "Días Promedio" if es_promedio else "Monto ($USD)" if es_dinero else "Cantidad de Vehículos Rentados", 
            "Empresa": "Empresa"
        }
    )
        
    st.plotly_chart(fig)
    
    with st.expander("Análisis Detallado"):
        mostrar_datos_y_analisis(data, es_dinero, es_promedio, metrica)