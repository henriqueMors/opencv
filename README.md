# Open Data App: Processamento de Imagens com OpenCV

Aplicação web feita em **Python** com **Streamlit** e **OpenCV** para aplicar filtros e ajustes em imagens e ver o resultado na hora, com a imagem original e a processada lado a lado.

## Funcionalidades

- **Upload de imagem** nos formatos JPG, JPEG e PNG. Imagens com transparência ou em tons de cinza também funcionam.
- **Comparação lado a lado**: imagem original × imagem processada
- Ajustes na barra lateral:

| Ajuste | O que faz |
|---|---|
| **Borrão** (0.2 a 3.5) | suaviza a imagem (borrão gaussiano) |
| **Brilho** (-50 a 50) | escurece (valores negativos) ou clareia (positivos) |
| **Melhorar Detalhes da Imagem** | realça bordas e texturas |
| **Converter para Escala de Cinza** | remove as cores |
| **Filtro Erosão** | "emagrece" as áreas claras; ajuda a remover ruído |
| **Filtro Dilatação** | "engorda" as áreas claras; ajuda a preencher falhas |
| **Filtro Edge** | mostra apenas os contornos (detector Canny) |

- **Ajustes extras** que aparecem só quando o filtro está ativo: tamanho da erosão, tamanho da dilatação e sensibilidade das bordas
- **Qualquer combinação de filtros funciona**: os efeitos são aplicados numa ordem segura (primeiro os de cor, depois os que podem remover a cor)

## Estrutura do projeto

```
opencv_app/
├── app.py            # monta a página e organiza os passos
├── componentes.py    # título, upload da imagem e comparação lado a lado
├── controles.py      # barra lateral: sliders e checkboxes
├── processamento.py  # aplica os filtros na ordem certa
├── filtros.py        # funções de filtro com OpenCV
└── test_filtros.py   # testes automatizados com pytest
```

A lógica de processamento (`filtros.py` e `processamento.py`) **não depende do Streamlit**. Ela pode ser testada isoladamente e reaproveitada em outras aplicações, como uma API ou um app desktop.

| Para... | altere |
|---|---|
| criar um novo filtro | `filtros.py` (função), `controles.py` (controle) e `processamento.py` (aplicação) |
| mudar textos ou layout da página | `componentes.py` |
| mudar faixas e valores iniciais dos ajustes | `controles.py` |

## Como executar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# instalar as dependências
pip install streamlit opencv-python numpy pillow pytest

# rodar o app
streamlit run app.py
```

O app abre no navegador em `http://localhost:8501`.

## Testes

```bash
pytest
```

Os testes conferem que:

- o brilho nunca ultrapassa os limites de 0 a 255;
- o brilho positivo clareia a imagem;
- a conversão para cinza não é aplicada duas vezes;
- o borrão mantém o tamanho da imagem;
- **todas as combinações** de cinza, erosão, dilatação e bordas funcionam juntas, mesmo com borrão e brilho nos valores extremos.

## Conceitos utilizados

- **RGB × BGR**: o OpenCV trabalha por padrão em BGR. Este projeto mantém a imagem em **RGB** do início ao fim, o mesmo padrão do Pillow e do Streamlit, para evitar cores trocadas.
- **HSV**: o brilho é ajustado no canal V (*Value*) do espaço de cores HSV, sem alterar o tom das cores.
- **Morfologia** (erosão e dilatação): operações que mudam a forma das áreas claras da imagem, muito usadas para limpar ruído antes de OCR ou de contagem de objetos.
- **Canny**: algoritmo clássico de detecção de bordas, com um limite inferior e um superior de sensibilidade.

## Tecnologias

- Python 3
- Streamlit
- OpenCV
- NumPy
- Pillow
- pytest