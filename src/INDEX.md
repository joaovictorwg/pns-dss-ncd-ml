"""
INDICE DE DOCUMENTACAO E ARQUIVOS

Mapa completo para navegar a refatoração.
"""

# =============================================================================
# COMECAR AQUI
# =============================================================================

"""
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SE VOCÊ TEM 5 MINUTOS                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Leia: REFATORACAO_RESUMO.txt (arquivo na raiz)                         │
│  2. Execute: python src/QUICKSTART.py                                      │
│  3. Escolha opção "1" (Pipeline completo)                                  │
│                                                                             │
│  Pronto! Você tem os dados processados.                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                        SE VOCÊ TEM 15 MINUTOS                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Leia: src/README.md (documentação estruturada)                         │
│  2. Veja exemplos em: src/examples.py (6 exemplos)                         │
│  3. Execute: python src/examples.py 6 (validação de lógica)                │
│                                                                             │
│  Agora você entende o pipeline e pode usar em seus notebooks.              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                      SE VOCÊ TEM 30 MINUTOS                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Leia: src/MIGRATION_GUIDE.py (antes vs. depois)                        │
│  2. Inspecione: src/preprocessing.py (veja as funções)                     │
│  3. Inspecione: src/feature_engineering.py (entenda engenharia)            │
│  4. Inspecione: src/transformation.py (veja transformações)                │
│  5. Execute todos os 6 exemplos em src/examples.py                         │
│                                                                             │
│                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# =============================================================================
# MAPA DE ARQUIVOS
# =============================================================================

"""
DOCUMENTAÇÃO TEXTUAL (ler primeiro):
───────────────────────────────────

[1] REFATORACAO_RESUMO.txt
   ├─ Status: LEIA PRIMEIRO
    ├─ Tempo: 5 minutos
    └─ O quê: Resumo executivo de toda refatoração
       - Números e estatísticas
       - Estrutura final
       - Benefícios
       - Como usar

[2] src/README.md
   ├─ Status: ESSENCIAL
    ├─ Tempo: 10 minutos
    └─ O quê: Documentação estruturada do projeto
       - Estrutura KDD explicada
       - Cada módulo detalhado
       - Fluxo de dados
       - Próximos passos


CÓDIGO EXEMPLOS (execute depois):
──────────────────────────────────

[3] src/QUICKSTART.py
   ├─ Status: COMECE AQUI
    ├─ Tempo: 2 minutos (execução)
    └─ O quê: 5 cenários rápidos
       - Pipeline completo
       - Etapas individuais
       - Notebook Jupyter
       - sklearn integration
       - Verificações

[4] src/examples.py
   ├─ Status: EXPLORE
    ├─ Tempo: 15 minutos
    └─ O quê: 6 exemplos detalhados
       - Exemplo 1: Pipeline automático
       - Exemplo 2: Etapas individuais
       - Exemplo 3: Retomar intermediário
       - Exemplo 4: Exploração pós-pipeline
       - Exemplo 5: sklearn integration
       - Exemplo 6: Validação de lógica

[5] src/MIGRATION_GUIDE.py
   ├─ Status: COMPARE
    ├─ Tempo: 10 minutos
    └─ O quê: Antes vs. Depois
       - Estrutura antiga vs. nova
       - Localização de funções
       - Mudanças principais
       - Checklist de migração


CÓDIGO PRINCIPAL (navegar depois):
──────────────────────────────────

[6] src/config.py
   ├─ Status: CONSULTA
    ├─ Tempo: 5 minutos (ler)
    └─ O quê: Configurações centralizadas
       - Caminhos de arquivos
       - Mapas de recodificação
       - Constantes globais
       - Parâmetros

[7] src/selection.py
   ├─ Status: CONSULTA
    ├─ Tempo: 3 minutos (ler)
    └─ O quê: Seleção de features
       - VARIABLES_MAP
       - select_features()
       - ~80 linhas

[8] src/preprocessing.py
   ├─ Status: PRINCIPAL
    ├─ Tempo: 10 minutos (ler)
    └─ O quê: Limpeza e validação
       - 18 funções tratar_*
       - clean_pns_data() [orquestrador]
       - ~400 linhas
       - Maioria das operações

