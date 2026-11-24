import numpy as np
import pytest

from filtros import brilho_imagem, para_cinza, borrao_imagem
from processamento import aplicar_filtros


@pytest.fixture
def imagem():
    rng = np.random.default_rng(0)
    return rng.integers(0, 256, (40, 60, 3), dtype=np.uint8)


def ajustes_base(**mudancas):
    ajustes = {"borrao": 0.2, "brilho": 0, "detalhes": False, "cinza": False,
               "erosao": None, "dilatacao": None, "bordas": None}
    ajustes.update(mudancas)
    return ajustes


def test_brilho_nao_passa_dos_limites(imagem):
    assert brilho_imagem(imagem, 50).max() <= 255
    assert brilho_imagem(imagem, -50).min() >= 0


def test_brilho_positivo_clareia(imagem):
    assert brilho_imagem(imagem, 50).mean() > imagem.mean()


def test_cinza_vira_um_canal_e_nao_converte_duas_vezes(imagem):
    cinza = para_cinza(imagem)
    assert cinza.ndim == 2
    assert para_cinza(cinza).ndim == 2


def test_borrao_mantem_tamanho(imagem):
    assert borrao_imagem(imagem, 3.5).shape == imagem.shape


@pytest.mark.parametrize("cinza", [False, True])
@pytest.mark.parametrize("erosao", [None, 3])
@pytest.mark.parametrize("dilatacao", [None, 3])
@pytest.mark.parametrize("bordas", [None, (100, 200)])
def test_todas_as_combinacoes_funcionam(imagem, cinza, erosao, dilatacao, bordas):
    ajustes = ajustes_base(borrao=3.5, brilho=-50, detalhes=True, cinza=cinza,
                           erosao=erosao, dilatacao=dilatacao, bordas=bordas)
    resultado = aplicar_filtros(imagem, ajustes)
    assert resultado.shape[:2] == imagem.shape[:2]
