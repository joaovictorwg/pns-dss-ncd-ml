"""
Pré-processamento com limpeza, recodificação e filtros básicos

Responsabilidades:
- Conversão de códigos (1/2/9)
- Variáveis binárias
- Remoção de valores inválidos
- Filtros de população-alvo
- Conversão de tipos
- Ajustes lógicos estruturais

"""

import pandas as pd
import numpy as np
from config import (
    MIN_AGE, VALID_AGE_RANGE,
    UF_MAP, WATER_MAP, INTERNET_MAP,
    DCNT_SIMPLES
)


def tratar_uf(df):
    """
    Recodifica UF: mantém como código numérico (será one-hot na engenharia)
    Não aplica one-hot aqui
    """
    # Apenas verifica que está presente e numérica
    df_temp = df.copy()
    df_temp['uf'] = df_temp['uf'].astype('Int64')
    return df_temp


def tratar_situacao_censitaria(df):
    """
    Transforma situação censitária em variável binária:
    1 (Urbano) -> 1
    2 (Rural)  -> 0
    """
    df_temp = df.copy()

    df_temp['situacao_domicilio'] = (
        df_temp['situacao_domicilio']
        .replace({1: 1, 2: 0})
    )

    df_temp['situacao_domicilio'] = df_temp['situacao_domicilio'].astype('Int64')

    return df_temp


def tratar_tipo_domicilio(df):
    """
    Recodifica tipo de domicílio: mantém como código para one-hot na engenharia
    Converte código numérico para string
    """
    df_temp = df.copy()

    # Apenas convert para int (será mapeado na engenharia)
    df_temp['tipo_domicilio'] = df_temp['tipo_domicilio'].astype('Int64')

    return df_temp


def tratar_infraestrutura_domiciliar(df):
    """
    Trata variáveis de infraestrutura:
    - Água canalizada (mantém como ordinal)
    - Acesso à internet (binária)
    """

    df_temp = df.copy()

    # Água canalizada (ordinal: 0, 1, 2)
    mapa_agua = {
        1: 2,  # Melhor: canalizada no cômodo
        2: 1,  # Intermediário: no terreno
        3: 0   # Pior: não canalizada
    }

    df_temp['infra_agua'] = df_temp['agua_canalizada'].replace(mapa_agua)
    df_temp['infra_agua'] = df_temp['infra_agua'].astype('Int64')

    # Internet (binária: 0, 1)
    mapa_internet = {
        1: 1,  # Sim
        2: 0   # Não
    }

    df_temp['acesso_internet'] = (
        df_temp['acesso_internet'].replace(mapa_internet).astype('Int64')
    )

    # Remover colunas originais
    df_temp = df_temp.drop(columns=['agua_canalizada'])

    return df_temp


def tratar_sexo(df):
    """
    Converte sexo em variável binária:
    1 (Masculino) -> 0
    2 (Feminino)  -> 1
    """
    df_temp = df.copy()

    df_temp['sexo_feminino'] = df_temp['sexo'].replace({2: 1, 1: 0})
    df_temp['sexo_feminino'] = df_temp['sexo_feminino'].astype('Int64')

    df_temp = df_temp.drop('sexo', axis=1)

    return df_temp


def tratar_idade(df):
    """
    Pré-processamento de idade:
    - Remove valores inválidos (<0 ou >130)
    - Filtra população adulta (>=18 anos)
    - Converte para float

    """

    df_temp = df.copy()

    # Remover valores inconsistentes
    df_temp = df_temp[
        (df_temp['idade'] >= VALID_AGE_RANGE[0]) &
        (df_temp['idade'] <= VALID_AGE_RANGE[1])
    ]

    # Restringir à população adulta
    df_temp = df_temp[df_temp['idade'] >= MIN_AGE]

    # Garantir tipo numérico
    df_temp['idade'] = df_temp['idade'].astype('float64')

    return df_temp


def tratar_raca(df):
    """
    Recodifica raça/cor: mantém como código para one-hot na engenharia
    Converte para string conforme mapa
    """
    df_temp = df.copy()

    # Converter para int primeiro
    df_temp['raca'] = df_temp['raca'].astype('Int64')

    # Apenas verifica validação
    valid_races = set(UF_MAP.keys())
    # Deixa para engenharia fazer o mapeamento completo

    return df_temp


