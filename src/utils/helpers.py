import pandas as pd
import os

def cargar_datos():
    # Cargar el archivo
    df = pd.read_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "raw", "BD.xlsx")))

    # Crear nuevas columnas basadas en 'Class'
    df["Category"] = df["Class"].astype(str).str[0]
    df["Type"] = df["Class"].astype(str).str[1]
    df["Transmission"] = df["Class"].astype(str).str[2]
    df["Fuel"] = df["Class"].astype(str).str[3]

    # Reordena las columnas para que las nuevas queden después de "Class"
    columnas = df.columns.tolist()
    columnas_a_mover = ["Category", "Type", "Transmission", "Fuel"]
    columnas_reordenadas = (
        columnas[:columnas.index("Class")+1] + 
        columnas_a_mover + 
        [col for col in columnas if col not in columnas_a_mover and col not in columnas[:columnas.index("Class")+1]]
    )

    # Aplica el nuevo orden
    df = df[columnas_reordenadas]

    return df