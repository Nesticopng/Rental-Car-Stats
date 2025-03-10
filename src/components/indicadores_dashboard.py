import streamlit as st
from src.utils.helpers import cargar_datos

#Data frame
df = cargar_datos()
df_trans_show = df[df['Status_'] == 'SHOW']

#Sección Recaudaciones
suma_total_show = df_trans_show['TotalBill'].sum()
suma_total_show_formateado = f"{suma_total_show:,.2f}"

#Sección Pick Up
conteo_pick_up = df_trans_show['LocOut'].value_counts()
pick_up_mayor_frecuencia = conteo_pick_up.index[0]
frecuencia_mayor_pick_up = conteo_pick_up.iloc[0]

#Sección Empresa
conteo_source = df_trans_show['Source'].value_counts()
empresa_mayor_frecuencia = conteo_source.index[0]
frecuencia_mayor_empresa = conteo_source.iloc[0]

#Total Registros en el Dataframe
total_registros = df.shape[0]

def indicadores_dashboard():
    with st.container():
        col1, col2, col3, col4 = st.columns(4, border=True)
        
        with col1:
            st.subheader("Dinero Recaudado", divider="gray")
            st.title(f"**{suma_total_show_formateado}**$")
            st.write(f"El total de dinero recaudado es **{suma_total_show_formateado} $** en un periodo de un año.")
        
        with col2:
            st.subheader("Destino más Recurrido", divider="gray")
            st.title(f"**{pick_up_mayor_frecuencia}**")
            st.write(f"El destino más recurrido es **{pick_up_mayor_frecuencia}** en donde se han concretado **{frecuencia_mayor_pick_up} rentas**.")

        with col3:
            st.subheader("Registros Totales", divider="gray")
            st.title(f"**{total_registros}**")
            st.write(f"Hay un total de **{total_registros}** en un periodo de un año")

        with col4:
            st.subheader("Empresa con más Rentas", divider="gray")
            st.title(f"**{empresa_mayor_frecuencia}**")
            st.write(f"La empresa que más rentas ha concretado es: **{empresa_mayor_frecuencia}** con **{frecuencia_mayor_empresa} rentas**.")