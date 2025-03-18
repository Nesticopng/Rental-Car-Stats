import streamlit as st
import pandas as pd
import calplot
import numpy as np
from src.utils.helpers import cargar_datos

def mostrar_analisis(fecha_columna, titulo):
    with st.expander(f"Análisis Detallado", expanded=False):
        st.header(f"📊 Análisis de {titulo}")

        if fecha_columna.isna().all():
            st.warning("⚠️ No hay datos disponibles para esta categoría de fecha.")
            return

        # Calcular el periodo de tiempo
        min_fecha = fecha_columna.min()
        max_fecha = fecha_columna.max()
        periodo_estudio = f"Periodo de estudio: {min_fecha.strftime('%d/%m/%Y')} hasta {max_fecha.strftime('%d/%m/%Y')}"
        st.write(periodo_estudio)

        # Analizar por año
        frecuencia_anual = fecha_columna.dt.year.value_counts().reset_index()
        frecuencia_anual.columns = ["Año", "Cantidad de Vehículos Rentados"]

        if len(frecuencia_anual) > 1:
            st.write("Años con más transacciones:")
            st.write(frecuencia_anual.sort_values(by="Cantidad de Vehículos Rentados", ascending=False).head())
            
        else:
            st.write(f"Solo se tiene datos para el año **{min_fecha.year}**.")


        # Analizar por mes
        st.write("Meses con más transacciones por año:")
        meses_espanol = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        
        for year in frecuencia_anual["Año"]:
            mes_por_año = fecha_columna[fecha_columna.dt.year == year].dt.month.value_counts().reset_index()
            mes_por_año.columns = ["Mes", "Cantidad de Vehículos Rentados"]
            mes_por_año["Mes"] = mes_por_año["Mes"].apply(lambda x: meses_espanol[x - 1])
            
            if len(mes_por_año) > 1:
                st.write(f"Año **{year}**:")
                st.write(mes_por_año.sort_values(by="Cantidad de Vehículos Rentados", ascending=False).head())

            else:
                st.write(f"Solo se tiene datos para el año **{year}**.")


        # Analizar por día (por cada mes de cada año)
        st.write("Días con más transacciones por mes y año:")
        for year in frecuencia_anual["Año"]:
            for month in range(1, 13):
                dia_por_mes = fecha_columna[(fecha_columna.dt.year == year) & (fecha_columna.dt.month == month)].dt.day.value_counts().reset_index()
                dia_por_mes.columns = ["Día", "Cantidad de Vehículos Rentados"]
                
                if not dia_por_mes.empty:
                    st.write(f"Año **{year}**, Mes **{meses_espanol[month-1]}**:")
                    st.write(dia_por_mes.sort_values(by="Cantidad de Vehículos Rentados", ascending=False).head())

# Configuraciones del Calendario
def mostrar_calendario(fecha_columna, titulo):
    st.header(f"{titulo}")

    if fecha_columna.isna().all():
        st.warning("⚠️ No hay datos disponibles para esta categoría de fecha.")
        return

    transacciones_por_fecha = fecha_columna.value_counts().sort_index()

    fig, axes = calplot.calplot(transacciones_por_fecha, cmap="Reds", dropzero=True, linewidth=1)

    ax = axes[0] if isinstance(axes, (list, np.ndarray)) else axes

    # Cambiar los nombres de los meses a español
    meses_espanol = {
        "Jan": "Ene", "Feb": "Feb", "Mar": "Mar", "Apr": "Abr",
        "May": "May", "Jun": "Jun", "Jul": "Jul", "Aug": "Ago",
        "Sep": "Sep", "Oct": "Oct", "Nov": "Nov", "Dec": "Dic"
    }

    ax.set_xticklabels([meses_espanol.get(label.get_text(), label.get_text()) for label in ax.get_xticklabels()])
    
    # Cambiar los nombres de los dias de la semana
    dias_espanol = {
        "Mon": "Lun", "Tue": "Mar", "Wed": "Mié", "Thu": "Jue",
        "Fri": "Vie", "Sat": "Sáb", "Sun": "Dom"
    }

    ax.set_yticklabels([dias_espanol.get(label.get_text(), label.get_text()) for label in ax.get_yticklabels()])

    st.pyplot(fig)

# Generar Gráfica
def grafica_tiempo():

    # Cargar Datos
    df = cargar_datos()

    # Convertir las fechas a formato datetime
    df["PickUpDate"] = pd.to_datetime(df["Pickupd"].astype(str).str[:10], errors="coerce")
    df["ReturnDate"] = pd.to_datetime(df["Returnd"].astype(str).str[:10], errors="coerce")
    df["BookedDate"] = pd.to_datetime(df["Booked"].astype(str).str[:10], errors="coerce")

    st.header("📆 Calendario de Transacciones")

    tipo_fecha = st.selectbox(
        "Selecciona el tipo de transacción a visualizar:",
        ["Fecha de Renta del Vehículo", "Fecha de Vuelta del Vehículo", "Fecha de Reserva"]
    )

    if tipo_fecha == "Fecha de Renta del Vehículo":
        mostrar_calendario(df["PickUpDate"], "Calendario de Rentas")
        mostrar_analisis(df["PickUpDate"], "Rentas de Vehículos")

    elif tipo_fecha == "Fecha de Vuelta del Vehículo":
        mostrar_calendario(df["ReturnDate"], "Calendario de Devoluciones")
        mostrar_analisis(df["ReturnDate"], "Devoluciones de Vehículos")

    elif tipo_fecha == "Fecha de Reserva":
        mostrar_calendario(df["BookedDate"], "Calendario de Reservas")
        mostrar_analisis(df["BookedDate"], "Reservas de Vehículos")