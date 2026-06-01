# PNS DSS NCD ML

Projeto de pesquisa para analise de Determinantes Sociais da Saude (DSS) e Doencas Cronicas Nao Transmissiveis (DCNT) com microdados da Pesquisa Nacional de Saude (PNS 2019).

## Objetivo

Construir uma base analitica consistente a partir dos microdados da PNS 2019 e avaliar associacoes entre fatores sociodemograficos, socioeconomicos, territoriais e comportamentais e desfechos cronicos.

## Estrutura do repositorio

- `data/`: dados brutos e processados.
- `notebooks/`: exploracao e experimentos de modelagem.
- `src/`: codigo do pipeline de pre-processamento e modulos de apoio.
- `ibge-official-files/`: arquivos oficiais de referencia do IBGE/PNS.

## Ambiente

- Python 3.12.10
- JupyterLab
- Bibliotecas principais no arquivo `requirements.txt`

## Documentacao enxuta

- Dicionario de variaveis: `DICIONARIO_VARIAVEIS.md`
- Guia de execucao da pipeline: `GUIA_PIPELINE_PRE_PROCESSAMENTO.md`

## Execucao rapida

1. Ative o ambiente virtual (`tcc_venv`).
2. Instale dependencias: `pip install -r requirements.txt`.
3. Siga o guia em `GUIA_PIPELINE_PRE_PROCESSAMENTO.md`.
