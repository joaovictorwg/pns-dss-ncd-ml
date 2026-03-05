"""
Pipeline principal para orquestração do flucxo completo de pré-processamento

"""

import pandas as pd
from selection import select_features
from preprocessing import clean_pns_data
from feature_engineering import apply_feature_engineering
from transformation import apply_transformations
from config import (
    RAW_DATA_FILE, SELECTED_DATA_FILE,
    CLEANED_DATA_FILE, ENGINEERED_DATA_FILE, TRANSFORMED_DATA_FILE
)


def run_preprocessing_pipeline(
    input_file=None,
    save_intermediate=False,
    skip_to_stage=None
):
    """
    Executa o pipeline completo de pré-processamento

    Etapas:
    1. Seleção de features
    2. Limpeza (clean_pns_data)
    3. Engenharia de features (apply_feature_engineering)
    4. Transformações estatísticas (apply_transformations)

    Parameters
    ----------
    input_file : str or Path, optional
        Caminho do arquivo bruto. Padrão: config.RAW_DATA_FILE

    save_intermediate : bool, default False
        Se True, salva saída de cada etapa em CSV.

    skip_to_stage : int, optional
        Inicia pipeline em etapa específica.
        1: seleção
        2: limpeza
        3: engenharia
        4: transformação
        None: executa todas (padrão)

    Returns
    -------
    pd.DataFrame
        DataFrame final transformado e pronto para modelagem.

    Example
    -------
    > df_final = run_preprocessing_pipeline(save_intermediate=True)
    > df_final.shape
    (50000, 120)
    """

    if input_file is None:
        input_file = RAW_DATA_FILE

    print("=" * 70)
    print("INICIANDO PIPELINE DE PRÉ-PROCESSAMENTO")
    print("=" * 70)

    # ============ ETAPA 1: Seleção de Features ============
    if skip_to_stage is None or skip_to_stage <= 1:
        print("\n[1/4] SELEÇÃO DE FEATURES")
        print("-" * 70)

        try:
            df_selected = select_features(
                input_file=input_file,
                output_file=SELECTED_DATA_FILE
            )
        except FileNotFoundError:
            print(f" Arquivo não encontrado: {input_file}")
            raise

        if save_intermediate:
            df_selected.to_csv(SELECTED_DATA_FILE, index=False)
            print(f"    Salvo: {SELECTED_DATA_FILE}")
    else:
        print(f"\n[1/4] Pulando para etapa {skip_to_stage}")
        try:
            df_selected = pd.read_csv(SELECTED_DATA_FILE)
            print(f"   Carregado de {SELECTED_DATA_FILE}: {df_selected.shape}")
        except FileNotFoundError:
            print(f" Arquivo de seleção não encontrado. Execute sem skip_to_stage=1")
            raise

    # ============ ETAPA 2: Limpeza ============
    if skip_to_stage is None or skip_to_stage <= 2:
        print("\n[2/4] LIMPEZA E VALIDAÇÃO")
        print("-" * 70)

        df_cleaned = clean_pns_data(df_selected)

        if save_intermediate:
            df_cleaned.to_csv(CLEANED_DATA_FILE, index=False)
            print(f"   Salvo: {CLEANED_DATA_FILE}")
    else:
        try:
            df_cleaned = pd.read_csv(CLEANED_DATA_FILE)
            print(f"[2/4] Carregado de {CLEANED_DATA_FILE}: {df_cleaned.shape}")
        except FileNotFoundError:
            print(f" Arquivo limpo não encontrado.")
            raise

    # ============ ETAPA 3: Engenharia de Features ============
    if skip_to_stage is None or skip_to_stage <= 3:
        print("\n[3/4] ENGENHARIA DE FEATURES")
        print("-" * 70)

        df_engineered = apply_feature_engineering(df_cleaned)

        if save_intermediate:
            df_engineered.to_csv(ENGINEERED_DATA_FILE, index=False)
            print(f"   Salvo: {ENGINEERED_DATA_FILE}")
    else:
        try:
            df_engineered = pd.read_csv(ENGINEERED_DATA_FILE)
            print(f"[3/4] Carregado de {ENGINEERED_DATA_FILE}: {df_engineered.shape}")
        except FileNotFoundError:
            print(f"Arquivo engenheirado não encontrado.")
            raise

    # ============ ETAPA 4: Transformações Estatísticas ============
    if skip_to_stage is None or skip_to_stage <= 4:
        print("\n[4/4] TRANSFORMAÇÕES ESTATÍSTICAS")
        print("-" * 70)

        df_final = apply_transformations(df_engineered)

        if save_intermediate:
            df_final.to_csv(TRANSFORMED_DATA_FILE, index=False)
            print(f"   Salvo: {TRANSFORMED_DATA_FILE}")
    else:
        try:
            df_final = pd.read_csv(TRANSFORMED_DATA_FILE)
            print(f"[4/4] Carregado de {TRANSFORMED_DATA_FILE}: {df_final.shape}")
        except FileNotFoundError:
            print(f"Arquivo transformado não encontrado.")
            raise

    # ============ Resumo Final ============
    print("\n" + "=" * 70)
    print("PIPELINE CONCLUÍDO COM SUCESSO!")
    print("=" * 70)
    print(f"\nResumo Final:")
    print(f"   Registros: {df_final.shape[0]:,}")
    print(f"   Features: {df_final.shape[1]}")
    print(f"   Memória: {df_final.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    print(f"\nArquivo final: {TRANSFORMED_DATA_FILE}")
    print()

    return df_final


if __name__ == "__main__":
    # Executar pipeline completo com salvamento
    df = run_preprocessing_pipeline(save_intermediate=True)

    # Exibir informações básicas
    print("\nPrimeiras linhas:")
    print(df.head())

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nValores faltantes:")
    print(df.isna().sum()[df.isna().sum() > 0])