[9] src/feature_engineering.py
   ├─ Status: PRINCIPAL
    ├─ Tempo: 8 minutos (ler)
    └─ O quê: Engenharia de features
       - One-hot encoding
       - IMC
       - Ordinais
       - apply_feature_engineering() [orquestrador]
       - ~350 linhas

[10] src/transformation.py
   ├─ Status: PRINCIPAL
     ├─ Tempo: 3 minutos (ler)
     └─ O quê: Transformações estatísticas
        - Log de renda
        - Centralização
        - Polinômios
        - ~80 linhas

[11] src/pipeline.py
   ├─ Status: ORQUESTRADOR
     ├─ Tempo: 5 minutos (ler)
     └─ O quê: Coordenador principal
        - run_preprocessing_pipeline()
        - Suporta etapas parciais
        - Salvamento opcional
        - ~150 linhas

[12] src/evaluation.py
   ├─ Status: FUTURO
     └─ O quê: Placeholder para avaliação

[13] src/modeling.py
   ├─ Status: FUTURO
     └─ O quê: Placeholder para modelos


NOTEBOOK (atualizado):
─────────────────────

[14] notebooks/01_pre_processamento.ipynb
   ├─ Status: ATUALIZADO
     └─ O quê: Notebook reformulado
        - Agora importa e usa o pipeline
        - Mantém estrutura exploratória
        - Pode ser executado normalmente
"""

# =============================================================================
# FLUXO DE LEITURA RECOMENDADO
# =============================================================================

"""
ROTEIRO A) Para Usuários (rodar código):
──────────────────────────────────────────

1. (5 min)  REFATORACAO_RESUMO.txt
            → Entender O QUE foi feito

2. (2 min)  Execute: python src/QUICKSTART.py
            → Escolha opção 1
            → Pronto, tem dados processados

3. (5 min)  src/README.md - seção "Como Usar"
            → Aprender 3 formas de usar

4. (15 min) src/examples.py
            → Executar exemplos e ver resulados
            → python src/examples.py 1 (pipeline)
            → python src/examples.py 4 (exploração)

Tempo total: ~25 minutos para estar produtivo


ROTEIRO B) Para Desenvolvedores (entender código):
────────────────────────────────────────────────────

1. (5 min)  REFATORACAO_RESUMO.txt
            → Entender O QUE e POR QUE

2. (10 min) src/README.md
            → Documentação estruturada

3. (10 min) src/MIGRATION_GUIDE.py
            → Ver antes vs. depois

4. (5 min)  src/config.py
            → Entender configurações

5. (20 min) src/preprocessing.py
            → Leia cada função

6. (15 min) src/feature_engineering.py
            → Leia cada função

7. (5 min)  src/transformation.py
            → Leia cada função

8. (10 min) src/pipeline.py
            → Entenda orquestração

9. (30 min) src/examples.py
            → Execute todos os exemplos

Tempo total: ~85 minutos para dominar


ROTEIRO C) Para Estender/Manter (modificar código):
─────────────────────────────────────────────────────

[Faça roteiro B completo]

Depois:

10. (15 min) src/examples.py exemplo 6
             → Validar lógica mantida

11. (20 min) Testes unitários (crie seus)
             → Test cada método isoladamente

12. (Conforme necessário) Adicione código:
             → Nova função em módulo apropriado
             → Adicione ao "__init__.py"
             → Adicione ao pipeline orquestrador
             → Documente
             → Teste

Tempo total: >2 horas para estar confortável mantendo