def tratar_alfabetizado(df):
    """
    Trata alfabetismo:
    - Converte para variável binária (1 = sim, 0 = não)
    - Converte 'Ignorado' (9) para NaN
    """

    df_temp = df.copy()

    mapa_alfabetizado = {
        1: 1,  # Sim
        2: 0   # Não
    }

    df_temp['alfabetizado'] = df_temp['alfabetizado'].replace(mapa_alfabetizado)

    # 9 vira NaN
    df_temp.loc[~df_temp['alfabetizado'].isin([0, 1]), 'alfabetizado'] = pd.NA

    df_temp['alfabetizado'] = df_temp['alfabetizado'].astype('float64')

    return df_temp


def tratar_escolaridade_bruta(df):
    """
    Mantém escolaridade como código numérico 
    """
    df_temp = df.copy()

    df_temp['escolaridade'] = df_temp['escolaridade'].astype('Int64')

    return df_temp


def tratar_plano_saude(df):
    """
    Trata plano de saúde:
    - Converte para variável binária (1 = possui, 0 = não possui)
    - Trata 'Ignorado' (9) como NaN
    """

    df_temp = df.copy()

    mapa_plano = {
        1: 1,  # Sim
        2: 0   # Não
    }

    df_temp['plano_saude'] = df_temp['plano_saude'].replace(mapa_plano)

    # Valores diferentes de 0 e 1 viram NaN
    df_temp.loc[~df_temp['plano_saude'].isin([0, 1]), 'plano_saude'] = pd.NA

    df_temp['plano_saude'] = df_temp['plano_saude'].astype('float64')

    return df_temp


def tratar_renda_bruta(df):
    """
    Pré-processamento de renda:
        Remove valores negativos
        Converte para float
    """

    df_temp = df.copy()

    # Remover valores negativos
    df_temp = df_temp[df_temp['renda_domiciliar'] >= 0]
    df_temp = df_temp[df_temp['renda_per_capita'] >= 0]

    # Converter para float
    df_temp['renda_domiciliar'] = df_temp['renda_domiciliar'].astype('float64')
    df_temp['renda_per_capita'] = df_temp['renda_per_capita'].astype('float64')

    return df_temp


def tratar_peso_altura_bruto(df):
    """
    Pré-processamento de peso e altura:
    - Remove valores inválidos
    - Converte para float
    """

    df_temp = df.copy()

    # Tratar valores inválidos
    df_temp.loc[df_temp['peso'] <= 0, 'peso'] = np.nan
    df_temp.loc[df_temp['altura'] <= 0, 'altura'] = np.nan
    df_temp.loc[df_temp['altura'] == 999, 'altura'] = np.nan  # código ignorado

    # Converter para float
    df_temp['peso'] = df_temp['peso'].astype('float64')
    df_temp['altura'] = df_temp['altura'].astype('float64')

    return df_temp


def tratar_tabagismo_bruto(df):
    """
    Pré-processamento de tabagismo:
    """

    df_temp = df.copy()

    # Apenas converte para int
    df_temp['fumante_atual'] = df_temp['fumante_atual'].astype('Int64')
    df_temp['fumou_passado'] = df_temp['fumou_passado'].astype('Int64')

    return df_temp


def tratar_alcool_bruto(df):
    """
    Pré-processamento de álcool:

    """

    df_temp = df.copy()

    # Apenas converte para int
    df_temp['alcool_frequencia'] = df_temp['alcool_frequencia'].astype('Int64')
    df_temp['alcool_dia_semana'] = df_temp['alcool_dia_semana'].astype('Int64')

    return df_temp


def tratar_atividade_fisica_bruta(df):
    """
    Pré-processamento de atividade física:

    """

    df_temp = df.copy()

    # Apenas converte para int
    df_temp['atividade_fisica'] = df_temp['atividade_fisica'].astype('Int64')
    df_temp['atividade_fisica_frequencia'] = df_temp['atividade_fisica_frequencia'].astype('Int64')

    return df_temp


def tratar_dcnts_simples(df):
    """
    Tratamento padronizado para DCNTs sem complexidade:
    Converte:
        1 (Sim) -> 1
        2 (Não) -> 0
        9 (Ignorado) -> NaN
    """

    df_temp = df.copy()

    for col in DCNT_SIMPLES:
        if col in df_temp.columns:
            df_temp[col] = df_temp[col].replace({
                1: 1,
                2: 0,
                9: np.nan
            }).astype('float64')

    return df_temp


