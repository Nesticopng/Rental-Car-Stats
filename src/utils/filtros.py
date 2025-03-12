import streamlit as st
from src.utils.helpers import cargar_datos_sin_filtros

def configuraciones():
    with st.popover("Configuraciones de la Base de Datos", icon="⚙️", use_container_width=True):
        st.title("Configuraciónes")
        
        df = cargar_datos_sin_filtros()
        if "filters" not in st.session_state:
            st.session_state["filters"] = {}

        st.markdown("<br>", unsafe_allow_html=True)

        # 🏙️ Filtros de Locaciones
        st.subheader("Filtros de Locaciones")

        col1, col2 = st.columns(2)
        
        with col1:
            locin_ciudad = st.multiselect("Ciudad de Renta (LocIn)", df["LocInCity"].dropna().unique(), placeholder="Seleccione una o varias ciudades")
            locin_pais = st.multiselect("País de Renta (LocIn)", df["LocInCountry"].dropna().unique(), placeholder="Seleccione uno o varios países")

        with col2:
            locout_ciudad = st.multiselect("Ciudad de Retorno (LocOut)", df["LocOutCity"].dropna().unique(), placeholder="Seleccione una o varias ciudades")
            locout_pais = st.multiselect("País de Retorno (LocOut)", df["LocOutCountry"].dropna().unique(), placeholder="Seleccione uno o varios países")

        st.markdown("<br>", unsafe_allow_html=True)

        # 🚗 Filtros de Clasificación de Vehículos
        st.subheader("Filtros de Clasificación de Vehículos (Class)")
        class_filtro = st.multiselect("Clasificación (Class)", df["Class"].dropna().unique(), placeholder="Seleccione una o varios tipos de Vehículos")

        st.markdown("<br>", unsafe_allow_html=True)

        # 🏢 Filtro de Empresas
        st.subheader("Filtro de Empresas")
        empresa = st.multiselect("Empresas", df["Source"].dropna().unique(), placeholder="Seleccione una o varias empresas")

        col1, col2 = st.columns(2)

        with col1:
            codigo_tarifa = st.multiselect("Código de Tarifa", df["RateCode"].dropna().unique(), placeholder="Seleccione uno o varios códigos")
        
        with col2:
            status = st.multiselect("Estatus del Registro", df["Status_"].dropna().unique(), placeholder="Seleccione uno o varios estados")

        st.markdown("<br>", unsafe_allow_html=True)

        # 🔢 Filtros de Rango Numérico
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            rdays_min, rdays_max = st.slider("Rango de Días Rentados (Días)", int(df["RDays"].min()), int(df["RDays"].max()), (int(df["RDays"].min()), int(df["RDays"].max())))
        
        with col2:
            totalbill_min, totalbill_max = st.slider("Rango de Dinero Gastado por Vehículo ($USD)", float(df["TotalBill"].min()), float(df["TotalBill"].max()), (float(df["TotalBill"].min()), float(df["TotalBill"].max())))

        st.markdown("<br>", unsafe_allow_html=True)

        # 📅 Filtros de Fecha (Pickupd y Returnd)
        col1, col2 = st.columns(2)
        with col1:
            pickup_date = st.date_input("Fecha de Renta (Rango)", [])
            pickup_date_range = tuple(pickup_date) if len(pickup_date) == 2 else None

        with col2:
            return_date = st.date_input("Fecha de Retorno (Rango)", [])
            return_date_range = tuple(return_date) if len(return_date) == 2 else None

        if st.button("Aplicar Filtros"):
            st.session_state["filters"] = {
                "LocInCity": locin_ciudad,
                "LocOutCity": locout_ciudad,
                "LocInCountry": locin_pais,
                "LocOutCountry": locout_pais,
                "Class": class_filtro,
                "Source": empresa,
                "RateCode": codigo_tarifa,
                "Status_": status,
                "RDays": (rdays_min, rdays_max),
                "TotalBill": (totalbill_min, totalbill_max),
                "Pickupd": pickup_date_range,
                "Returnd": return_date_range,
            }
            st.rerun()