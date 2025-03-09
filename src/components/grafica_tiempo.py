import streamlit as st
import pandas as pd
import calplot
import numpy as np
from src.utils.helpers import cargar_datos

# Cargar Datos
df = cargar_datos()

# Convertir las fechas a formato datetime
df["PickUpDate"] = pd.to_datetime(df["Pickupd"].astype(str).str[:10], errors="coerce")
df["ReturnDate"] = pd.to_datetime(df["Returnd"].astype(str).str[:10], errors="coerce")
df["BookedDate"] = pd.to_datetime(df["Booked"].astype(str).str[:10], errors="coerce")


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
        frecuencia_anual = fecha_columna.dt.year.value_counts().sort_index()
        if len(frecuencia_anual) > 1:
            st.write("Años con más transacciones:")
            # Mostrar los años con más transacciones (ordenados por la cantidad de transacciones)
            st.write(frecuencia_anual.sort_values(ascending=False).head())
        else:
            st.write(f"Solo se tiene datos para el año **{min_fecha.year}**.")

        # Analizar por mes (por cada año)
        st.write("Meses con más transacciones por año:")
        meses_espanol = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        
        for year in frecuencia_anual.index:
            mes_por_anio = fecha_columna[fecha_columna.dt.year == year].dt.month.value_counts().sort_index()
            if len(mes_por_anio) > 1:
                st.write(f"Año **{year}**:")
                # Mostrar los meses con más transacciones (ordenados por la cantidad de transacciones)
                st.write(mes_por_anio.sort_values(ascending=False).head())
            else:
                st.write(f"Solo se tiene datos para el año **{year}**.")

        # Analizar por día (por cada mes de cada año)
        st.write("Días con más transacciones por mes y año:")
        for year in frecuencia_anual.index:
            for month in range(1, 13):
                dia_por_mes = fecha_columna[(fecha_columna.dt.year == year) & (fecha_columna.dt.month == month)].dt.day.value_counts().sort_index()
                if not dia_por_mes.empty:
                    st.write(f"Año **{year}**, Mes **{meses_espanol[month-1]}**:")
                    # Mostrar los días con más transacciones (ordenados por la cantidad de transacciones)
                    st.write(dia_por_mes.sort_values(ascending=False).head())

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

    # Llamar a la función de análisis
    mostrar_analisis(fecha_columna, titulo)

# Generar Gráfica
def grafica_tiempo():
    st.header("📆 Calendario de Transacciones")

    # Selección de tipo de fecha
    tipo_fecha = st.selectbox(
        "Selecciona el tipo de transacción a visualizar:",
        ["Fecha de Renta del Vehículo", "Fecha de Vuelta del Vehículo", "Fecha de Reserva"]
    )

    # Mapeo del tipo seleccionado a los datos reales
    if tipo_fecha == "Fecha de Renta del Vehículo":
        mostrar_calendario(df["PickUpDate"], "Calendario de Rentas")
    elif tipo_fecha == "Fecha de Vuelta del Vehículo":
        mostrar_calendario(df["ReturnDate"], "Calendario de Devoluciones")
    elif tipo_fecha == "Fecha de Reserva":
        mostrar_calendario(df["BookedDate"], "Calendario de Reservas")