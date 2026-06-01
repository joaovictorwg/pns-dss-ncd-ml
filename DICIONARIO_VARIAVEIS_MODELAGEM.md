# Dicionario de Variaveis da Modelagem (LASSO e Random Forest)

## Escopo
Este dicionario inclui somente as variaveis usadas na modelagem dos notebooks:
- notebooks/lasso_hipertensao.ipynb
- notebooks/random_forest.ipynb

Modelos considerados:
- BIO
- DSS
- DSS+BIO

Total de variaveis de entrada (features): 28
Variavel alvo (desfecho): 1

## 1) Variavel alvo

### hipertensao
- Tipo: float64 (binaria no uso de modelagem)
- Valores esperados: 0 ou 1
- Descricao: diagnostico medico de hipertensao arterial
- Papel: desfecho (y)

## 2) Features demograficas (base)

### idade_c
- Tipo: float64
- Descricao: idade centralizada
- Blocos: BIO, DSS, DSS+BIO

### sexo_feminino
- Tipo: int64/bool (binaria)
- Valores: 0 (masculino), 1 (feminino)
- Blocos: BIO, DSS, DSS+BIO

### raca_Preta
- Tipo: bool/int (binaria)
- Descricao: dummy de raca/cor
- Blocos: BIO, DSS, DSS+BIO

### raca_Parda
- Tipo: bool/int (binaria)
- Descricao: dummy de raca/cor
- Blocos: BIO, DSS, DSS+BIO

### raca_Amarela
- Tipo: bool/int (binaria)
- Descricao: dummy de raca/cor
- Blocos: BIO, DSS, DSS+BIO

### raca_Indigena
- Tipo: bool/int (binaria)
- Descricao: dummy de raca/cor
- Blocos: BIO, DSS, DSS+BIO

## 3) Features biomedicas e comportamentais

### atividade_ativo
- Tipo: bool/int (binaria)
- Descricao: pratica atividade fisica (sim/nao)
- Blocos: BIO, DSS+BIO

### tabagismo_ativo
- Tipo: bool/int (binaria)
- Descricao: fumante atual (sim/nao)
- Blocos: BIO, DSS+BIO

### alcool_ativo
- Tipo: bool/int (binaria)
- Descricao: consumo atual de alcool (sim/nao)
- Blocos: BIO, DSS+BIO

### imc
- Tipo: float64
- Descricao: indice de massa corporal
- Blocos: BIO, DSS+BIO

## 4) Features DSS (determinantes sociais)

### escolaridade_ord
- Tipo: float64 (ordinal)
- Faixa usual: 0 a 4
- Blocos: DSS, DSS+BIO

### renda_per_capita_log
- Tipo: float64
- Descricao: renda per capita transformada por log1p
- Blocos: DSS, DSS+BIO

### plano_saude
- Tipo: float64/binaria
- Valores usuais: 0 (nao), 1 (sim)
- Blocos: DSS, DSS+BIO

### situacao_domicilio
- Tipo: int64/binaria
- Valores usuais: 0 (rural), 1 (urbano)
- Blocos: DSS, DSS+BIO

## 5) Interacoes com idade

### sexo_x_idade
- Tipo: float64
- Formula: sexo_feminino * idade_c
- Blocos: BIO, DSS, DSS+BIO

### raca_Preta_x_idade
- Tipo: float64
- Formula: raca_Preta * idade_c
- Blocos: BIO, DSS, DSS+BIO

### raca_Parda_x_idade
- Tipo: float64
- Formula: raca_Parda * idade_c
- Blocos: BIO, DSS, DSS+BIO

### raca_Amarela_x_idade
- Tipo: float64
- Formula: raca_Amarela * idade_c
- Blocos: BIO, DSS, DSS+BIO

### raca_Indigena_x_idade
- Tipo: float64
- Formula: raca_Indigena * idade_c
- Blocos: BIO, DSS, DSS+BIO

### atividade_x_idade
- Tipo: float64
- Formula: atividade_ativo * idade_c
- Blocos: BIO, DSS+BIO

### tabagismo_x_idade
- Tipo: float64
- Formula: tabagismo_ativo * idade_c
- Blocos: BIO, DSS+BIO

### alcool_x_idade
- Tipo: float64
- Formula: alcool_ativo * idade_c
- Blocos: BIO, DSS+BIO

### imc_x_idade
- Tipo: float64
- Formula: imc * idade_c
- Blocos: BIO, DSS+BIO

### esc_x_idade
- Tipo: float64
- Formula: escolaridade_ord * idade_c
- Blocos: DSS, DSS+BIO

### renda_x_idade
- Tipo: float64
- Formula: renda_per_capita_log * idade_c
- Blocos: DSS, DSS+BIO

### plano_x_idade
- Tipo: float64
- Formula: plano_saude * idade_c
- Blocos: DSS, DSS+BIO

### situacao_x_idade
- Tipo: float64
- Formula: situacao_domicilio * idade_c
- Blocos: DSS, DSS+BIO

### indice_socioeconomico_x_idade
- Tipo: float64
- Formula: indice_socioeconomico * idade_c
- Blocos: DSS, DSS+BIO

## 6) Interacoes DSS com IMC

### renda_x_imc
- Tipo: float64
- Formula: renda_per_capita_log * imc
- Blocos: DSS+BIO

### esc_x_imc
- Tipo: float64
- Formula: escolaridade_ord * imc
- Blocos: DSS+BIO

## 7) Composicao por bloco

### Bloco BIO
idade_c, sexo_feminino, raca_Preta, raca_Parda, raca_Amarela, raca_Indigena, sexo_x_idade, raca_Preta_x_idade, raca_Parda_x_idade, raca_Amarela_x_idade, raca_Indigena_x_idade, atividade_ativo, tabagismo_ativo, alcool_ativo, imc, atividade_x_idade, tabagismo_x_idade, alcool_x_idade, imc_x_idade

### Bloco DSS
idade_c, sexo_feminino, raca_Preta, raca_Parda, raca_Amarela, raca_Indigena, sexo_x_idade, raca_Preta_x_idade, raca_Parda_x_idade, raca_Amarela_x_idade, raca_Indigena_x_idade, escolaridade_ord, renda_per_capita_log, plano_saude, situacao_domicilio, esc_x_idade, renda_x_idade, plano_x_idade, situacao_x_idade, indice_socioeconomico_x_idade

### Bloco DSS+BIO
Uniao de BIO + DSS + interacoes DSS-IMC: renda_x_imc e esc_x_imc
