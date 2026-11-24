from componentes import cabecalho, carregar_imagem, mostrar_comparacao
from controles import ler_ajustes
from processamento import aplicar_filtros


def principal():
    cabecalho()
    original, imagem = carregar_imagem()
    ajustes = ler_ajustes()

    if imagem is not None:
        processada = aplicar_filtros(imagem, ajustes)
        mostrar_comparacao(original, processada)

if __name__ == "__main__":
    principal()
