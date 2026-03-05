"""
Exemplos de uso da pipeline de pré-processamento.

Modulo: examples.py 
"""

import pandas as pd

# =============================================================================
#   PIPELINE AUTOMATICA COMPLETA
# =============================================================================

from pipeline import run_preprocessing_pipeline

def exemplo_1_pipeline_completo():
    """
    Executa pipeline completo: seleção → limpeza → engenharia → transformação
    """
    
    # executa a pipeline completa, salvando cada etapa em csv
    df_final = run_preprocessing_pipeline(
        save_intermediate=True  # serve para salvar cada etapa em csv
    )
    
    print(f" Shape final: {df_final.shape}")
    print(f" Colunas: {df_final.columns.tolist()}")
    
    return df_final


# =============================================================================
# ETAPAS INDIVIDUAIS PARA EXPLORAÇÃO
# =============================================================================

from selection import select_features
from preprocessing import clean_pns_data
from feature_engineering import apply_feature_engineering
from transformation import apply_transformations

def exemplo_2_etapas_individuais():
    """
    executa as etapas individuais para exploração e inspeção 
    """
    
    # Seleção
    print("[1] Executando seleção de features...")
    df_selected = select_features()
    print(f"   Shape: {df_selected.shape}")
    print(f"   Colunas: {list(df_selected.columns)[:5]}...")
    
    # Limpeza
    print("\n[2] Executando limpeza...")
    df_clean = clean_pns_data(df_selected)
    print(f"   Shape: {df_clean.shape}")
    print(f"   Tipos: {df_clean.dtypes.value_counts()}")
    
    # Engenharia
    print("\n[3] Executando engenharia...")
    df_feat = apply_feature_engineering(df_clean)
    print(f"   Shape: {df_feat.shape}")
    print(f"   Características novas: {df_feat.shape[1] - df_clean.shape[1]}")
    
    # Transformações
    print("\n[4] Executando transformações...")
    df_trans = apply_transformations(df_feat)
    print(f"   Shape final: {df_trans.shape}")
    
    return df_trans


# =============================================================================
# CONTINUAR DE ALGUMA ETAPA INTERMEDIARIA
# =============================================================================

def exemplo_3_retomar_intermediario():
    """
    util para caso a pipeline for interrompida e você quer continuar
    """
    
    # continuar da engenharia (pula seleção + limpeza)
    # assume que limpeza já foi feita e salva em arquivo
    df_final = run_preprocessing_pipeline(skip_to_stage=3)
    
    return df_final


# =============================================================================
# EXPLORAÇÃO DE DADOS PÓS-PIPELINE
# =============================================================================

import pandas as pd
import numpy as np

def exemplo_4_exploracao_pos_pipeline():
    """
    analise dos dados depois da pipeline
    """
    
    df = run_preprocessing_pipeline(save_intermediate=False)
    
    print("\n" + "=" * 70)
    print("EXPLORAÇÃO DE DADOS")
    print("=" * 70)
    
    # infos basicas
    print(f"\n1. DIMENSIONALIDADE")
    print(f"   Registros: {df.shape[0]:,}")
    print(f"   Features: {df.shape[1]}")
    print(f"   Memória: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    
    # tipos de dados
    print(f"\n2. TIPOS DE DADOS")
    print(df.dtypes.value_counts())
    
    # valores faltantes
    print(f"\n3. VALORES FALTANTES")
    na_count = df.isna().sum()
    na_pct = (na_count / len(df) * 100).round(2)
    
    if na_count.sum() > 0:
        missing_df = pd.DataFrame({
            'N_NaN': na_count[na_count > 0],
            'PCT': na_pct[na_count > 0]
        }).sort_values('N_NaN', ascending=False)
        print(missing_df)
    else:
        print("   Sem valores faltantes!")
    
    # estatisticas descritisva
    print(f"\n4. ESTATÍSTICAS NUMÉRICAS")
    print(df.describe().round(2))
    
    # colunas categoricas (one-hot)
    one_hot_cols = [col for col in df.columns if col.startswith(
        ('uf_', 'raca_', 'domicilio_', 'tabagismo_', 'alcool_', 'atividade_')
    )]
    print(f"\n5. FEATURES ONE-HOT ({len(one_hot_cols)})")
    print(f"   {one_hot_cols[:10]}{'...' if len(one_hot_cols) > 10 else ''}")
    
    # Target (hipertensão)
    if 'hipertensao' in df.columns:
        print(f"\n6. VARIÁVEL ALVO (HIPERTENSÃO)")
        print(df['hipertensao'].value_counts(dropna=False))
        print(f"   Taxa de positivos: {df['hipertensao'].mean():.2%}")
    
    return df


# =============================================================================
# INTEGRAÇÃO COM SKLEARN
# =============================================================================

def exemplo_5_sklearn_pipeline():
    """
    usando dados processados em uma pipline sklearn
    """
    
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    
    # gerar os dados
    df = run_preprocessing_pipeline(save_intermediate=False)
    
    # separar features e target
    X = df.drop(columns=['hipertensao'])
    y = df['hipertensao']
    
    # train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # pipeline sklearn (evitando leakage)
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=1000, random_state=42))
    ])
    
    # treinar
    pipe.fit(X_train, y_train)
    
    # avaliar
    train_score = pipe.score(X_train, y_train)
    test_score = pipe.score(X_test, y_test)
    
    print(f"\n Train Score: {train_score:.4f}")
    print(f" Test Score: {test_score:.4f}")
    
    return pipe


# =============================================================================
# VALIDAÇÂO DE LOGICA ENTRE ETAPAS
# =============================================================================

