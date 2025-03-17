import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def ChatGPT():
    client = OpenAI(
        api_key=api_key
    )

    st.write("### Chat IA")

    # Inicializar session_state para almacenar mensajes
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes previos
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada de usuario
    if prompt := st.chat_input("Escribe tu consulta aquí..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta de OpenAI
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.messages,
                    stream=True
                )

                for chunk in response:
                    if chunk.choices:
                        full_response += chunk.choices[0].delta.content or ""
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

                # Guardar la respuesta en session_state
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            except Exception as e:
                error_message = str(e)

                if "quota" in error_message or "insufficient_quota" in error_message:
                    st.error("⚠️ No tienes suficientes créditos en OpenAI. Verifica tu cuenta.")
                else:
                    st.error(f"❌ Ocurrió un error inesperado: {error_message}")

                return