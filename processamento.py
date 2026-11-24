# Aplica os filtros na ordem certa, de acordo com os ajustes escolhidos
from filtros import (
    borrao_imagem, brilho_imagem, melhorar_detalhes,
    para_cinza, erosao_imagem, dilatacao_imagem, bordas_imagem,
)


def aplicar_filtros(imagem, ajustes):
    """Recebe a imagem (array RGB) e o dicionário de ajustes; devolve a imagem processada."""
    # 1) Efeitos de cor primeiro
    resultado = borrao_imagem(imagem, ajustes["borrao"])
    resultado = brilho_imagem(resultado, ajustes["brilho"])
    if ajustes["detalhes"]:
        resultado = melhorar_detalhes(resultado)

    # 2) Depois os que podem tirar a cor
    if ajustes["cinza"]:
        resultado = para_cinza(resultado)
    if ajustes["erosao"]:
        resultado = erosao_imagem(resultado, ajustes["erosao"])
    if ajustes["dilatacao"]:
        resultado = dilatacao_imagem(resultado, ajustes["dilatacao"])
    if ajustes["bordas"]:
        resultado = bordas_imagem(resultado, *ajustes["bordas"])

    return resultado
