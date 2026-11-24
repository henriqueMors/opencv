# Controles da barra lateral: devolve tudo o que o usuário escolheu num dicionário
import streamlit as st


def ler_ajustes():
    """Mostra os controles na barra lateral e devolve os ajustes escolhidos.

    Para erosão, dilatação e bordas, o valor é None quando o filtro está desligado.
    """
    st.sidebar.header("Ajustes")
    ajustes = {
        "borrao": st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5, value=0.2),
        "brilho": st.sidebar.slider("Brilho", min_value=-50, max_value=50, value=0),
        "detalhes": st.sidebar.checkbox("Melhorar Detalhes da Imagem"),
        "cinza": st.sidebar.checkbox("Converter para Escala de Cinza"),
        "erosao": None,
        "dilatacao": None,
        "bordas": None,
    }

    usar_erosao = st.sidebar.checkbox("Filtro Erosão")
    usar_dilatacao = st.sidebar.checkbox("Filtro Dilatação")
    usar_bordas = st.sidebar.checkbox("Filtro Edge")

    # Ajustes extras: só aparecem quando o filtro está marcado
    if usar_erosao:
        ajustes["erosao"] = st.sidebar.slider("Tamanho da erosão", 1, 15, 3)
    if usar_dilatacao:
        ajustes["dilatacao"] = st.sidebar.slider("Tamanho da dilatação", 1, 15, 3)
    if usar_bordas:
        ajustes["bordas"] = st.sidebar.slider("Sensibilidade das bordas", 0, 255, (100, 200))

    return ajustes
