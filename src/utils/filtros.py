import streamlit as st
from src.utils.helpers import cargar_datos_sin_filtros, cargar_datos

def configuraciones():
    with st.popover("Configuraciones de la Base de Datos", icon="⚙️", use_container_width=True):
    
        st.title("Configuraciónes")
        
        df = cargar_datos_sin_filtros()

        if "filters" not in st.session_state:
            st.session_state["filters"] = {}
        temp_filters = st.session_state["filters"].copy()
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 🏙️ Filtros de Locaciones
        st.subheader("Filtros de Locaciones")
        col1, col2 = st.columns(2)
        
        with col1:
            temp_filters["LocInCity"] = st.multiselect("Ciudad de Renta (LocIn)", df["LocInCity"].dropna().unique(), default=st.session_state["filters"].get("LocInCity", []), placeholder="Seleccione ciudades")
            temp_filters["LocInCountry"] = st.multiselect("País de Renta (LocIn)", df["LocInCountry"].dropna().unique(), default=st.session_state["filters"].get("LocInCountry", []), placeholder="Seleccione países")
        
        with col2:
            temp_filters["LocOutCity"] = st.multiselect("Ciudad de Retorno (LocOut)", df["LocOutCity"].dropna().unique(), default=st.session_state["filters"].get("LocOutCity", []), placeholder="Seleccione ciudades")
            temp_filters["LocOutCountry"] = st.multiselect("País de Retorno (LocOut)", df["LocOutCountry"].dropna().unique(), default=st.session_state["filters"].get("LocOutCountry", []), placeholder="Seleccione países")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 🚗 Filtros de Clasificación de Vehículos
        st.subheader("Filtros de Clasificación de Vehículos")
        temp_filters["Class"] = st.multiselect("Clasificación", df["Class"].dropna().unique(), default=st.session_state["filters"].get("Class", []), placeholder="Seleccione clasificaciones")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 🏢 Filtro de Empresas
        st.subheader("Filtro de Empresas")
        temp_filters["Source"] = st.multiselect("Empresas", df["Source"].dropna().unique(), default=st.session_state["filters"].get("Source", []), placeholder="Seleccione empresas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            temp_filters["RateCode"] = st.multiselect("Código de Tarifa", df["RateCode"].dropna().unique(), default=st.session_state["filters"].get("RateCode", []), placeholder="Seleccione códigos")
    
        with col2:
            temp_filters["Status_"] = st.multiselect("Estatus del Registro", df["Status_"].dropna().unique(), default=st.session_state["filters"].get("Status_", []), placeholder="Seleccione estatus")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 🔢 Filtros de Rango Numérico
        col1, col2 = st.columns(2)
        
        with col1:
            temp_filters["RDays"] = st.slider("Días Rentados", int(df["RDays"].min()), int(df["RDays"].max()), value=st.session_state["filters"].get("RDays", (int(df["RDays"].min()), int(df["RDays"].max()))))        
        
        with col2:
            temp_filters["TotalBill"] = st.slider("Dinero Gastado ($USD)", float(df["TotalBill"].min()), float(df["TotalBill"].max()), value=st.session_state["filters"].get("TotalBill", (float(df["TotalBill"].min()), float(df["TotalBill"].max()))))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botones de Acción
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Guardar Cambios", use_container_width=True, type="primary"):
                st.session_state["filters"] = temp_filters.copy()
                st.rerun()
        
        with col2:
            if st.button("Limpiar Filtros", use_container_width=True):
                st.session_state["filters"] = {}
                st.rerun()