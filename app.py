import cv2
import numpy as np
import streamlit as st
from PIL import Image


# ---------- Efeitos de cor (trabalham com a imagem colorida) ----------

def borrao_imagem(imagem, taxa):
    # Borrão gaussiano: "taxa" é a intensidade (sigma).
    # Com o tamanho (0, 0), o OpenCV calcula sozinho o tamanho da janela.
    return cv2.GaussianBlur(imagem, (0, 0), taxa)


def brilho_imagem(imagem, quantidade):
    # Converte para HSV e soma (ou subtrai) a quantidade no canal V (brilho)
    hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV).astype(np.int16)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] + quantidade, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)


def melhorar_detalhes(imagem):
    # Realça bordas e texturas (precisa de imagem colorida)
    return cv2.detailEnhance(imagem, sigma_s=10, sigma_r=0.15)


# ---------- Efeitos de forma (funcionam em cor ou cinza) ----------

def para_cinza(imagem):
    # Só converte se a imagem ainda for colorida (3 canais)
    if imagem.ndim == 3:
        return cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    return imagem


def erosao_imagem(imagem, tamanho):
    # "Emagrece" as áreas claras
    kernel = np.ones((tamanho, tamanho), np.uint8)
    return cv2.erode(imagem, kernel, iterations=1)


def dilatacao_imagem(imagem, tamanho):
    # "Engorda" as áreas claras
    kernel = np.ones((tamanho, tamanho), np.uint8)
    return cv2.dilate(imagem, kernel, iterations=1)


def bordas_imagem(imagem, limite_inferior, limite_superior):
    # Detector de bordas Canny (funciona em cinza)
    return cv2.Canny(para_cinza(imagem), limite_inferior, limite_superior)


# ---------- Página ----------

def principal():
    st.title("Open Data App")
    st.subheader("Esse aplicativo permite integrar processamento de imagens com OpenCV")
    st.text("Streamlit com OpenCV para processamento de imagens em tempo real.")

    arquivo_imagem = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    # Controles na barra lateral
    st.sidebar.header("Ajustes")
    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5, value=0.2)
    qtd_brilho = st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0)
    filtro_aprimoramento = st.sidebar.checkbox("Melhorar Detalhes da Imagem")
    img_cinza = st.sidebar.checkbox("Converter para Escala de Cinza")
    img_erosao = st.sidebar.checkbox("Filtro Erosão")
    img_dilatacao = st.sidebar.checkbox("Filtro Dilatação")
    img_edge = st.sidebar.checkbox("Filtro Edge")

    # Ajustes extras: só aparecem quando o filtro está marcado
    if img_erosao:
        tam_erosao = st.sidebar.slider("Tamanho da erosão", 1, 15, 3)
    if img_dilatacao:
        tam_dilatacao = st.sidebar.slider("Tamanho da dilatação", 1, 15, 3)
    if img_edge:
        limites = st.sidebar.slider("Sensibilidade das bordas", 0, 255, (100, 200))

    if not arquivo_imagem:
        st.warning("Por favor, faça o upload de uma imagem para continuar.")
        return

    # Abre a imagem e garante 3 canais em RGB
    imagem_original = Image.open(arquivo_imagem).convert("RGB")
    imagem = np.array(imagem_original)

    # 1) Efeitos de cor primeiro
    imagem_processada = borrao_imagem(imagem, taxa_borrao)
    imagem_processada = brilho_imagem(imagem_processada, qtd_brilho)
    if filtro_aprimoramento:
        imagem_processada = melhorar_detalhes(imagem_processada)

    # 2) Depois os que podem tirar a cor
    if img_cinza:
        imagem_processada = para_cinza(imagem_processada)
    if img_erosao:
        imagem_processada = erosao_imagem(imagem_processada, tam_erosao)
    if img_dilatacao:
        imagem_processada = dilatacao_imagem(imagem_processada, tam_dilatacao)
    if img_edge:
        imagem_processada = bordas_imagem(imagem_processada, limites[0], limites[1])

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