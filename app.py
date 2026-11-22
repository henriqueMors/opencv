import cv2
import numpy as np
import streamlit as st
from PIL import Image
from skimage.morphology import erosion, disk

def erosao_skimage(imagem, tamanho):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    return erosion(cinza, disk(tamanho))   # disk = janela em formato de círculo

def brilho_imagem(imagem, quantidade):
    # Converte para HSV (Matiz, Saturação, Valor/brilho)
    hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)

    # Soma a quantidade ao canal V (brilho); o cv2.add não deixa passar de 255
    hsv[:, :, 2] = cv2.add(hsv[:, :, 2], quantidade)

    # Volta para RGB
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def borrao_imagem(imagem, taxa):
    # O tamanho do borrão precisa ser ímpar e maior que zero (1, 3, 5...)
    taxa = max(1, int(taxa))
    if taxa % 2 == 0:
        taxa += 1
    return cv2.GaussianBlur(imagem, (taxa, taxa), 0)

def melhorar_detalhes(imagem):
    # Realça bordas e texturas
    return cv2.detailEnhance(imagem, sigma_s=10, sigma_r=0.15)

def escala_cinza(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

def principal():
    st.title("Open Data App")
    st.subheader("Esse aplicativo permite integrar processamento de imagens com OpenCV")
    st.text("Streamlit com OpenCV para processamento de imagens em tempo real.")

    arquivo_imagem = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    # Todos os controles na barra lateral
    st.sidebar.header("Ajustes")
    taxa_borrao = st.sidebar.slider("Borrão", min_value=1, max_value=51, value=1, step=2)
    quantidade_brilho = st.sidebar.slider("Quantidade de brilho", min_value=0, max_value=100, value=0)
    filtro_aprimorado = st.sidebar.checkbox("Aplicar filtro aprimorado")
    aplicar_cinza = st.sidebar.checkbox("Converter para escala de cinza")
    aplicar_erosao = st.sidebar.checkbox("Aplicar erosão")

    if not arquivo_imagem:
        st.warning("Por favor, faça o upload de uma imagem para continuar.")
        return

    # Abre a imagem e garante 3 canais em RGB (PNG transparente ou cinza também funciona)
    imagem_original = Image.open(arquivo_imagem).convert("RGB")
    imagem = np.array(imagem_original)

    # Aplica os efeitos em sequência
    imagem_processada = borrao_imagem(imagem, taxa_borrao)
    imagem_processada = brilho_imagem(imagem_processada, quantidade_brilho)
    if filtro_aprimorado:
        imagem_processada = melhorar_detalhes(imagem_processada)
    if aplicar_cinza:
        imagem_processada = escala_cinza(imagem_processada)
    if aplicar_erosao:
        tamanho_erosao = st.sidebar.slider("Tamanho da erosão", min_value=1, max_value=10, value=1)
        imagem_processada = erosao_skimage(imagem_processada, tamanho_erosao)

    # Mostra as duas lado a lado
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.text("Imagem original:")
        st.image(imagem_original)
    with coluna2:
        st.text("Imagem processada:")
        st.image(imagem_processada)

if __name__ == "__main__":
    principal()