def tratar_doenca_coracao(df):
    """
    Trata doença do coração e subtipos:
    - Converte 1 -> 1, 2 -> 0, 9 -> NaN
    - Ajusta coerência lógica:
        Se doenca_coracao == 0, então subtipos = 0
    """

    df_temp = df.copy()

    colunas = [
        "doenca_coracao",
        "infarto",
        "angina",
        "insuficiencia_cardiaca",
        "arritmia"
    ]

    # Conversão padrão
    for col in colunas:
        if col in df_temp.columns:
            df_temp[col] = df_temp[col].replace({
                1: 1,
                2: 0,
                9: np.nan
            }).astype('float64')

    # Ajuste lógico estrutural
    if "doenca_coracao" in df_temp.columns:
        df_temp.loc[
            df_temp["doenca_coracao"] == 0,
            ["infarto", "angina", "insuficiencia_cardiaca", "arritmia"]
        ] = 0

    return df_temp


def tratar_doenca_pulmonar(df):
    """
    Trata doença pulmonar e subtipos:
    - Converte 1 -> 1, 2 -> 0, 9 -> NaN
    - Ajusta coerência lógica:
        Se doenca_pulmao == 0, então enfisema = 0 e bronquite = 0
    """

    df_temp = df.copy()

    colunas = [
        "doenca_pulmao",
        "enfisema",
        "bronquite"
    ]

    # Conversão padrão
    for col in colunas:
        if col in df_temp.columns:
            df_temp[col] = df_temp[col].replace({
                1: 1,
                2: 0,
                9: np.nan
            }).astype('float64')

    # Ajuste lógico estrutural
    if "doenca_pulmao" in df_temp.columns:
        df_temp.loc[
            df_temp["doenca_pulmao"] == 0,
            ["enfisema", "bronquite"]
        ] = 0

    return df_temp


def criar_variaveis_agregadas_doencas(df):
    """
    Cria variáveis agregadas para análise de multimorbidade

    Variáveis criadas:
    - n_doencas: contagem total de DCNTs por indivíduo
    - doenca_cronica: binária indicando presença de pelo menos 1 DCNT

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame com variáveis de DCNTs já tratadas

    Returns
    -------
    pd.DataFrame
        DataFrame com variáveis agregadas adicionadas
    """
    df_temp = df.copy()

    # Lista completa de DCNTs
    doencas = [
        "hipertensao", "diabetes", "doenca_coracao", "infarto",
        "angina", "insuficiencia_cardiaca", "arritmia",
        "avc", "asma", "artrite", "dort", "depressao",
        "doenca_pulmao", "enfisema", "bronquite",
        "insuficiencia_renal"
    ]

    # Contagem de doenças (soma por linha)
    # fillna(0) para tratar missing como ausência de doença na contagem
    df_temp["n_doencas"] = df_temp[doencas].fillna(0).sum(axis=1).astype('Int64')

    # Variável binária: tem pelo menos 1 DCNT
    df_temp["doenca_cronica"] = (df_temp["n_doencas"] > 0).astype('Int64')

    return df_temp


def clean_pns_data(df):
    """
    Função orquestra aplica limpeza e pré-processamento

    Etapas:
    1. Filtra público-alvo (tem resposta para peso, recorte do modulo individual)
    2. Aplica todas as funções de limpeza

    """

    # FILTRAGEM INICIAL: Modulo Individual da PNS, morador selecionado
    df_clean = df.dropna(subset=['peso']).copy()

    print(f"Após filtro de público-alvo (com resposta): {df_clean.shape[0]} registros")

    # Aplicar todas as funções de limpeza
    df_clean = tratar_uf(df_clean)
    df_clean = tratar_situacao_censitaria(df_clean)
    df_clean = tratar_tipo_domicilio(df_clean)
    df_clean = tratar_infraestrutura_domiciliar(df_clean)
    df_clean = tratar_sexo(df_clean)
    df_clean = tratar_idade(df_clean)
    df_clean = tratar_raca(df_clean)
    df_clean = tratar_alfabetizado(df_clean)
    df_clean = tratar_escolaridade_bruta(df_clean)
    df_clean = tratar_plano_saude(df_clean)
    df_clean = tratar_renda_bruta(df_clean)
    df_clean = tratar_peso_altura_bruto(df_clean)
    df_clean = tratar_tabagismo_bruto(df_clean)
    df_clean = tratar_alcool_bruto(df_clean)
    df_clean = tratar_atividade_fisica_bruta(df_clean)
    df_clean = tratar_dcnts_simples(df_clean)
    df_clean = tratar_doenca_coracao(df_clean)
    df_clean = tratar_doenca_pulmonar(df_clean)
    
    # Criar variáveis agregadas de multimorbidade
    df_clean = criar_variaveis_agregadas_doencas(df_clean)

    print(f"Limpeza completa: {df_clean.shape[0]} registros, {df_clean.shape[1]} features")

    return df_clean
