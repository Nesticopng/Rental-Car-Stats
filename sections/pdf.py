import streamlit as st
from src.utils.generar_pdf import generar_pdf


def PDF():
    st.title("📄 PDF")

    if st.button("Generar PDF", type="primary"):
        pdf_path = generar_pdf()
        st.success("✅ PDF generado con éxito.")

    # Leer el archivo generado para que el usuario lo descargue
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        # Botón de descarga
        st.download_button(
            label="📥 Descargar PDF",
            data=pdf_bytes,
            file_name="Trabajo_final.pdf",
            mime="application/pdf"
        )
