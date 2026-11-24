# Filtros de imagem com OpenCV (sem Streamlit: fáceis de testar e reaproveitar)
import cv2
import numpy as np


# ---------- Efeitos de cor (trabalham com a imagem colorida) ----------

def borrao_imagem(imagem, taxa):
    """Borrão gaussiano. 'taxa' é a intensidade (sigma); o OpenCV calcula a janela."""
    return cv2.GaussianBlur(imagem, (0, 0), taxa)


def brilho_imagem(imagem, quantidade):
    """Soma (ou subtrai) a quantidade no canal V (brilho) do HSV."""
    hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV).astype(np.int16)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] + quantidade, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)


def melhorar_detalhes(imagem):
    """Realça bordas e texturas (precisa de imagem colorida)."""
    return cv2.detailEnhance(imagem, sigma_s=10, sigma_r=0.15)


# ---------- Efeitos de forma (funcionam em cor ou cinza) ----------

def para_cinza(imagem):
    """Converte para cinza só se a imagem ainda for colorida (3 canais)."""
    if imagem.ndim == 3:
        return cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    return imagem


def erosao_imagem(imagem, tamanho):
    """'Emagrece' as áreas claras."""
    kernel = np.ones((tamanho, tamanho), np.uint8)
    return cv2.erode(imagem, kernel, iterations=1)


def dilatacao_imagem(imagem, tamanho):
    """'Engorda' as áreas claras."""
    kernel = np.ones((tamanho, tamanho), np.uint8)
    return cv2.dilate(imagem, kernel, iterations=1)


def bordas_imagem(imagem, limite_inferior, limite_superior):
    """Detector de bordas Canny (trabalha em cinza)."""
    return cv2.Canny(para_cinza(imagem), limite_inferior, limite_superior)
