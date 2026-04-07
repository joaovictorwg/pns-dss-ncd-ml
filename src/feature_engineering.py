"""
enghenharia de features: criação de variaveis, composicoes, e transformacoes categoricas

responsabilidades:
- One-hot encoding (UF, raça, tipo domicílio)
- Criação de variáveis ordinais (escolaridade)
- Combinações de variáveis (tabagismo, álcool, atividade física)
- Cálculo de IMC

"""

import pandas as pd
import numpy as np
from config import (
    UF_MAP, RACE_MAP, RACE_CATEGORIES,
    HOUSING_TYPE_MAP, HOUSING_TYPE_CATEGORIES,
    EDUCATION_LEVELS, EDUCATION_FUNDAMENTAL, EDUCATION_MEDIO,
    EDUCATION_SUPERIOR, EDUCATION_POS,
    IMC_MIN, IMC_MAX
)


def tratar_uf(df):
    """
    one-hot para uf usando drop_first
    evitar multicolinearidade
    """
    df_temp = df.copy()

    # mapeia codigo para sigla
    df_temp['uf'] = df_temp['uf'].map(UF_MAP)

    # define categorias fixas
    categorias_uf = sorted(UF_MAP.values())
    df_temp['uf'] = pd.Categorical(df_temp['uf'], categories=categorias_uf)

    # gera dummies
    df_uf_dummies = pd.get_dummies(
        df_temp['uf'],
        prefix='uf',
        drop_first=True
    )

    # concatena e remove original
    df_result = pd.concat(
        [df_temp.drop(columns=['uf']), df_uf_dummies],
        axis=1
    )

    return df_result


def tratar_tipo_domicilio(df):
    """
    one-hot encoding para tipo domicilio
    """
    df_temp = df.copy()

    # mapeia codigo para nome
    df_temp['tipo_domicilio'] = df_temp['tipo_domicilio'].map(HOUSING_TYPE_MAP)

    # define categorias fixas
    df_temp['tipo_domicilio'] = pd.Categorical(
        df_temp['tipo_domicilio'],
        categories=HOUSING_TYPE_CATEGORIES
    )

    # gera dummies
    df_dom_dummies = pd.get_dummies(
        df_temp['tipo_domicilio'],
        prefix='domicilio',
        drop_first=True
    )

    # Cconcatena e remove original
    df_result = pd.concat(
        [df_temp.drop(columns=['tipo_domicilio']), df_dom_dummies],
        axis=1
    )

    return df_result


def tratar_raca(df):
    """
    One-Hot Encoding para raça/cor.
    """
    df_temp = df.copy()

    # Mapear código para nome
    df_temp['raca'] = df_temp['raca'].map(RACE_MAP)

    # Definir categorias fixas
    df_temp['raca'] = pd.Categorical(
        df_temp['raca'],
        categories=RACE_CATEGORIES
    )

    # Gerar dummies
    df_raca_dummies = pd.get_dummies(
        df_temp['raca'],
        prefix='raca',
        drop_first=True
    )

    # Concatenar e remover original
    df_result = pd.concat(
        [df_temp.drop(columns=['raca']), df_raca_dummies],
        axis=1
    )

    return df_result


def tratar_escolaridade(df):
    """
    Cria variável ordinal de escolaridade incorporando analfabetismo.

    Níveis:
    0 = Analfabeto
    1 = Fundamental
    2 = Médio
    3 = Superior
    4 = Pós-graduação
    """
    df_temp = df.copy()

    # Criar variável Base
    df_temp['escolaridade_ord'] = pd.NA

    # Analfabetos
    df_temp.loc[df_temp['alfabetizado'] == 0, 'escolaridade_ord'] = 0

    # Fundamental
    df_temp.loc[
        df_temp['escolaridade'].isin(EDUCATION_FUNDAMENTAL),
        'escolaridade_ord'
    ] = 1

    # Médio
    df_temp.loc[
        df_temp['escolaridade'].isin(EDUCATION_MEDIO),
        'escolaridade_ord'
    ] = 2

    # Superior
    df_temp.loc[
        df_temp['escolaridade'].isin(EDUCATION_SUPERIOR),
        'escolaridade_ord'
    ] = 3

    # Pós-graduação
    df_temp.loc[
        df_temp['escolaridade'].isin(EDUCATION_POS),
        'escolaridade_ord'
    ] = 4

    # Converter para float nullable
    df_temp['escolaridade_ord'] = pd.to_numeric(
        df_temp['escolaridade_ord'],
        errors='coerce'
    )

    # Remover colunas auxiliares
    df_temp = df_temp.drop(columns=['escolaridade', 'alfabetizado'])

    return df_temp


def tratar_altura_peso_imc(df):
    """
    Calcula IMC a partir de peso e altura.

    Etapas:
    - Converte altura de cm para metros
    - Calcula IMC
    - Remove valores biologicamente implausíveis
    - Remove colunas auxiliares
    """

    df_temp = df.copy()

    # Converter altura para metros
    df_temp['altura_m'] = df_temp['altura'] / 100

    # Calcular IMC
    df_temp['imc'] = df_temp['peso'] / (df_temp['altura_m'] ** 2)

    # Remover valores biologicamente implausíveis
    df_temp.loc[
        (df_temp['imc'] < IMC_MIN) | (df_temp['imc'] > IMC_MAX),
        'imc'
    ] = np.nan

    # Remover colunas auxiliares
    df_temp = df_temp.drop(columns=['peso', 'altura', 'altura_m'])

    return df_temp


