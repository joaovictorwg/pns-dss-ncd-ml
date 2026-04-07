# Dicionário de Variáveis - Dataset PNS 2019 (Processado)

**Total de variáveis:** 79  
**Total de observações:** 74.304  
**Fonte:** Pesquisa Nacional de Saúde (PNS) 2019 - IBGE  
**População-alvo:** Adultos (≥18 anos) com dados completos

---

## 📋 Índice por Categoria

1. [Variáveis Sociodemográficas](#1-variáveis-sociodemográficas)
2. [Variáveis Geográficas](#2-variáveis-geográficas)
3. [Variáveis de Infraestrutura Domiciliar](#3-variáveis-de-infraestrutura-domiciliar)
4. [Variáveis Socioeconômicas](#4-variáveis-socioeconômicas)
5. [Variáveis de Saúde](#5-variáveis-de-saúde)
6. [Variáveis Comportamentais](#6-variáveis-comportamentais)
7. [Variáveis Biomédicas](#7-variáveis-biomédicas)
8. [Variáveis Derivadas e Transformadas](#8-variáveis-derivadas-e-transformadas)

---

## 1. Variáveis Sociodemográficas

### `sexo_feminino`
- **Tipo:** `int64`
- **Valores:** 0, 1
- **Descrição:** Sexo do respondente
  - `0` = Masculino
  - `1` = Feminino
- **Origem:** Variável C006 (PNS)

### `idade_c`
- **Tipo:** `float64`
- **Descrição:** Idade centralizada em torno da média amostral
- **Cálculo:** idade - média(idade)
- **Uso:** Variável contínua para modelagem; reduz multicolinearidade com termos polinomiais
- **Origem:** Variável C008 (PNS)

### `idade_c2`
- **Tipo:** `float64`
- **Descrição:** Termo quadrático da idade centralizada
- **Cálculo:** (idade_c)²
- **Uso:** Captura relações não-lineares entre idade e desfechos de saúde
- **Origem:** Derivada de C008

### `faixa_etaria`
- **Tipo:** `str` (categórica)
- **Valores:** '18-29', '30-39', '40-49', '50-59', '60+'
- **Descrição:** Categorização etária em grupos quinquenais/decenais
- **Cálculo:** pd.cut(idade, bins=[18, 30, 40, 50, 60, 120])
- **Origem:** Derivada de C008

### `raca_Preta`
### `raca_Amarela`
### `raca_Parda`
### `raca_Indigena`
### `raca_Ignorado`
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** One-hot encoding de raça/cor autodeclarada
  - Categoria de referência (baseline): **Branca** (drop_first=True)
- **Categorias originais:**
  - 1 = Branca (referência)
  - 2 = Preta
  - 3 = Amarela
  - 4 = Parda
  - 5 = Indígena
  - 9 = Ignorado
- **Origem:** Variável C009 (PNS)

---

## 2. Variáveis Geográficas

### `uf_AL`, `uf_AM`, `uf_AP`, ..., `uf_TO` (26 variáveis)
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** One-hot encoding da Unidade Federativa (UF) de residência
  - Categoria de referência (baseline): **AC - Acre** (drop_first=True)
  - Total de 27 UFs: 26 variáveis dummy + 1 baseline
- **Estados incluídos:**
  - Norte: RO, AC*, AM, RR, PA, AP, TO
  - Nordeste: MA, PI, CE, RN, PB, PE, AL, SE, BA
  - Centro-Oeste: MT, MS, GO, DF
  - Sudeste: MG, ES, RJ, SP
  - Sul: PR, SC, RS
- **Origem:** Variável V0001 (PNS)

### `regiao_norte`
### `regiao_nordeste`
### `regiao_centro_oeste`
### `regiao_sudeste`
### `regiao_sul`
- **Tipo:** `int64`
- **Valores:** 0, 1
- **Descrição:** Variáveis binárias indicando região geográfica do Brasil
- **Cálculo:** Agregação das UFs por região
  - **Norte:** AC, AP, AM, PA, RO, RR, TO
  - **Nordeste:** AL, BA, CE, MA, PB, PE, PI, RN, SE
  - **Centro-Oeste:** DF, GO, MT, MS
  - **Sudeste:** ES, MG, RJ, SP
  - **Sul:** PR, RS, SC
- **Origem:** Derivada das variáveis uf_*

---

## 3. Variáveis de Infraestrutura Domiciliar

### `situacao_domicilio`
- **Tipo:** `int64`
- **Valores:** 0, 1
- **Descrição:** Situação censitária do domicílio
  - `0` = Rural
  - `1` = Urbano
- **Origem:** Variável V0026 (PNS)

### `domicilio_Apartamento`
### `domicilio_Cortico`
### `domicilio_Ignorado`
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** One-hot encoding do tipo de domicílio
  - Categoria de referência (baseline): **Casa** (drop_first=True)
- **Categorias originais:**
  - 1 = Casa (referência)
  - 2 = Apartamento
  - 3 = Cortiço
  - 9 = Ignorado
- **Origem:** Variável A001 (PNS)

### `infra_agua`
- **Tipo:** `int64`
- **Valores:** 0, 1, 2
- **Descrição:** Nível de acesso à água canalizada (ordinal)
  - `0` = Não canalizada (pior condição)
  - `1` = Canalizada no terreno (intermediário)
  - `2` = Canalizada no cômodo (melhor condição)
- **Origem:** Variável A00601 (PNS)

### `acesso_internet`
- **Tipo:** `int64`
- **Valores:** 0, 1
- **Descrição:** Acesso à internet no domicílio
  - `0` = Não
  - `1` = Sim
- **Origem:** Variável A01901 (PNS)

---

## 4. Variáveis Socioeconômicas

### `plano_saude`
- **Tipo:** `float64`
- **Valores:** 0.0, 1.0, NaN
- **Descrição:** Posse de plano de saúde privado
  - `0.0` = Não possui
  - `1.0` = Possui
  - `NaN` = Ignorado
- **Origem:** Variável I00102 (PNS)

### `escolaridade_ord`
- **Tipo:** `float64`
- **Valores:** 0.0, 1.0, 2.0, 3.0, 4.0
- **Descrição:** Nível de escolaridade (ordinal)
  - `0` = Analfabeto
  - `1` = Ensino Fundamental
  - `2` = Ensino Médio
  - `3` = Ensino Superior
  - `4` = Pós-graduação
- **Cálculo:** Combinação das variáveis D001 (alfabetizado) e D00901 (escolaridade)
- **Origem:** Variáveis D001 e D00901 (PNS)

### `renda_domiciliar_log`
- **Tipo:** `float64`
- **Descrição:** Renda domiciliar total transformada por log(1+x)
- **Cálculo:** np.log1p(renda_domiciliar)
- **Justificativa:** Reduz assimetria e estabiliza variância
- **Origem:** Variável VDF002 (PNS)

### `renda_per_capita_log`
- **Tipo:** `float64`
- **Descrição:** Renda domiciliar per capita transformada por log(1+x)
- **Cálculo:** np.log1p(renda_per_capita)
- **Justificativa:** Reduz assimetria e estabiliza variância
- **Origem:** Variável VDF003 (PNS)

### `esc_scaled`
- **Tipo:** `float64`
- **Descrição:** Escolaridade padronizada (StandardScaler)
- **Cálculo:** (escolaridade_ord - μ) / σ
- **Uso:** Componente do índice socioeconômico
- **Origem:** Derivada de escolaridade_ord

### `renda_scaled`
- **Tipo:** `float64`
- **Descrição:** Renda per capita (log) padronizada (StandardScaler)
- **Cálculo:** (renda_per_capita_log - μ) / σ
- **Uso:** Componente do índice socioeconômico
- **Origem:** Derivada de renda_per_capita_log

### `indice_socioeconomico`
- **Tipo:** `float64`
- **Descrição:** Índice socioeconômico composto
- **Cálculo:** Média de esc_scaled e renda_scaled
- **Interpretação:** Quanto maior, melhor a posição socioeconômica
- **Origem:** Derivada de esc_scaled e renda_scaled

---

## 5. Variáveis de Saúde

### 5.1 Doenças Crônicas Não Transmissíveis (DCNTs)

Todas as DCNTs seguem o mesmo padrão:
- **Tipo:** `float64`
- **Valores:** 0.0, 1.0, NaN
  - `0.0` = Não possui a doença
  - `1.0` = Possui a doença
  - `NaN` = Resposta ignorada/não sabe

#### `hipertensao`
- **Descrição:** Diagnóstico médico de hipertensão arterial
- **Origem:** Variável Q00201 (PNS)

#### `diabetes`
- **Descrição:** Diagnóstico médico de diabetes mellitus
- **Origem:** Variável Q03001 (PNS)

#### `doenca_coracao`
- **Descrição:** Diagnóstico médico de doença do coração (qualquer tipo)
- **Origem:** Variável Q06306 (PNS)
- **Nota:** Se doenca_coracao = 0, os subtipos abaixo são automaticamente 0

#### `infarto`
- **Descrição:** Diagnóstico médico de infarto agudo do miocárdio
- **Origem:** Subtipo de doenca_coracao

#### `angina`
- **Descrição:** Diagnóstico médico de angina pectoris
- **Origem:** Subtipo de doenca_coracao

#### `insuficiencia_cardiaca`
- **Descrição:** Diagnóstico médico de insuficiência cardíaca
- **Origem:** Subtipo de doenca_coracao

#### `arritmia`
- **Descrição:** Diagnóstico médico de arritmia cardíaca
- **Origem:** Subtipo de doenca_coracao

#### `avc`
- **Descrição:** Diagnóstico médico de acidente vascular cerebral (AVC/derrame)
- **Origem:** Variável Q068 (PNS)

#### `asma`
- **Descrição:** Diagnóstico médico de asma ou bronquite asmática
- **Origem:** Variável Q074 (PNS)

#### `artrite`
- **Descrição:** Diagnóstico médico de artrite ou reumatismo
- **Origem:** Variável Q079 (PNS)

#### `dort`
- **Descrição:** Diagnóstico médico de DORT (Distúrbio Osteomuscular Relacionado ao Trabalho)
- **Origem:** Variável Q088 (PNS)

#### `depressao`
- **Descrição:** Diagnóstico médico de depressão
- **Origem:** Variável Q092 (PNS)

#### `doenca_pulmao`
- **Descrição:** Diagnóstico médico de doença pulmonar (exceto asma)
- **Nota:** Se doenca_pulmao = 0, enfisema e bronquite são automaticamente 0

#### `enfisema`
- **Descrição:** Diagnóstico médico de enfisema pulmonar
- **Origem:** Variável Q11605 (PNS), subtipo de doenca_pulmao

#### `bronquite`
- **Descrição:** Diagnóstico médico de bronquite crônica
- **Origem:** Variável Q11606 (PNS), subtipo de doenca_pulmao

#### `insuficiencia_renal`
- **Descrição:** Diagnóstico médico de insuficiência renal crônica
- **Origem:** Variável Q124 (PNS)

### 5.2 Variáveis Agregadas de Multimorbidade

#### `n_doencas`
- **Tipo:** `int64`
- **Valores:** 0 a 16
- **Descrição:** Contagem total de DCNTs diagnosticadas por indivíduo
- **Cálculo:** Soma de todas as 16 DCNTs (NaN tratado como 0)
- **DCNTs incluídas:** hipertensao, diabetes, doenca_coracao, infarto, angina, insuficiencia_cardiaca, arritmia, avc, asma, artrite, dort, depressao, doenca_pulmao, enfisema, bronquite, insuficiencia_renal
- **Origem:** Derivada das DCNTs

#### `doenca_cronica`
- **Tipo:** `int64`
- **Valores:** 0, 1
- **Descrição:** Presença de pelo menos uma DCNT
  - `0` = Nenhuma DCNT
  - `1` = Pelo menos 1 DCNT
- **Cálculo:** doenca_cronica = (n_doencas > 0)
- **Uso:** Variável desfecho para análise binária de multimorbidade
- **Origem:** Derivada de n_doencas

---

## 6. Variáveis Comportamentais

### 6.1 Tabagismo

#### `tabagismo_status`
- **Tipo:** `int64`
- **Valores:** 0, 1, 2
- **Descrição:** Status de tabagismo (ordinal)
  - `0` = Nunca fumou
  - `1` = Ex-fumante
  - `2` = Fumante atual
- **Origem:** Combinação de P050 (fumante atual) e P052 (fumou no passado)

#### `tabagismo_ativo`
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** Indicador se fuma atualmente
  - `True` = Fumante atual
  - `False` = Não fumante (nunca fumou ou ex-fumante)
- **Origem:** Derivada de tabagismo_status

### 6.2 Consumo de Álcool

#### `alcool_status`
- **Tipo:** `int64`
- **Valores:** 0, 1, 2, 3
- **Descrição:** Intensidade de consumo de álcool (ordinal)
  - `0` = Nunca bebe
  - `1` = Consumo raro (ocasional, <1 dia/semana)
  - `2` = Consumo moderado (1-2 dias/semana)
  - `3` = Consumo frequente (≥3 dias/semana)
- **Origem:** Combinação de P02801 (frequência de álcool) e dias da semana

#### `alcool_ativo`
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** Indicador se consome álcool atualmente
  - `True` = Consome (qualquer frequência)
  - `False` = Nunca bebeu
- **Origem:** Derivada de alcool_status

### 6.3 Atividade Física

#### `atividade_status`
- **Tipo:** `int64`
- **Valores:** 0, 1, 2, 3
- **Descrição:** Frequência de atividade física (ordinal)
  - `0` = Sedentário (não pratica)
  - `1` = Baixa frequência (1-2 dias/semana)
  - `2` = Moderada (3-4 dias/semana)
  - `3` = Alta (≥5 dias/semana)
- **Origem:** Variável P035 (PNS)

#### `atividade_ativo`
- **Tipo:** `bool`
- **Valores:** True, False
- **Descrição:** Indicador se pratica atividade física regularmente
  - `True` = Pratica atividade física
  - `False` = Sedentário
- **Origem:** Derivada de atividade_status

---

## 7. Variáveis Biomédicas

### `imc`
- **Tipo:** `float64`
- **Descrição:** Índice de Massa Corporal (IMC)
- **Cálculo:** peso (kg) / altura² (m)
- **Faixa válida:** 10.0 a 70.0 (valores fora são considerados NaN)
- **Origem:** Derivada de P00104 (peso) e W00203 (altura)
- **Classificação OMS:**
  - < 18.5: Baixo peso
  - 18.5-24.9: Peso normal
  - 25.0-29.9: Sobrepeso
  - ≥ 30.0: Obesidade

### `idade_imc`
- **Tipo:** `float64`
- **Descrição:** Termo de interação entre idade centralizada e IMC
- **Cálculo:** idade_c × imc
- **Justificativa:** Captura o efeito conjunto de idade e IMC sobre a saúde
- **Origem:** Derivada de idade_c e imc

---

## 8. Variáveis Derivadas e Transformadas

| Variável | Tipo | Descrição Resumida |
|----------|------|-------------------|
| `idade_c` | float64 | Idade centralizada (idade - média) |
| `idade_c2` | float64 | Idade centralizada ao quadrado |
| `faixa_etaria` | str | Categorização etária (18-29, 30-39, etc.) |
| `renda_domiciliar_log` | float64 | log(1 + renda_domiciliar) |
| `renda_per_capita_log` | float64 | log(1 + renda_per_capita) |
| `esc_scaled` | float64 | Escolaridade padronizada |
| `renda_scaled` | float64 | Renda per capita (log) padronizada |
| `indice_socioeconomico` | float64 | Média de esc_scaled e renda_scaled |
| `idade_imc` | float64 | Interação idade_c × imc |
| `regiao_*` (5 vars) | int64 | Agregação regional das UFs |
| `n_doencas` | int64 | Contagem de DCNTs (0-16) |
| `doenca_cronica` | int64 | Presença de ≥1 DCNT (binária) |

---

## 📊 Resumo Estatístico

### Distribuição por Tipo de Dado

| Tipo | Quantidade | Variáveis |
|------|-----------|-----------|
| `bool` | 37 | UFs (26), domicílio (3), raça (5), comportamentais (3) |
| `float64` | 27 | DCNTs (16), IMC, idade, rendas, escaladas |
| `int64` | 14 | Status ordinais, contadores, binárias |
| `str` | 1 | faixa_etaria |

### Valores Ausentes (NaN/pd.NA)

- **DCNTs:** Podem conter NaN quando resposta = "Ignorado" ou "Não sabe"
- **plano_saude:** Contém NaN para respostas ignoradas
- **escolaridade_ord:** Pode conter NaN se alfabetização e escolaridade forem ambas inválidas
- **imc:** Contém NaN se peso/altura ausentes ou IMC fora da faixa válida

---

## 🔄 Pipeline de Processamento

```
Dados Brutos (PNS 2019)
    ↓
1. preprocessing.py - Limpeza e filtros
    ├─ Conversão de códigos
    ├─ Filtros de idade (≥18 anos)
    ├─ Tratamento de DCNT
    └─ Criação de n_doencas e doenca_cronica
    ↓
2. feature_engineering.py - Engenharia de features
    ├─ One-hot encoding (UF, raça, domicílio)
    ├─ Variáveis ordinais (escolaridade)
    ├─ Cálculo de IMC
    ├─ Combinações (tabagismo, álcool, atividade)
    └─ Faixa etária
    ↓
3. transformation.py - Transformações estatísticas
    ├─ Log de rendas
    ├─ Centralização de idade
    └─ Termos polinomiais
    ↓
4. Notebook modelagem.ipynb - Features adicionais
    ├─ Agregação regional
    ├─ Interação idade_imc
    └─ Índice socioeconômico
    ↓
Dataset Final (79 variáveis × 74.304 obs)
```

---

## 📖 Notas Metodológicas

### Tratamento de Valores Ausentes
- **DCNTs:** Código 9 ("Ignorado") → NaN
- **Plano de saúde:** Código 9 → NaN
- **IMC:** Valores <10 ou >70 → NaN (biologicamente implausíveis)
- **Na contagem de doenças:** NaN tratado como ausência (0) apenas para n_doencas

### One-Hot Encoding
- Utiliza `drop_first=True` para evitar multicolinearidade
- Categorias de referência (baseline):
  - **UF:** AC (Acre)
  - **Raça/Cor:** Branca
  - **Tipo de Domicílio:** Casa

### Padronização
- **StandardScaler:** Aplicado em esc_scaled, renda_scaled
- **Centralização:** Aplicada em idade_c (média = 0)
- **Log-transformação:** Aplicada em rendas (log1p para preservar zeros)

### Ajustes Lógicos Estruturais
1. **Doenças do coração:** Se `doenca_coracao = 0`, então subtipos (infarto, angina, insuficiencia_cardiaca, arritmia) = 0
2. **Doenças pulmonares:** Se `doenca_pulmao = 0`, então subtipos (enfisema, bronquite) = 0

---

## 📚 Referências

- **Fonte de dados:** IBGE - Pesquisa Nacional de Saúde (PNS) 2019
- **Documentação PNS:** https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html
- **Dicionário original:** input_PNS_2019.txt (IBGE)
- **Configurações:** `data/config/pns_config.json`

---

**Última atualização:** 2026-03-09  
**Versão do dataset:** PNS 2019 - Processado Final  
**Arquivo de dados:** `data/processed/pns_2019_transformed.csv`
