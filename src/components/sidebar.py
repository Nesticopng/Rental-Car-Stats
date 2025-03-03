import streamlit as st

def mostrar_sidebar():
    """Muestra una barra lateral personalizada."""
    isotipo = "assets/images/car.png"
    logotipo = "assets/images/logo.png"
    st.logo(logotipo, icon_image=isotipo)

    menu = ["Inicio", "Cargar Archivo", "PDF", "Documentación"]
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "Inicio"
        
    st.markdown("""
        <style>
            .stRadio > div {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            .stRadio > div > label {
                width: 100%;
                display: flex;
                padding: 12px;
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                color: #333;
                border-radius: 10px;
                background-color: #e0e0e0;
                cursor: pointer;
                transition: all 0.3s ease-in-out;
                border: none;
                margin-bottom: 10px;
            }
            .stRadio > div > label:hover {
                background-color: rgb(146, 146, 146);
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
            .stRadio > div > label[data-baseweb="radio"] > div:first-child {
                background-color: #FF4E4C !important;
                color: white !important;
                box-shadow: 0px 4px 12px rgba(255, 0, 0, 0.3) !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.session_state.selected_page = st.sidebar.radio(
        " ",
        options=menu,
        index=menu.index(st.session_state.selected_page),
        key="menu_radio"
    )
