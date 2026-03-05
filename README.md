# PNS DSS NCD ML

Projeto de pesquisa aplicado para analisar Determinantes Sociais da Saude (DSS) e Doencas Cronicas Nao Transmissiveis (DCNT) com base nos microdados da Pesquisa Nacional de Saude (PNS 2019), utilizando pipeline de preprocessamento e modelagem em Python.

## Objetivo

Construir uma base analitica consistente a partir dos microdados da PNS 2019 e avaliar relacoes entre fatores sociodemograficos, socioeconomicos, territoriais e comportamentais com desfechos de doencas cronicas.

## Escopo do projeto

- Leitura e organizacao dos microdados oficiais da PNS.
- Selecao e tratamento de variaveis com base teorica.
- Preprocessamento, feature engineering e transformacoes estatisticas.
- Analise exploratoria e preparacao para modelagem preditiva.

## Estrutura principal

- `data/`: dados brutos e processados.
- `notebooks/`: analise exploratoria e experimentos.
- `src/`: modulos de processamento, transformacao, modelagem e avaliacao.
- `ibge-official-files/`: arquivos oficiais de suporte (layout, scripts e malha territorial).
- `docs.md`: documentacao metodologica, decisoes tecnicas e justificativas teoricas.

## Ambiente de desenvolvimento

- Python com ambiente virtual `tcc_venv`.
- Jupyter Notebook para analise exploratoria.
- Bibliotecas principais: `pandas`, `numpy`, `matplotlib`, `seaborn`, `geopandas`, `scikit-learn`.

## Como executar

1. Ative o ambiente virtual.
2. Execute o notebook `notebooks/analise_exploratoria.ipynb`.
3. Ou rode o pipeline pelos modulos em `src/`.

## Documentacao

As escolhas metodologicas, criterios de selecao de variaveis e justificativas epidemiologicas estao centralizadas em `docs.md`.