def tratar_tabagismo(df):
    """
    Cria duas variáveis de tabagismo:
    
    1. tabagismo_status (ordinal):
        0 = nunca fumou
        1 = ex-fumante
        2 = fumante atual
    
    2. tabagismo_ativo (booleano):
        True = fuma atualmente
        False = não fuma ou nunca fumou
    
    Remove colunas originais (fumante_atual, fumou_passado).
    """

    df_temp = df.copy()

    # Criar variável ordinal
    df_temp['tabagismo_status'] = np.nan

    # Fumante atual
    df_temp.loc[
        df_temp['fumante_atual'].isin([1, 2]),
        'tabagismo_status'
    ] = 2

    # Não fuma atualmente
    nao_atual = df_temp['fumante_atual'] == 3

    # Ex-fumante
    df_temp.loc[
        nao_atual & df_temp['fumou_passado'].isin([1, 2]),
        'tabagismo_status'
    ] = 1

    # Nunca fumou
    df_temp.loc[
        nao_atual & (df_temp['fumou_passado'] == 3),
        'tabagismo_status'
    ] = 0

    # Converter para inteiro (nullable)
    df_temp['tabagismo_status'] = df_temp['tabagismo_status'].astype('Int64')

    # Criar variável booleana: True se fuma atualmente
    df_temp['tabagismo_ativo'] = df_temp['fumante_atual'].isin([1, 2])

    # Remover colunas originais
    df_temp = df_temp.drop(
        columns=['fumante_atual', 'fumou_passado']
    )

    return df_temp


def tratar_alcool(df):
    """
    Cria duas variáveis de álcool:
    
    1. alcool_status (ordinal):
        0 = nunca bebe
        1 = consumo raro
        2 = consumo moderado (1-2 dias/semana)
        3 = consumo frequente (≥3 dias/semana)
    
    2. alcool_ativo (booleano):
        True = bebe atualmente (qualquer frequência)
        False = nunca bebeu
    
    Remove colunas originais.
    """

    df_temp = df.copy()

    # Criar variável ordinal
    df_temp['alcool_status'] = np.nan

    # Nunca bebe
    df_temp.loc[
        df_temp['alcool_frequencia'] == 1,
        'alcool_status'
    ] = 0

    # Consumo raro
    df_temp.loc[
        (df_temp['alcool_frequencia'] == 2) |
        ((df_temp['alcool_frequencia'] == 3) &
         (df_temp['alcool_dia_semana'] == 0)),
        'alcool_status'
    ] = 1

    # Consumo moderado (1–2 dias/semana)
    df_temp.loc[
        df_temp['alcool_dia_semana'].isin([1, 2]),
        'alcool_status'
    ] = 2

    # Consumo frequente (≥3 dias/semana)
    df_temp.loc[
        df_temp['alcool_dia_semana'] >= 3,
        'alcool_status'
    ] = 3

    # Converter para inteiro (nullable)
    df_temp['alcool_status'] = df_temp['alcool_status'].astype('Int64')

    # Criar variável booleana: True se bebe atualmente (qualquer frequência)
    df_temp['alcool_ativo'] = df_temp['alcool_frequencia'] != 1

    # Remover colunas originais
    df_temp = df_temp.drop(
        columns=['alcool_frequencia', 'alcool_dia_semana']
    )

    return df_temp


def tratar_atividade_fisica(df):
    """
    Cria duas variáveis de atividade física:
    
    1. atividade_status (ordinal):
        0 = sedentário
        1 = baixa frequência (1-2 dias/semana)
        2 = moderada (3-4 dias/semana)
        3 = alta (≥5 dias/semana)
    
    2. atividade_ativo (booleano):
        True = pratica atividade física regularmente
        False = sedentário
    
    Remove colunas originais.
    """

    df_temp = df.copy()

    # Criar variável ordinal
    df_temp['atividade_status'] = np.nan

    # Sedentário
    df_temp.loc[
        (df_temp['atividade_fisica'] == 2) |
        (df_temp['atividade_fisica_frequencia'] == 0),
        'atividade_status'
    ] = 0

    # Baixa frequência (1–2 dias)
    df_temp.loc[
        df_temp['atividade_fisica_frequencia'].isin([1, 2]),
        'atividade_status'
    ] = 1

    # Moderada (3–4 dias)
    df_temp.loc[
        df_temp['atividade_fisica_frequencia'].isin([3, 4]),
        'atividade_status'
    ] = 2

    # Alta (≥5 dias)
    df_temp.loc[
        df_temp['atividade_fisica_frequencia'] >= 5,
        'atividade_status'
    ] = 3

    # Converter para inteiro (nullable)
    df_temp['atividade_status'] = df_temp['atividade_status'].astype('Int64')

    # Criar variável booleana: True se é ativo (pratica atividade)
    df_temp['atividade_ativo'] = (df_temp['atividade_fisica'] == 1)

    # Remover originais
    df_temp = df_temp.drop(
        columns=['atividade_fisica', 'atividade_fisica_frequencia']
    )

    return df_temp


