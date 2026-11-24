# Partes visuais da página
import numpy as np
import streamlit as st
from PIL import Image


def cabecalho():
    st.title("Open Data App")
    st.subheader("Esse aplicativo permite integrar processamento de imagens com OpenCV")
    st.text("Streamlit com OpenCV para processamento de imagens em tempo real.")


def carregar_imagem():
    """Campo de upload. Devolve (imagem PIL, array RGB) ou (None, None)."""
    arquivo = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
    if not arquivo:
        st.warning("Por favor, faça o upload de uma imagem para continuar.")
        return None, None
    original = Image.open(arquivo).convert("RGB")  # garante 3 canais em RGB
    return original, np.array(original)


def mostrar_comparacao(original, processada):
    """Mostra a imagem original e a processada lado a lado."""
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.text("Imagem original:")
        st.image(original)
    with coluna2:
        st.text("Imagem processada:")
        st.image(processada)
