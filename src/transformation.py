"""
Transformações estatísticas: log, centralização, padronização e scaling

Responsabilidades:
- Transformação log de variáveis de renda
- Centralização de variáveis contínuas
- Termos polinomiais
- Scaling (futuro: sklearn Pipeline)


Importante: as transformações devem ser realizadas dentro de uma pipeline de modelagem
para evitar data leakage 
"""

import pandas as pd
import numpy as np


def transform_renda(df):
    """
    Transformação logarítmica de variáveis de renda.

    - Aplica log1p para preservar zeros
    - Remove variáveis originais
    - NÃO faz winsorização

    """

    df_temp = df.copy()

    # Aplicar log1p (previne log de zero)
    df_temp['renda_domiciliar_log'] = np.log1p(df_temp['renda_domiciliar'])
    df_temp['renda_per_capita_log'] = np.log1p(df_temp['renda_per_capita'])

    # Remover versões originais
    df_temp = df_temp.drop(columns=['renda_domiciliar', 'renda_per_capita'])

    return df_temp


def transform_idade(df):
    """
    Centralização e polinômio de idade.

    - Centraliza em torno da média
    - Cria termo quadrático centralizado
    - Remove variável original


    """

    df_temp = df.copy()

    # Calcular média (em princípio, usar estatísticas de treino em produção)
    media_idade = df_temp['idade'].mean()

    # Centralizar
    df_temp['idade_c'] = df_temp['idade'] - media_idade

    # Termo quadrático centralizado
    df_temp['idade_c2'] = df_temp['idade_c'] ** 2

    # Remover original
    df_temp = df_temp.drop(columns=['idade'])

    return df_temp


def apply_transformations(df):
    """
    Função orquestradora: aplica transformações estatísticas.

    Etapas:
    1. Log de renda
    2. Centralização e polinômio de idade


    """

    df_trans = df.copy()

    print(f"Aplicando transformações estatísticas: {df_trans.shape[0]} registros")

    df_trans = transform_renda(df_trans)
    df_trans = transform_idade(df_trans)

    print(f"Transformações completas: {df_trans.shape[0]} registros, {df_trans.shape[1]} features")

    return df_trans