def criar_faixa_etaria(df):
    """
    Cria variável categórica de faixa etária a partir de idade.
    
    Categorias:
    - 18-29 anos
    - 30-39 anos
    - 40-49 anos
    - 50-59 anos
    - 60+ anos
    
    IMPORTANTE: Esta função deve ser chamada ANTES de transformation.py
    (que remove a coluna 'idade'). Usa a idade original, não idade_c ou idade_c2.
    """
    
    df_temp = df.copy()
    
    df_temp['faixa_etaria'] = pd.cut(
        df_temp['idade'],
        bins=[18, 30, 40, 50, 60, 120],
        labels=['18-29', '30-39', '40-49', '50-59', '60+'],
        include_lowest=True
    )
    
    return df_temp


def apply_feature_engineering(df):
    """
    Função orquestradora aplica engenharia de features

    Etapas:
    1. One-hot encoding (UF, raça, tipo domicílio, álcool, atividade)
    2. Criação de variáveis ordinais (escolaridade, tabagismo)
    3. Cálculo de IMC

    Parameters
   
    df : pd.DataFrame
        DataFrame já limpo (saída de clean_pns_data)

    Returns

    pd.DataFrame
        DataFrame com features engenheiradas, pronto para transformações estatísticas

    Não salva CSV
    """

    df_feat = df.copy()

    print(f"Iniciando engenharia de features: {df_feat.shape[0]} registros")

    df_feat = tratar_uf(df_feat)
    df_feat = tratar_tipo_domicilio(df_feat)
    df_feat = tratar_raca(df_feat)
    df_feat = tratar_escolaridade(df_feat)
    df_feat = tratar_altura_peso_imc(df_feat)
    df_feat = tratar_tabagismo(df_feat)
    df_feat = tratar_alcool(df_feat)
    df_feat = tratar_atividade_fisica(df_feat)
    df_feat = criar_faixa_etaria(df_feat)

    # ===== Variáveis derivadas adicionais para compatibilidade com dicionário =====
    # 1. Interação idade_imc
    if 'idade_c' in df_feat.columns and 'imc' in df_feat.columns:
        df_feat['idade_imc'] = df_feat['idade_c'] * df_feat['imc']
    # 2. Variáveis de região
    uf_regioes = {
        'regiao_norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
        'regiao_nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
        'regiao_centro_oeste': ['DF', 'GO', 'MT', 'MS'],
        'regiao_sudeste': ['ES', 'MG', 'RJ', 'SP'],
        'regiao_sul': ['PR', 'RS', 'SC']
    }
    for reg, ufs in uf_regioes.items():
        colnames = [f'uf_{uf}' for uf in ufs if f'uf_{uf}' in df_feat.columns]
        if colnames:
            df_feat[reg] = df_feat[colnames].any(axis=1).astype(int)
        else:
            df_feat[reg] = 0
    # 3. Índice socioeconômico
    df_feat = add_socioeconomic_index(df_feat)
    print(f"Engenharia completa: {df_feat.shape[0]} registros, {df_feat.shape[1]} features")
    return df_feat

# Função para ser chamada após as transformações estatísticas (após existir renda_per_capita_log e idade_c)
def add_socioeconomic_index(df):
    """
    Adiciona esc_scaled, renda_scaled e indice_socioeconomico ao DataFrame.

    Regras para renda_scaled:
    - Usa renda_per_capita_log quando já existir.
    - Se ainda não existir (etapa de engenharia), usa log1p(renda_per_capita).
    """
    df_out = df.copy()

    if 'escolaridade_ord' in df_out.columns:
        esc_mean = df_out['escolaridade_ord'].mean()
        esc_std = df_out['escolaridade_ord'].std(ddof=0)
        df_out['esc_scaled'] = (df_out['escolaridade_ord'] - esc_mean) / esc_std if esc_std > 0 else 0

    renda_base = None
    if 'renda_per_capita_log' in df_out.columns:
        renda_base = df_out['renda_per_capita_log']
    elif 'renda_per_capita' in df_out.columns:
        renda_base = np.log1p(df_out['renda_per_capita'])

    if renda_base is not None:
        renda_mean = renda_base.mean()
        renda_std = renda_base.std(ddof=0)
        df_out['renda_scaled'] = (renda_base - renda_mean) / renda_std if renda_std > 0 else 0

    if 'esc_scaled' in df_out.columns and 'renda_scaled' in df_out.columns:
        df_out['indice_socioeconomico'] = df_out[['esc_scaled', 'renda_scaled']].mean(axis=1)

    return df_out


def apply_post_transformation_feature_engineering(df):
    """
    Aplica features de engenharia que dependem de colunas criadas em
    transformation.py (ex.: renda_per_capita_log).
    """
    df_out = df.copy()
    df_out = add_socioeconomic_index(df_out)
    return df_out
