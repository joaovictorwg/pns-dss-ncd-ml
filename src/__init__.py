"""
Pacote src: módulos de pré-processamento, engenharia e modelagem.

Estrutura KDD:
- selection.py: seleção de features
- preprocessing.py: limpeza e validação
- feature_engineering.py: criação de variáveis
- transformation.py: transformações estatísticas
- modeling.py: pipelines e modelos (futuro)
- evaluation.py: métricas e avaliação (futuro)
- pipeline.py: orquestração
"""

from .selection import select_features
from .preprocessing import clean_pns_data
from .feature_engineering import apply_feature_engineering
from .transformation import apply_transformations
from .pipeline import run_preprocessing_pipeline

__all__ = [
    'select_features',
    'clean_pns_data',
    'apply_feature_engineering',
    'apply_transformations',
    'run_preprocessing_pipeline',
]
