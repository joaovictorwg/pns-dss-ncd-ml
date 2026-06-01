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

from importlib import import_module

__all__ = [
    'select_features',
    'clean_pns_data',
    'apply_feature_engineering',
    'apply_transformations',
    'run_preprocessing_pipeline',
]

_LAZY_EXPORTS = {
    'select_features': ('selection', 'select_features'),
    'clean_pns_data': ('preprocessing', 'clean_pns_data'),
    'apply_feature_engineering': ('feature_engineering', 'apply_feature_engineering'),
    'apply_transformations': ('transformation', 'apply_transformations'),
    'run_preprocessing_pipeline': ('pipeline', 'run_preprocessing_pipeline'),
}


def __getattr__(name):
    if name in _LAZY_EXPORTS:
        module_name, attr_name = _LAZY_EXPORTS[name]
        module = import_module(f'.{module_name}', __name__)
        return getattr(module, attr_name)
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
