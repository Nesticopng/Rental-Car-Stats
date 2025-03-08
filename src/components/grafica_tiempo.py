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
    st.header("📆 Calendario de Transacciones")

    # Selección de tipo de fecha
    tipo_fecha = st.selectbox(
        "Selecciona el tipo de transacción a visualizar:",
        ["Fecha de Renta del Vehículo", "Fecha de Vuelta del Vehículo", "Fecha de Reserva"]
    )

    # Mapeo del tipo seleccionado a los datos reales
    if tipo_fecha == "Fecha de Renta del Vehículo":
        mostrar_calendario(df["PickUpDate"], "Calendario de Pick-Up")
    elif tipo_fecha == "Fecha de Vuelta del Vehículo":
        mostrar_calendario(df["ReturnDate"], "Calendario de Devoluciones")
    elif tipo_fecha == "Fecha de Reserva":
        mostrar_calendario(df["BookedDate"], "Calendario de Reservas")