# Guia de Execucao da Pipeline de Pre-processamento

Este guia descreve como executar a pipeline de pre-processamento dos microdados PNS 2019 com o codigo da pasta src.

## Pre-requisitos

- Python 3.12+
- Ambiente virtual ativo (tcc_venv)
- Dependencias instaladas

```bash
pip install -r requirements.txt
```

## Fluxo da Pipeline

A funcao principal esta em src/pipeline.py:

- Etapa 1: selecao de variaveis
- Etapa 2: limpeza e validacao
- Etapa 3: engenharia de atributos
- Etapa 4: transformacoes estatisticas

## Execucao Completa

No terminal, na raiz do projeto:

```bash
python src/pipeline.py
```

Ou via import:

```python
from pipeline import run_preprocessing_pipeline

# Executa todas as etapas e salva intermediarios
(df_final) = run_preprocessing_pipeline(save_intermediate=True)
```

## Execucao por Etapa (Retomar)

A pipeline aceita retomar em etapa especifica com skip_to_stage:

- 1: selecao
- 2: limpeza
- 3: engenharia
- 4: transformacoes

Exemplo:

```python
from pipeline import run_preprocessing_pipeline

# Retoma da engenharia de atributos
(df_final) = run_preprocessing_pipeline(skip_to_stage=3, save_intermediate=True)
```

## Entradas e Saidas

- Entrada principal: data/raw/pns_2019.csv
- Saidas processadas: data/processed/

Arquivos gerados (dependendo de save_intermediate):

- pns_2019_selected.csv
- pns_2019_cleaned.csv
- pns_2019_engineered.csv
- pns_2019_final.csv

## Uso em Notebook

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd().parent / 'src'))
from pipeline import run_preprocessing_pipeline

df = run_preprocessing_pipeline(save_intermediate=False)
print(df.shape)
```

## Erros Comuns

- Arquivo nao encontrado: confirme se data/raw/pns_2019.csv existe.
- Modulo nao encontrado: execute na raiz do projeto ou ajuste o sys.path no notebook.
- Ambiente incorreto: valide se o tcc_venv esta ativo antes de rodar.