def exemplo_6_validar_logica():
    """
    Verificar se lógica foi mantida em cada etapa
    """
    
    from preprocessing import clean_pns_data
    from feature_engineering import apply_feature_engineering
    from transformation import apply_transformations
    from selection import select_features
    
    # carrega dados
    df = select_features()
    
    # verificacoes
    print("\n" + "=" * 70)
    print(" VALIDAÇÕES DE LÓGICA")
    print("=" * 70)
    
    # limpeza mantem publico alvo
    df_clean = clean_pns_data(df)
    print(f"\n1. PÚBLICO-ALVO (Hipertensão)")
    print(f"   Antes: {len(df)} registros")
    print(f"   Depois: {len(df_clean)} registros")
    print(f"   Removidos: {len(df) - len(df_clean):,} ({(1 - len(df_clean)/len(df))*100:.1f}%)")
    
    # engenharia cria features
    df_feat = apply_feature_engineering(df_clean)
    print(f"\n2. FEATURES")
    print(f"   Antes engenharia: {df_clean.shape[1]} features")
    print(f"   Depois engenharia: {df_feat.shape[1]} features")
    print(f"   Criadas: {df_feat.shape[1] - df_clean.shape[1]}")
    
    # transformação amantem registros
    df_trans = apply_transformations(df_feat)
    print(f"\n3. TRANSFORMAÇÕES ESTATÍSTICAS")
    print(f"   Registros: {len(df_feat)} → {len(df_trans)}")
    print(f"   Preservados: {'OK' if len(df_feat) == len(df_trans) else 'X'}")
    
    # verifica que variaveis foram removidas
    print(f"\n4. VARIÁVEIS REMOVIDAS (como esperado)")
    removed = set(df_clean.columns) - set(df_trans.columns)
    for var in sorted(removed):
        print(f"   - {var}")
    
    return df_trans


# =============================================================================
# ANÁLISE DE MULTIMORBIDADE COM VARIÁVEIS AGREGADAS
# =============================================================================

def exemplo_7_analise_multimorbidade():
    """
    Demonstra uso das variáveis agregadas n_doencas e doenca_cronica
    criadas automaticamente no preprocessing
    """
    
    from preprocessing import clean_pns_data
    from selection import select_features
    
    # Carregar e limpar dados
    df = select_features()
    df_clean = clean_pns_data(df)
    
    print("\n" + "=" * 70)
    print(" ANÁLISE DE MULTIMORBIDADE")
    print("=" * 70)
    
    # Distribuição de número de doenças
    print("\n1. DISTRIBUIÇÃO DE NÚMERO DE DOENÇAS (n_doencas)")
    print("-" * 70)
    dist_doencas = df_clean['n_doencas'].value_counts().sort_index()
    for n_doencas, count in dist_doencas.items():
        pct = count / len(df_clean) * 100
        print(f"   {n_doencas} doenças: {count:6,} ({pct:5.2f}%)")
    
    # Estatísticas descritivas
    print(f"\n   Média de doenças por pessoa: {df_clean['n_doencas'].mean():.2f}")
    print(f"   Mediana: {df_clean['n_doencas'].median():.0f}")
    print(f"   Máximo: {df_clean['n_doencas'].max():.0f}")
    
    # Prevalência de doença crônica
    print("\n2. PREVALÊNCIA DE DOENÇA CRÔNICA (doenca_cronica)")
    print("-" * 70)
    dist_cronica = df_clean['doenca_cronica'].value_counts()
    print(f"   Sem doença crônica: {dist_cronica.get(0, 0):6,} ({dist_cronica.get(0, 0)/len(df_clean)*100:5.2f}%)")
    print(f"   Com doença crônica: {dist_cronica.get(1, 0):6,} ({dist_cronica.get(1, 0)/len(df_clean)*100:5.2f}%)")
    
    # Análise por faixa etária
    print("\n3. MULTIMORBIDADE POR FAIXA ETÁRIA")
    print("-" * 70)
    df_clean['faixa_etaria'] = pd.cut(
        df_clean['idade'], 
        bins=[18, 30, 40, 50, 60, 120],
        labels=['18-29', '30-39', '40-49', '50-59', '60+']
    )
    
    print("\n   Média de doenças por faixa etária:")
    for faixa in ['18-29', '30-39', '40-49', '50-59', '60+']:
        media = df_clean[df_clean['faixa_etaria'] == faixa]['n_doencas'].mean()
        print(f"   {faixa}: {media:.2f} doenças")
    
    # Exemplo de uso em modelagem
    print("\n4. EXEMPLO PARA MODELAGEM")
    print("-" * 70)
    print("   Use 'n_doencas' como variável preditora:")
    print("     → Captura carga geral de morbidade")
    print("     → Proxy de fragilidade/vulnerabilidade")
    print("\n   Use 'doenca_cronica' para análise binária:")
    print("     → Comparar saudáveis vs acometidos")
    print("     → Modelos de classificação simples")
    
    return df_clean


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    
    import sys
    
    if len(sys.argv) > 1:
        exemplo = sys.argv[1]
    else:
        exemplo = "1"
    
    print(f"\n Executando EXEMPLO {exemplo}\n")
    
    if exemplo == "1":
        exemplo_1_pipeline_completo()
    elif exemplo == "2":
        exemplo_2_etapas_individuais()
    elif exemplo == "3":
        exemplo_3_retomar_intermediario()
    elif exemplo == "4":
        exemplo_4_exploracao_pos_pipeline()
    elif exemplo == "5":
        exemplo_5_sklearn_pipeline()
    elif exemplo == "6":
        exemplo_6_validar_logica()
    elif exemplo == "7":
        exemplo_7_analise_multimorbidade()
    else:
        print(" Exemplo não encontrado. Use 1-7")
