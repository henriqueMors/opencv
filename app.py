import cv2
import streamlit as st
from PIL import Image

def principal():
    st.title("Open Data App")
    st.subheader("Esse aplicativo permite integrar processamento de imagens com OpenCV")
    st.text("Streamlit com OpenCV para processamento de imagens em tempo real.")

    #img = cv2.imread("images/docdoom.jpg")
    #img = cv2.imread("images/gtavi.jpg")
    #img = cv2.imread("images/vicecity.jpg")

    arquivo_imagem = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
    
    taxa_borrao = st.sidebar.slider("Taxa de borrão", min_value=1, max_value=20, value=5)
    quantidade_brilho = st.sidebar.slider("Quantidade de brilho", min_value=0, max_value=100, value=50)
    filtro_aprimorado = st.sidebar.checkbox("Aplicar filtro aprimorado")
    

    if not arquivo_imagem:
        st.warning("Por favor, faça o upload de uma imagem para continuar.")
        return None

    imagem_original = Image.open(arquivo_imagem)

    st.text("Imagem original:")

    st.image(imagem_original)

if __name__ == "__main__":
    principal()