"""

# =============================================================================
# 🔍 BUSCA RÁPIDA
# =============================================================================

"""
PROCURANDO POR...                       ARQUIVO
─────────────────────────────────────────────────────────────────────
Como usar pipeline?                     → src/QUICKSTART.py
Exemplos de código?                     → src/examples.py
Documentação?                           → src/README.md
Antes vs. Depois?                       → src/MIGRATION_GUIDE.py
Funções de limpeza?                     → src/preprocessing.py
Funções de engenharia?                  → src/feature_engineering.py
Log/centralização?                      → src/transformation.py
Configurações?                          → src/config.py
Seleção de features?                    → src/selection.py
Orquestrador?                           → src/pipeline.py
Importações?                            → src/__init__.py
Mapas e constantes?                     → src/config.py
Caminhos de arquivos?                   → src/config.py
Estrutura KDD explicada?                → src/README.md
Status do projeto?                      → REFATORACAO_RESUMO.txt
Validar lógica preservada?              → src/examples.py (ex 6)
Variáveis binárias?                     → src/preprocessing.py > tratar_sexo()
One-hot encoding?                       → src/feature_engineering.py > tratar_uf()
Cálculo IMC?                           → src/feature_engineering.py > tratar_altura_peso_imc()
Escolaridade ordinal?                   → src/feature_engineering.py > tratar_escolaridade()
Começar agora?                          → src/QUICKSTART.py
"""

# =============================================================================
# ⚡ ATALHOS ÚTEIS
# =============================================================================

"""
COMANDO                             RESULTADO
─────────────────────────────────────────────────────────────────────
cd src
python QUICKSTART.py                → Menu interativo para começar

python examples.py 1                → Pipeline completo

python examples.py 6                → Validar lógica preservada

python -c "from pipeline import    → Teste de import
run_preprocessing_pipeline"

ipython                             → Enter e explore:
>>> from pipeline import run_preprocessing_pipeline
>>> df = run_preprocessing_pipeline()
>>> df.info()

grep "def " preprocessing.py         → Ver todas as funções
"""

# =============================================================================
# 📊 ESTATÍSTICAS
# =============================================================================

"""
MÉTRICA                             VALOR
─────────────────────────────────────────────────────────────────────
Arquivos Python criados             9
Linhas de código novo              ~1500
Funções de limpeza preservadas     18
Funções de engenharia criadas      8
Novos exemplos                      6
Documentação                        ~2000 linhas
Status da lógica                   100% preservada
Data leakage prevention            Preparado para sklearn
Modularidade                       Máxima (7 módulos)
Reusabilidade                      Máxima (importar função)
"""

# =============================================================================
# CHECKLIST
# =============================================================================

"""
ANTES DE COMEÇAR:
  [ ] Tenho Python 3.7+
  [ ] Tenho pandas, numpy instalados
  [ ] Tenho dados brutos em data/raw/pns_2019.csv

PARA USAR O PIPELINE:
  [ ] Li REFATORACAO_RESUMO.txt
  [ ] Executei python src/QUICKSTART.py
  [ ] Escolhi uma opção de cenário
  [ ] Verifiquei que funcionou

PARA ENTENDER A ESTRUTURA:
  [ ] Li src/README.md
  [ ] Executei src/examples.py
  [ ] Inspecionei src/preprocessing.py
  [ ] Inspecionei src/feature_engineering.py
  [ ] Inspecionei src/transformation.py

PARA ESTENDER O CÓDIGO:
  [ ] Li src/MIGRATION_GUIDE.py
  [ ] Executei src/examples.py exemplo 6
  [ ] Entendi onde adicionar novo código
  [ ] Entendi como testar mudanças
"""

# =============================================================================
# TROUBLESHOOTING
# =============================================================================

"""
ERRO                                SOLUÇÃO
─────────────────────────────────────────────────────────────────────
ImportError: No module named 'src'  → sys.path.insert(0, '../src')
                                     ou execute de dentro de src/

ModuleNotFoundError: pipeline       → Certifique-se que está em notebooks/ 
                                     ou adicione src ao path

FileNotFoundError: pns_2019.csv     → Verifique que data/raw/ existe
                                     e tem o arquivo

AttributeError: 'DataFrame' has no  → Colunas esperadas não existem
attribute 'xxx'                      → Verifique shape de dados intermediários

Dados ausentes após pipeline?        → Normal! Alguns registros removidos
                                     → Use skip_to_stage para debugar

Resultado diferente do antigo?       → Execute exemplo 6 de examples.py
                                     → Valida se lógica foi preservada
"""

# =============================================================================

print(__doc__)

"""
═════════════════════════════════════════════════════════════════════════════

PRÓXIMA AÇÃO:

  1. Leia: REFATORACAO_RESUMO.txt (na raiz do projeto)
  2. Execute: python src/QUICKSTART.py
  3. Explore: src/examples.py

═════════════════════════════════════════════════════════════════════════════
"""
