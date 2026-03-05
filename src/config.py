"""
Configurações centralizadas do projeto.
Caminhos, constantes e parâmetros globais.
"""

from pathlib import Path

# Diretório base do projeto
PROJECT_ROOT = Path(__file__).parent.parent

# Caminhos de dados
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CONFIG_DIR = DATA_DIR / "config"

# Arquivos
RAW_DATA_FILE = RAW_DATA_DIR / "pns_2019.csv"
SELECTED_DATA_FILE = PROCESSED_DATA_DIR / "pns_2019_selected.csv"
CLEANED_DATA_FILE = PROCESSED_DATA_DIR / "pns_2019_cleaned.csv"
ENGINEERED_DATA_FILE = PROCESSED_DATA_DIR / "pns_2019_engineered.csv"
TRANSFORMED_DATA_FILE = PROCESSED_DATA_DIR / "pns_2019_transformed.csv"

# Parâmetros de limpeza
MIN_AGE = 18
VALID_AGE_RANGE = (0, 130)

# Parâmetros de renda (sem winsorização)
# Mantém valores naturais para transformação log

# Estado (UF) - Mapa de códigos para siglas
UF_MAP = {
    11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO',
    21: 'MA', 22: 'PI', 23: 'CE', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL',
    28: 'SE', 29: 'BA', 31: 'MG', 32: 'ES', 33: 'RJ', 35: 'SP', 41: 'PR',
    42: 'SC', 43: 'RS', 50: 'MS', 51: 'MT', 52: 'GO', 53: 'DF'
}

# Raça/Cor
RACE_MAP = {
    1: 'Branca',
    2: 'Preta',
    3: 'Amarela',
    4: 'Parda',
    5: 'Indigena',
    9: 'Ignorado'
}

RACE_CATEGORIES = ['Branca', 'Preta', 'Amarela', 'Parda', 'Indigena', 'Ignorado']

# Tipo de domicílio
HOUSING_TYPE_MAP = {
    1: 'Casa',
    2: 'Apartamento',
    3: 'Cortico',
    9: 'Ignorado'
}

HOUSING_TYPE_CATEGORIES = ['Casa', 'Apartamento', 'Cortico', 'Ignorado']

# Água canalizada (ordinal)
WATER_MAP = {
    1: 2,  # Melhor: canalizada no cômodo
    2: 1,  # Intermediário: no terreno
    3: 0   # Pior: não canalizada
}

# Internet
INTERNET_MAP = {
    1: 1,  # Sim
    2: 0   # Não
}

# Escolaridade - níveis
EDUCATION_LEVELS = {
    'analfabeto': 0,
    'fundamental': 1,
    'medio': 2,
    'superior': 3,
    'pos_graduacao': 4
}

EDUCATION_FUNDAMENTAL = [3, 4, 5, 6, 7, 8]
EDUCATION_MEDIO = [9, 10, 11]
EDUCATION_SUPERIOR = [12]
EDUCATION_POS = [13, 14, 15]

# Tabagismo
SMOKING_CATEGORIES = {
    0: 'nunca_fumou',
    1: 'ex_fumante',
    2: 'fumante_atual'
}

# Álcool - intensidade
ALCOHOL_INTENSITY = {
    0: 'nunca_bebe',
    1: 'consumo_raro',
    2: 'consumo_moderado',
    3: 'consumo_frequente'
}

# Atividade física - intensidade
ACTIVITY_INTENSITY = {
    0: 'sedentario',
    1: 'baixa_frequencia',
    2: 'moderada',
    3: 'alta'
}

# IMC - Limites biológicos
IMC_MIN = 10
IMC_MAX = 70

# Doenças crônicas simples
DCNT_SIMPLES = [
    "hipertensao",
    "diabetes",
    "avc",
    "asma",
    "artrite",
    "dort",
    "depressao",
    "insuficiencia_renal"
]
