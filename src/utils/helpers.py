import pandas as pd
import os

def cargar_datos():
    """Carga los datos desde el archivo Excel."""
    return pd.read_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw", "BD.xlsx")))