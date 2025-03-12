import streamlit as st
import pandas as pd
import os

def guardar_archivo(uploadedfile):
    if not os.path.exists("temp"):
        os.makedirs("temp")
    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success(f"El Archivo se ha cargado :{uploadedfile.name} correctamente")

def cargar_archivo():
    st.title("📤 Cargar Archivo")
    archivo_excel = st.file_uploader("Subir Excel", type=["xlsm", "xlsx", "xlsb", "xltx", "xltm", "xls", "xlt"])
    if archivo_excel is not None:
        detalles_archivo = { 
            "nombre": archivo_excel.name,
            "tipo": archivo_excel.type,
            "tamaño": archivo_excel.size
        }
        st.write(detalles_archivo)
        df = pd.read_excel(archivo_excel)
        st.dataframe(df)
        guardar_archivo(archivo_excel)