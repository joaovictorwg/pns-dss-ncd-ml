"""
Seleção de features a partir dos dados brutos do PNS 2019
Mapeia códigos IBGE para nomes interpretáveis
"""

import pandas as pd
from config import RAW_DATA_FILE, SELECTED_DATA_FILE


# Dicionário completo de mapeamento de variáveis
VARIABLES_MAP = {
    # Características sociodemográficas (DSS)
    "V0001": "uf",
    "V0026": "situacao_domicilio",
    "A001": "tipo_domicilio",
    "A00601": "agua_canalizada",
    "A01901": "acesso_internet",

    # Características demográficas
    "C006": "sexo",
    "C008": "idade",
    "C009": "raca",

    # Características educacionais
    "D001": "alfabetizado",
    "D00901": "escolaridade",

    # Características de saúde
    "I00102": "plano_saude",

    # Renda
    "VDF002": "renda_domiciliar",
    "VDF003": "renda_per_capita",

    # Estilo de vida - Antropometria
    "P00104": "peso",
    "P00404": "altura",

    # Estilo de vida - Tabagismo
    "P050": "fumante_atual",
    "P052": "fumou_passado",

    # Estilo de vida - Álcool
    "P027": "alcool_frequencia",
    "P02801": "alcool_dia_semana",

    # Estilo de vida - Atividade física
    "P034": "atividade_fisica",
    "P035": "atividade_fisica_frequencia",

    # Variáveis alvo (Doenças Crônicas)
    "Q00201": "hipertensao",
    "Q03001": "diabetes",

    # Bloco: Doenças do Coração
    "Q06306": "doenca_coracao",
    "Q06307": "infarto",
    "Q06308": "angina",
    "Q06309": "insuficiencia_cardiaca",
    "Q06310": "arritmia",

    # Doenças respiratórias
    "Q068": "avc",
    "Q074": "asma",
    "Q079": "artrite",
    "Q088": "dort",
    "Q092": "depressao",

    # Bloco: Doenças do Pulmão
    "Q11604": "doenca_pulmao",
    "Q11605": "enfisema",
    "Q11606": "bronquite",

    # Outras doenças crônicas
    "Q124": "insuficiencia_renal"
}


def select_features(df_raw=None, input_file=None, output_file=None):
    """
    Seleciona um subconjunto de features do dataset bruto do PNS 2019

    Mapeia códigos IBGE para nomes interpretáveis e salva arquivo pré-selecionado

    Parameters
    ----------
    df_raw : pd.DataFrame, optional
        DataFrame bruto já carregado. Se None, carrega de `input_file`

    input_file : str or Path, optional
        Caminho do arquivo CSV bruto. Padrão: config.RAW_DATA_FILE

    output_file : str or Path, optional
        Caminho para salvar features selecionadas. Padrão: config.SELECTED_DATA_FILE

    Returns
    -------
    pd.DataFrame
        DataFrame com features selecionadas e renomeadas.

    Example
    -------
    >>> df_selected = select_features()
    """

    if input_file is None:
        input_file = RAW_DATA_FILE

    if output_file is None:
        output_file = SELECTED_DATA_FILE

    # Carrega dados se não fornecidos
    if df_raw is None:
        df_raw = pd.read_csv(input_file)

    # Seleciona apenas colunas disponíveis
    available_columns = [col for col in VARIABLES_MAP.keys() if col in df_raw.columns]
    missing_columns = [col for col in VARIABLES_MAP.keys() if col not in df_raw.columns]

    if missing_columns:
        print(f"Colunas não encontradas: {missing_columns}")

    # Seleciona e renomeia
    df_selected = df_raw.loc[:, available_columns].rename(
        columns={col: VARIABLES_MAP[col] for col in available_columns}
    )

    # Salva
    df_selected.to_csv(output_file, index=False)
    print(f"Features selecionadas salvas em: {output_file}")
    print(f"   Shape: {df_selected.shape}")

    return df_selected
