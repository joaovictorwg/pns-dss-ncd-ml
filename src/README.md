# Módulos de Pré-processamento - Estrutura KDD

Organização de código seguindo a metodologia **KDD** (Knowledge Discovery in Databases) com separação clara de responsabilidades.

---

## Estrutura de Arquivos

```
src/
├── config.py                  # Configurações centralizadas
├── selection.py              # Seleção de features (1. KDD)
├── preprocessing.py          # Limpeza e validação (2. KDD)
├── feature_engineering.py    # Criação de variáveis (3. KDD)
├── transformation.py         # Transformações estatísticas
├── modeling.py              # Pipelines e modelos (futuro)
├── evaluation.py            # Métricas e avaliação (futuro)
├── pipeline.py              # Orquestrador principal
├── __init__.py              # Pacote Python
└── README.md                # Este arquivo
```

---

## 1. SELECTION (Seleção de Features)

**Arquivo:** `selection.py`

### Responsabilidade
- Mapear códigos IBGE para nomes interpretáveis
- Selecionar subconjunto de features do dataset bruto

### Principais Funções

```python
select_features(df_raw=None, input_file=None, output_file=None)
```

Seleciona features a partir do CSV bruto e salva versão pré-selecionada.

**Exemplo:**
```python
from selection import select_features

df_selected = select_features()
# Output: ../data/processed/pns_2019_selected.csv
```

---

## 2. PREPROCESSING (Limpeza e Validação)

**Arquivo:** `preprocessing.py`

### Responsabilidade
- Conversão de códigos (1/2/9 → 0/1/NaN)
- Variáveis binárias
- Filtros de população-alvo
- Tratamento de valores inválidos
- Ajustes lógicos entre variáveis

### Principais Funções

```python
clean_pns_data(df)
```

Função orquestradora que aplica toda limpeza.

**Exemplo:**
```python
from preprocessing import clean_pns_data

df_clean = clean_pns_data(df_selected)
# Resultado: DataFrame limpo, sem transformações
```

### Variáveis Agregadas de Multimorbidade

O preprocessing cria automaticamente variáveis para análise de multimorbidade:

**`n_doencas`** (Int64):
- Contagem total de DCNTs por indivíduo
- Range: 0 a 16 doenças
- Útil para: análise de carga de doença, gradiente de complexidade

**`doenca_cronica`** (Int64 - binária):
- Indica presença de pelo menos 1 DCNT
- 0 = nenhuma doença crônica
- 1 = pelo menos uma doença
- Útil para: análise binária saudável vs doente

**Lista de DCNTs consideradas:**
`hipertensao`, `diabetes`, `doenca_coracao`, `infarto`, `angina`, `insuficiencia_cardiaca`, `arritmia`, `avc`, `asma`, `artrite`, `dort`, `depressao`, `doenca_pulmao`, `enfisema`, `bronquite`, `insuficiencia_renal`

---

## 3. FEATURE ENGINEERING (Engenharia de Features)

**Arquivo:** `feature_engineering.py`

### Responsabilidade
- One-hot encoding (UF, raça, tipo domicílio, tabagismo, álcool, atividade)
- Variáveis ordinais (escolaridade)
- Combinações inteligentes (tabagismo, álcool, atividade física)
- Cálculo de IMC


### Principais Funções

```python
apply_feature_engineering(df)
```

Função orquestradora que aplica toda engenharia.

**Exemplo:**
```python
from feature_engineering import apply_feature_engineering

df_feat = apply_feature_engineering(df_clean)
# Resultado: DataFrame com features engenheiradas
```

---

## 4. TRANSFORMATION (Transformações Estatísticas)

**Arquivo:** `transformation.py`

### Responsabilidade
- Transformação logarítmica de renda
- Centralização de variáveis contínuas
- Termos polinomiais
- Scaling (futuro: sklearn Pipeline)

### Principais Funções

```python
transform_renda(df)      # Log da renda
transform_idade(df)      # Centralização + polinômio
apply_transformations(df) # Orquestradora
```

**Exemplo:**
```python
from transformation import apply_transformations

df_trans = apply_transformations(df_feat)
# Resultado: DataFrame pronto para modelagem
```

---

## 5. PIPELINE (Orquestrador Principal)

**Arquivo:** `pipeline.py`

### Responsabilidade
- Coordenar fluxo completo
- Chamar funções na sequência correta
- Salvamento opcional de arquivos intermediários

### Principais Funções

```python
run_preprocessing_pipeline(
    input_file=None,
    save_intermediate=False,
    skip_to_stage=None
)
```

**Exemplo - Pipeline Completo:**
```python
from pipeline import run_preprocessing_pipeline

df_final = run_preprocessing_pipeline(save_intermediate=True)
```

**Exemplo - Retomar de etapa específica:**
```python
# Retomar da engenharia (pule seleção + limpeza)
df_final = run_preprocessing_pipeline(skip_to_stage=3)
```

---

## CONFIG (Configurações Centralizadas)

**Arquivo:** `config.py`

### Responsabilidade
- Caminhos de arquivos
- Constantes globais
- Mapas de recodificação
- Thresholds e parâmetros

**Exemplo:**
```python
from config import (
    RAW_DATA_FILE,
    UF_MAP,
    MIN_AGE,
    IMC_MIN, IMC_MAX
)
```

---

##  Como Usar

### Pipeline Automático 

```python
from pipeline import run_preprocessing_pipeline

# Executa tudo de uma vez
df_final = run_preprocessing_pipeline(save_intermediate=True)
```

### Etapa por Etapa (Exploração)

```python
from selection import select_features
from preprocessing import clean_pns_data
from feature_engineering import apply_feature_engineering
from transformation import apply_transformations

df_sel = select_features()
df_clean = clean_pns_data(df_sel)
df_feat = apply_feature_engineering(df_clean)
df_trans = apply_transformations(df_feat)
```

### No Notebook

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent / 'src'))

from pipeline import run_preprocessing_pipeline

df = run_preprocessing_pipeline(save_intermediate=False)
```

---

## Fluxo de Dados

```
┌─────────────────────────────────────────────────────────┐
│                   RAW DATA (CSV)                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 1️⃣  SELECTION: select_features()                        │
│    Mapeia códigos IBGE → nomes interpretáveis          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 2️⃣  PREPROCESSING: clean_pns_data()                     │
│    Limpeza, validação, filtros, recodificação          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 3️⃣  FEATURE ENGINEERING: apply_feature_engineering()   │
│    One-hot, ordinais, combinações, IMC                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 4️⃣  TRANSFORMATION: apply_transformations()            │
│    Log, centralização, polinômios                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│        CLEAN DATA (pronto para modelagem)              │
└─────────────────────────────────────────────────────────┘
```

---

## Checklist de Características

- Limpeza separada da engenharia
- Engenharia separada da transformação
- Sem winsorização
- Sem salvamento dentro das funções (apenas em `pipeline.py`)
- Evita data leakage (transformações em exploração)
- Código modular e reutilizável
- Documentação clara
- Estrutura KDD seguida
- Configurações centralizadas

---
