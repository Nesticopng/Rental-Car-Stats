import streamlit as st
import pandas as pd
import os
from pyairports.airports import Airports


def cargar_datos_sin_filtros():

    # Cargar el archivo por defecto si no se ha subido uno, o utiliza el subido por el usuario
    if "uploaded_file_path" in st.session_state:
        file_path = st.session_state["uploaded_file_path"]
    else:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw", "BD.xlsx"))
    
    df = pd.read_excel(file_path)
    
    columnas = df.columns.tolist()

    # Cargar decodificador (IATA)
    airports = Airports()

    # Crear nuevas columnas basadas en 'Class'
    df["Category"] = df["Class"].astype(str).str[0]
    df["Type"] = df["Class"].astype(str).str[1]
    df["Transmission"] = df["Class"].astype(str).str[2]
    df["Fuel"] = df["Class"].astype(str).str[3]

    # Cambiar el formato de las columnas basadas en fecha para quitar las horas.
    df["Pickupd"] = pd.to_datetime(df["Pickupd"]).dt.date
    df["Returnd"] = pd.to_datetime(df["Returnd"]).dt.date
    df["Booked"] = pd.to_datetime(df["Booked"]).dt.date

    # Función para obtener ciudad y país a partir de un código IATA
    def obtener_ciudad_pais(codigo_iata):
        try:
            airport = airports.airport_iata(codigo_iata)
            if airport:
                return airport.city, airport.country
            else:
                return "Desconocido", "Desconocido"
        except:
            return "Desconocido", "Desconocido"

    # Crear nuevas columnas para LocOut
    df[['LocOutCity', 'LocOutCountry']] = df['LocOut'].apply(
        lambda x: pd.Series(obtener_ciudad_pais(x))
    )

    # Crear nuevas columnas para LocIn
    df[['LocInCity', 'LocInCountry']] = df['LocIn'].apply(
        lambda x: pd.Series(obtener_ciudad_pais(x))
    )

    # Reordena las columnas para que queden después de "Class"
    columnas_a_mover = ["Category", "Type", "Transmission", "Fuel"]
    columnas_reordenadas = (
        columnas[:columnas.index("Class")+1] + 
        columnas_a_mover + 
        [col for col in columnas if col not in columnas_a_mover and col not in columnas[:columnas.index("Class")+1]]
    )

    # Reordena las columnas para que queden después de "LocOut"
    columnas_a_mover = ["LocOutCity", "LocOutCountry"]
    columnas_reordenadas = (
        columnas_reordenadas[:columnas_reordenadas.index("LocOut")+1] + 
        columnas_a_mover + 
        [col for col in columnas_reordenadas if col not in columnas_a_mover and col not in columnas_reordenadas[:columnas_reordenadas.index("LocOut")+1]]
    )
    
    # Reordena las columnas para que queden después de "LocIn"
    columnas_a_mover = ["LocInCity", "LocInCountry"]
    columnas_reordenadas = (
        columnas_reordenadas[:columnas_reordenadas.index("LocIn")+1] + 
        columnas_a_mover + 
        [col for col in columnas_reordenadas if col not in columnas_a_mover and col not in columnas_reordenadas[:columnas_reordenadas.index("LocIn")+1]]
    )

    # Aplica el nuevo orden
    df = df[columnas_reordenadas]
                
    return df

def cargar_datos():
        # Aplicar Filtros si existen
    df = cargar_datos_sin_filtros()

    if "filters" in st.session_state:
        filters = st.session_state["filters"]

        for key, value in filters.items():
            if isinstance(value, list) and value:  # Filtrar listas con valores seleccionados
                df = df[df[key.replace("_", "")].isin(value)]
            elif isinstance(value, tuple) and len(value) == 2:  # Rango de valores (min, max)
                df = df[(df[key.replace("_", "")] >= value[0]) & (df[key.replace("_", "")] <= value[1])]

    return df