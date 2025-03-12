import streamlit as st
def documentacion():
    st.title("📚 Documentación")
    st.write("Rental Car Stats es una aplicación estadística diseñada para Web ACO®, en la cual el usuario podra ingresar su **base de datos** y esta aplicación le dará 2 outputs, un Dashboard donde podras visualizar la **Base de Datos** y un PDF donde se podrá ver de forma más amplia y estructurada la información de esta aplicación.")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Aplicación", divider="grey")
    st.write("La aplicación consta de 4 secciones **Inicio, Cargar Archivo, PDF y Documentación**,")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Inicio")
    st.write("Esta sección de la aplicación es donde se podrá ver el análisis de la **Base de Datos** con sus gráficas")
    st.write("El Dashboard del Inicio se divide en 8 secciones donde el usuario podra interactuar con las gráficas por medio de **filtros** donde seleccionará las métricas que quiera analizar con respecto a una variable de la **Base de Datos**. Las siguientes variables que estamos analizando son 'Vehículos Según su Clasificación (Class)', 'Empresas (Source)', 'Calendario de Transacciones (Pickupd, Returnd, Booked)', 'Estados de las Reservaciones (Status_)', 'Pre-Depósitos (res_prepagos)' ")
    st.write("A su ves todas estas variables se podrán análizar con distintas métricas como 'Cantidades de Vehículos Rentados', 'Promedios de Dinero Gastado (\$USD)', 'Días Rentados', 'Dinero Generado por Tarifas (\$USD)', entre otros segùn la Variable.")

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("### Cargar Archivo")
    st.write("Esta sección le permitirá al usuario poder subir su propia **Base de Datos** (Excel), de esta forma la aplicación le proporcionara los análisis, gráficos y funciones que reflejen su propia Base de Datos **(Si el usuario no ingresa una Base de Datos la aplicación ya vendrá cargada con una por Defecto)**.")

    st.write("A continuación vamos a mostrar una breve descripción de las columnas, las variables que deben ir en ellas y sus formatos.")

    with st.container(border=True):
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Confirm", "LocOut / LocIn", "Class", "RateCode", "Pickupd / Returnd / Booked", "Source", "RDays", "TotalRate / AvgRateDay / TotalExtras / TotalBill", "res_prepagos", "Status_"])

        with tab1:
            st.subheader("Confirm")
            st.text("Funciona como un ID que registra de forma resumida los datos de la transaccion")
            st.write("Es un String")

        with tab2:
            st.subheader("LocOut / LocIn")
            st.text("Son las Ubicaciones (IATA) donde Rentan/Devuelven los vehículos.")
            st.write("Es un String")

        with tab3:
            st.subheader("Class")
            st.text("Clasificación de Vehículos (ACRISS). Contiene 4 Carácteres")
            st.write("Es un String")
            
        with tab4:
            st.subheader("RateCode")
            st.text("Código de tarifa asociado.")
            st.write("Es un String")

        with tab5:
            st.subheader("Pickupd / Returnd / Booked")
            st.text("Son las Variables que indican día de la Renta, Retorno del Vehículo Rentado y Reservación del Vehículo")
            st.write("Es un Date (YYYY/MM/DD)")

        with tab6:
            st.subheader("Source")
            st.text("Empresas")
            st.write("Es un String")
        
        with tab7:
            st.subheader("RDays")
            st.text("Tiempo (Días) del vehículo rentado.")
            st.write("Es un Int")

        with tab8:
            st.subheader("TotalRate / AvgRateDay / TotalExtras / TotalBill")
            st.text("Tárifas, Básicas, Promedio por días, Extras, Total")
            st.write("Es un Float")
        
        with tab9:
            st.subheader("res_prepagos")
            st.text("Pre-Depósitos")
            st.write("Es un Float")

        with tab10:
            st.subheader("Status_")
            st.text("Estatus de las Transacciones")
            st.write("Es un String")
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("### PDF")
    st.write("En esta sección, el usuario podrá **generar dinámicamente un PDF personalizado** que resume de manera clara y estructurada los análisis realizados sobre la **Base de Datos**. Este PDF incluirá:")
    st.write("- **Gráficos y visualizaciones** clave de la Base de Datos.")
    st.write("- **Métricas y estadísticas** relevantes, como promedios, totales y tendencias.")
    st.write("- **Filtros aplicados** por el usuario durante la interacción con el Dashboard.")
    st.write("- **Conclusiones** basadas en los datos analizados.")

    st.write("El PDF está diseñado para ser un **reporte profesional** que puede ser compartido con equipos, clientes o stakeholders, permitiendo una comunicación efectiva de los insights obtenidos.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("### Documentación")
    st.write("En esta sección, se encuentra una **guía detallada** sobre el uso, la lógica y las funcionalidades de la aplicación **Rental Car Stats**. Está diseñada para que nuevos usuarios puedan familiarizarse rápidamente con la herramienta y aprovechar al máximo sus capacidades.")
    st.write("¿Qué incluye la Documentación?")
    st.write("1. **Explicación de cada sección**:")
    st.write("- **Inicio**: Cómo interactuar con el Dashboard, aplicar filtros y analizar las métricas.")
    st.write("- **Cargar Archivo**: Instrucciones para subir una Base de Datos personalizada y entender los formatos requeridos.")
    st.write("- **Documentación**: Esta guía detallada.")

    st.write("2. **Lógica de la aplicación**:")
    st.write("- Cómo se procesan y analizan los datos.")
    st.write("- Detalles sobre las métricas calculadas y su interpretación.")

    st.write("3. **Funcionalidades avanzadas**:")
    st.write("- Uso de filtros interactivos.")
    st.write("- Personalización de gráficos y reportes.")

    st.write("Esta documentación está diseñada para ser un **recurso de referencia** constante, tanto para usuarios nuevos como para aquellos que deseen profundizar en el uso de la aplicación.")