Os microdados da PNS foram processados inicialmente no ambiente SAS OnDemand for Academics, por meio da execução dos scripts oficiais disponibilizados pelo IBGE, garantindo fidelidade ao layout original dos dados.

## SAS
O SAS (Statistical Analysis System) é uma plataforma de software amplamente utilizada para análise estatística, gerenciamento e processamento de grandes volumes de dados, sendo especialmente difundida em pesquisas nas áreas de saúde pública, epidemiologia e ciências sociais. A ferramenta permite a leitura, transformação, validação e análise de dados estruturados e semiestruturados, oferecendo mecanismos robustos para controle de qualidade e rastreabilidade dos processos analíticos.

## Arquivo .sas
Arquivos com extensão .sas correspondem a scripts escritos na linguagem SAS, os quais descrevem instruções para manipulação e análise de dados. No contexto dos microdados disponibilizados pelo IBGE, esses arquivos não representam os dados em si, mas sim a especificação formal do layout dos arquivos de dados em formato texto, definindo a posição, o tipo e o significado de cada variável.

## Relação entre SAS e Txt
Nos conjuntos de microdados da Pesquisa Nacional de Saúde (PNS), os dados são disponibilizados em arquivos texto de largura fixa (.txt), acompanhados de scripts em linguagem SAS (.sas). Esses scripts descrevem precisamente como os arquivos texto devem ser lidos, indicando a posição inicial, o tamanho e o tipo de cada variável, além de rótulos e formatos categóricos. Dessa forma, o arquivo .sas funciona como um dicionário de dados executável, garantindo a correta interpretação dos microdados.

## Transformação em .csv
O processamento inicial dos microdados da PNS foi realizado no ambiente SAS Studio for Academics, por meio da execução dos scripts oficiais em linguagem SAS disponibilizados pelo IBGE. Os arquivos texto foram lidos conforme o layout definido no script, resultando na criação de um conjunto de dados estruturado, posteriormente exportado para o formato CSV para viabilizar as análises em ambiente Python.

## Seleção das variaveis e renomeação
A interpretação das variáveis foi realizada com base no dicionário oficial da PNS, garantindo a correta identificação dos códigos e categorias associados a cada pergunta do questionário.

## Inspeção dos dados
A inspeção inicial dos microdados da PNS 2019 revelou a estrutura hierárquica do plano amostral do IBGE. Observou-se que, enquanto as variáveis sociodemográficas abrangem a totalidade dos domicílios, as variáveis de condições crônicas e estilos de vida restringem-se ao morador selecionado para a entrevista individual, delimitando a base analítica para aproximadamente 90.846 instâncias. A alta taxa de valores ausentes em variáveis específicas, como enfisema e bronquite, orientou a decisão metodológica de priorizar DCNTs com maior densidade de dados, como hipertensão e diabetes, garantindo a robustez estatística necessária para a etapa de mineração.

---

# Pré-processamento

### Unidade Federativa
A variável Unidade da Federação foi convertida para as respectivas siglas oficiais do IBGE (ex.: SP, BA, TO) e posteriormente submetida à técnica de One-Hot Encoding com remoção da categoria de referência (drop_first=True), a fim de evitar multicolinearidade nos modelos lineares penalizados. Essa estratégia permite capturar heterogeneidades regionais relevantes para a análise dos Determinantes Sociais da Saúde (DSS), mantendo interpretabilidade nos coeficientes da regressão LASSO e nas métricas de importância de atributos do Random Forest.

### Situação Censitária
4.2.2. Codificação da Situação Censitária: A variável tipo de situação censitária (V0026) foi convertida para um formato binário, no qual o valor 1 representa o contexto urbano e o valor 0 representa o contexto rural. Esta simplificação fundamenta-se na natureza dicotômica da variável na base da PNS 2019 e visa facilitar a análise comparativa entre os diferentes ambientes de moradia, considerados determinantes intermediários no processo de adoecimento por doenças crônicas.

### Tipo domicilio
A variável A001 (Tipo de Domicílio), de natureza categórica nominal, teve seus códigos convertidos em rótulos descritivos (Casa, Apartamento, Cortiço e Ignorado) e foi submetida a One-Hot Encoding com remoção da categoria de referência. Essa abordagem preserva a ausência de hierarquia entre as categorias, evita multicolinearidade em modelos lineares penalizados e permite análise individual da contribuição de cada tipo de moradia na predição dos desfechos.

### Infraestrutura Domiciliar (Água encanada e Internet)
A variável A00601 (forma de acesso à água) foi codificada de forma ordinal, refletindo o gradiente de qualidade da infraestrutura hídrica (canalizada em cômodo, canalizada no terreno e não canalizada). Essa estratégia preserva a hierarquia implícita da variável e reduz dimensionalidade, favorecendo estabilidade nos modelos lineares penalizados. A variável A01901 (acesso à internet no domicílio), por apresentar estrutura dicotômica, foi convertida em variável binária. As escolhas metodológicas visam manter coerência conceitual com determinantes estruturais da saúde e garantir interpretabilidade dos parâmetros estimados.

### Sexo
A variável sexo (C006) foi convertida em variável binária indicadora (‘sexo_feminino’), assumindo valor 1 para mulheres e 0 para homens. Essa transformação permite incorporação direta nos modelos de regressão regularizada (LASSO) e nos modelos baseados em árvores, assegurando interpretação clara do efeito associado ao sexo na predição das doenças crônicas analisadas.

### Idade
Idade

A variável C008 (Idade), mensurada em anos completos (0–130), foi mantida como variável contínua e restrita à população adulta (≥18 anos), em consonância com o foco analítico nas doenças crônicas. Registros com valores inconsistentes fora do intervalo válido foram excluídos para assegurar qualidade e consistência epidemiológica dos dados.

Considerando que a idade constitui o principal determinante biológico das doenças crônicas e poderia exercer influência dominante na modelagem preditiva, adotaram-se procedimentos metodológicos para garantir estabilidade e equilíbrio analítico. Inicialmente, a variável foi centralizada em torno de sua média amostral, reduzindo colinearidade estrutural com termos polinomiais. Em seguida, foi criado um termo quadrático centralizado (idade²), permitindo capturar possíveis relações não lineares entre envelhecimento e risco de adoecimento.

Essa estratégia evita categorizações arbitrárias, preserva poder estatístico e torna a modelagem linear penalizada (LASSO) mais comparável aos modelos baseados em árvores (Random Forest), que naturalmente capturam não linearidades.

Adicionalmente, a padronização das variáveis será realizada no pipeline de modelagem para assegurar penalização adequada no LASSO, prevenindo distorções decorrentes de diferenças de escala entre preditores.

Essa abordagem permite controlar adequadamente o efeito da idade sem inflar artificialmente sua influência, assegurando avaliação mais precisa da contribuição incremental dos Determinantes Sociais da Saúde no desempenho preditivo dos modelos.

### Raça/Cor
A variável C009 (Raça/Cor), de natureza categórica nominal, teve seus códigos convertidos em rótulos descritivos (Branca, Preta, Amarela, Parda, Indígena e Ignorado) e foi submetida à técnica de One-Hot Encoding com remoção da categoria de referência (drop_first=True).

A estratégia preserva a ausência de hierarquia entre as categorias e evita multicolinearidade nos modelos lineares penalizados (LASSO), mantendo estabilidade e interpretabilidade dos coeficientes.

Epidemiologicamente, raça/cor é considerada Determinante Social Estrutural da Saúde, refletindo desigualdades históricas associadas ao acesso a recursos, condições socioeconômicas e prevalência de doenças crônicas.

Nos modelos Random Forest, a codificação em variáveis indicadoras permite mensurar a importância relativa de cada categoria na predição dos desfechos. Recomenda-se avaliar possível colinearidade com renda e escolaridade.

### Alfabetização

A variável D001 (Sabe ler e escrever), de natureza categórica binária nominal, foi convertida para formato dicotômico, assumindo valor 1 para indivíduos alfabetizados e 0 para não alfabetizados. Registros classificados como “Ignorado” foram tratados como valores ausentes.

A alfabetização constitui indicador fundamental de capital educacional mínimo, representando um Determinante Social Estrutural da Saúde associado ao acesso à informação, inserção no mercado de trabalho e utilização de serviços de saúde.

Considerando a possível sobreposição conceitual com a variável escolaridade, recomenda-se avaliação de colinearidade durante a modelagem, a fim de evitar redundância e instabilidade na seleção de preditores no modelo LASSO. Nos modelos Random Forest, sua inclusão permite mensurar o impacto específico do analfabetismo absoluto na predição dos desfechos.



### Escolaridade

A variável D00901 (nível educacional mais elevado frequentado), de natureza ordinal, apresentou registros ausentes para indivíduos analfabetos, uma vez que, na estrutura da PNS 2019, a escolaridade é classificada como “não aplicável” quando o indivíduo declara não saber ler e escrever.

Para garantir consistência conceitual e evitar perda de informação, a variável alfabetização (D001) foi incorporada à construção da variável educacional, criando-se explicitamente a categoria “Analfabeto”.

Os níveis educacionais foram posteriormente agrupados em uma escala ordinal hierárquica, refletindo o gradiente educacional brasileiro: analfabetismo, ensino fundamental, ensino médio, ensino superior e pós-graduação.

Essa estratégia reduz dimensionalidade, preserva a hierarquia implícita da variável e evita redundância estrutural entre alfabetização e escolaridade. Nos modelos LASSO, a codificação ordinal favorece interpretabilidade do gradiente educacional, enquanto no Random Forest permite identificação de limiares não lineares associados ao risco de doenças crônicas.

A decisão metodológica assegura maior estabilidade estatística, coerência epidemiológica e redução de multicolinearidade no conjunto de preditores sociais.

### Plano de Saúde

A variável I00102 (posse de plano de saúde médico particular, empresarial ou público), de natureza categórica binária nominal, foi convertida para formato dicotômico, assumindo valor 1 para indivíduos que relataram possuir plano de saúde e 0 para aqueles que não possuem.

Não foram identificados registros classificados como “Ignorado” na amostra analisada.

A posse de plano de saúde constitui determinante intermediário relacionado ao acesso a serviços de saúde e reflete desigualdades socioeconômicas estruturais, sendo incluída no modelo ampliado com Determinantes Sociais da Saúde.

### Renda Domiciliar

A variável VDF002 (rendimento domiciliar mensal, em reais), de natureza contínua, apresentou distribuição fortemente assimétrica à direita, característica comum a variáveis de renda.

Para reduzir a influência de valores extremos e melhorar estabilidade estatística, foi aplicada winsorização no percentil 99, limitando valores acima desse ponto ao respectivo limiar superior. Em seguida, realizou-se transformação logarítmica (log1p), preservando valores iguais a zero.

Essa estratégia reduz assimetria, minimiza o impacto de outliers e aproxima a relação entre renda e desfechos crônicos de uma estrutura linear, favorecendo desempenho do modelo LASSO. Nos modelos Random Forest, a transformação também contribui para maior estabilidade nos critérios de divisão das

### Renda Domiciliar Per Capita

A variável VDF003 (rendimento domiciliar per capita mensal, em reais), de natureza contínua, apresentou distribuição assimétrica à direita, com presença de valores extremos.

Para mitigar a influência de outliers e melhorar a estabilidade dos modelos preditivos, foi aplicada winsorização no percentil 99, limitando valores superiores ao respectivo limiar. Posteriormente, utilizou-se transformação logarítmica (log1p), preservando valores iguais a zero.

Essa abordagem reduz assimetria, aproxima a relação entre renda e desfechos de uma estrutura linear e melhora desempenho do modelo LASSO, ao mesmo tempo em que mantém coerência analítica no Random Forest. A padronização final será realizada no pipeline de modelagem.

### Decisão das rendas 
Optou-se por utilizar apenas a renda domiciliar per capita como indicador socioeconômico, por representar de forma mais precisa a disponibilidade individual de recursos financeiros. A renda domiciliar total pode mascarar desigualdades relacionadas ao tamanho do domicílio, reduzindo a capacidade discriminatória do indicador. A exclusão da renda domiciliar total também evita colinearidade estrutural entre preditores socioeconômicos.

### Altura, Peso e Índice de Massa Corporal (IMC)

As variáveis P00104 (peso em quilogramas) e P00404 (altura em centímetros) foram submetidas a procedimentos de validação para exclusão de valores biologicamente implausíveis em adultos, considerando pesos entre 30 e 250 kg e alturas entre 120 e 220 cm. Registros classificados como “Ignorado” na variável altura foram tratados como valores ausentes.

A altura foi convertida para metros e utilizada para o cálculo do Índice de Massa Corporal (IMC), definido como peso (kg) dividido pela altura (m) ao quadrado.

Optou-se por manter o IMC como variável contínua, evitando categorização baseada em pontos de corte clínicos, a fim de preservar poder estatístico e permitir modelagem mais precisa das associações com os desfechos.

Optou-se por remover a variável peso do conjunto final de preditores, uma vez que o IMC constitui função direta dessa medida, evitando redundância estrutural e instabilidade nos modelos lineares penalizados.

A variável altura foi mantida como preditor contínuo independente, permitindo avaliar sua possível contribuição adicional na predição de desfechos específicos, como distúrbios osteomusculares e doenças respiratórias. O IMC foi mantido como variável contínua, preservando poder estatístico e permitindo que tanto o LASSO quanto o Random Forest capturem associações lineares e não lineares com os desfechos analisados.

### Tratamento da Variável de Tabagismo

As variáveis P050 (tabagismo atual) e P052 (tabagismo passado) foram combinadas para construção de uma única variável representando o status tabágico do indivíduo.

Na estrutura do questionário da PNS 2019, a pergunta sobre tabagismo passado (P052) é aplicada apenas aos indivíduos que declararam não fumar atualmente (P050 = 3). Dessa forma, valores ausentes em P052 não representam dados faltantes, mas sim ausência estrutural decorrente do fluxo do questionário.

Para preservar a coerência epidemiológica da exposição ao tabaco, foi criada variável categórica com três níveis:

0 — Nunca fumou

1 — Ex-fumante

2 — Fumante atual

A classificação foi definida da seguinte forma:

Indivíduos que relataram fumar diariamente ou menos que diariamente foram classificados como fumantes atuais.

Indivíduos que não fumam atualmente, mas relataram já ter fumado no passado, foram classificados como ex-fumantes.

Indivíduos que nunca fumaram foram classificados como nunca fumantes.

Após a consolidação da variável, aplicou-se codificação do tipo One-Hot Encoding com remoção da categoria de referência (drop_first=True), adotando como referência o grupo “nunca fumou”.

Essa estratégia foi escolhida para:

Evitar suposição de relação linear ordinal entre categorias.

Permitir que o modelo estime separadamente o efeito de ex-fumantes e fumantes atuais.

Preservar maior flexibilidade preditiva, especialmente no modelo LASSO.

As variáveis originais foram removidas após a transformação

### Consumo de Álcool

As variáveis P027 (frequência de consumo de bebida alcoólica) e P02801 (número de dias por semana de consumo) foram combinadas para construção de variável única representando intensidade de consumo alcoólico.

Considerando o fluxo condicional do questionário da PNS 2019, a variável referente aos dias por semana é respondida apenas por indivíduos que relataram consumo alcoólico, de modo que valores ausentes são estruturais.

Foi construída variável ordinal com quatro níveis:

0 — Nunca bebe

1 — Consumo raro

2 — Consumo moderado (1–2 dias por semana)

3 — Consumo frequente (≥3 dias por semana)

A categorização buscou preservar progressão de intensidade de exposição ao álcool, evitando granularidade excessiva e reduzindo variabilidade irrelevante.

Para modelagem, aplicou-se codificação do tipo One-Hot Encoding com remoção da categoria de referência, evitando imposição de relação linear entre níveis de consumo.

As variáveis originais foram removidas após transformação.

### Atividade Física

As variáveis P034 (prática de exercício físico nos últimos três meses) e P035 (frequência semanal de prática) foram combinadas para construção de variável única representando intensidade de atividade física.

A variável referente à frequência semanal é respondida apenas por indivíduos que relataram prática de exercício, sendo valores ausentes considerados estruturais.

Foi construída variável ordinal com quatro níveis:

0 — Sedentário (não pratica ou menos de 1 vez por semana)

1 — Baixa frequência (1–2 dias por semana)

2 — Frequência moderada (3–4 dias por semana)

3 — Alta frequência (≥5 dias por semana)

A categorização buscou refletir progressão de exposição protetora à atividade física, reduzindo granularidade excessiva e ruído estatístico.

Para modelagem, aplicou-se codificação One-Hot com remoção da categoria de referência, evitando suposição de relação linear entre níveis de frequência.

As variáveis originais foram removidas após transformação.

### DCNTs sem Salto Lógico

As variáveis referentes aos diagnósticos médicos de hipertensão, diabetes, AVC, asma, artrite, DORT, depressão e insuficiência renal crônica foram tratadas de forma padronizada, considerando estrutura binária homogênea no questionário da PNS 2019.

Para cada variável foi adotada a seguinte codificação:

1 — Presença de diagnóstico médico (Sim)

0 — Ausência de diagnóstico médico (Não)

Valores correspondentes a “Ignorado” foram convertidos para valores ausentes (NaN)

Optou-se por manter valores ausentes na base principal, sendo a exclusão aplicada apenas no momento da modelagem específica de cada desfecho, evitando perda desnecessária de observações em análises subsequentes.

### Doença do Coração e Subtipos

A variável “doença do coração” foi tratada como desfecho binário principal, seguindo codificação padronizada (1 = presença de diagnóstico médico; 0 = ausência).

Os subtipos específicos (infarto, angina, insuficiência cardíaca e arritmia) são investigados apenas entre indivíduos que responderam afirmativamente à pergunta geral, configurando fluxo condicional no questionário da PNS 2019.

Valores ausentes nos subtipos foram interpretados como ausência estrutural decorrente desse fluxo. Para garantir coerência clínica e consistência estatística, adotou-se a seguinte regra:

Indivíduos com resposta negativa para doença cardíaca geral foram automaticamente classificados como 0 (ausência) nas variáveis específicas.

Dessa forma, todas as variáveis foram mantidas como desfechos binários independentes, permitindo flexibilidade na modelagem preditiva, seja para doença cardíaca geral ou para condições específicas.

### Doenças Pulmonares

A variável referente à presença de doença pulmonar crônica foi tratada como desfecho binário, considerando diagnóstico médico autorreferido.

Os diagnósticos específicos de enfisema pulmonar e bronquite crônica são investigados apenas entre indivíduos que responderam afirmativamente à pergunta geral, configurando fluxo condicional no questionário da PNS 2019.

Valores ausentes nos subtipos foram interpretados como ausência estrutural decorrente desse fluxo. Para garantir consistência clínica e evitar viés decorrente de ausência estrutural, adotou-se a seguinte regra:

Indivíduos com resposta negativa para doença pulmonar geral foram automaticamente classificados como 0 (ausência) nas variáveis específicas de enfisema e bronquite.

Dessa forma, todas as variáveis foram mantidas como desfechos binários independentes, permitindo flexibilidade na modelagem preditiva tanto para doença pulmonar geral quanto para condições específicas.


## Resumo pre processamento
3. Pré-processamento e Construção da Base Analítica
3.1 Base de dados original

A base utilizada corresponde à Pesquisa Nacional de Saúde (PNS 2019), composta por:

293.726 indivíduos

1.088 variáveis

Predominância de variáveis numéricas (1.079 float64; 9 int64)

Volume aproximado de 2,4 GB

A base bruta inclui informações sociodemográficas, condições de saúde autorreferidas, diagnósticos médicos, estilo de vida, renda, infraestrutura domiciliar e medidas antropométricas.

3.2 Seleção teórica de variáveis

A seleção inicial foi orientada pela literatura sobre:

Determinantes Sociais da Saúde (DSS)

Fatores de risco para Doenças Crônicas Não Transmissíveis (DCNT)

Modelos epidemiológicos de risco cardiovascular

Foram selecionadas variáveis representando:

Características sociodemográficas (sexo, idade, raça, escolaridade)

Condições socioeconômicas (renda, plano de saúde, acesso à internet)

Infraestrutura domiciliar

Estilo de vida (tabagismo, álcool, atividade física)

Diagnósticos médicos autorreferidos

Medidas antropométricas

Após essa etapa:

37 variáveis mantidas

293.726 indivíduos preservados

Essa redução dimensional visou minimizar ruído e aumentar interpretabilidade sem comprometer a fundamentação teórica.

3.3 Definição da população analítica

Variáveis clínicas da PNS são respondidas apenas pelo morador selecionado no domicílio. Assim, registros sem informação válida para o desfecho principal foram removidos.

Após filtragem por presença de informação válida para hipertensão:

Base reduzida para aproximadamente 88 mil indivíduos

Essa decisão garante consistência da população analisada e evita imputação indevida em variáveis estruturais de saúde.

3.4 Padronização de variáveis binárias

Variáveis de diagnóstico médico foram recodificadas para estrutura binária:

1 = presença do diagnóstico

0 = ausência

9 (ignorado) → NaN

Foram incluídas:

Hipertensão

Diabetes

AVC

Asma

Artrite

DORT

Depressão

Insuficiência renal

Doenças cardíacas

Doenças pulmonares

Essa padronização permite aplicação direta em modelos de classificação binária.

3.5 Tratamento de variáveis com salto lógico

Algumas variáveis apresentam estrutura hierárquica (gate question).

3.5.1 Doenças cardíacas

Estrutura:

Pergunta geral sobre doença cardíaca

Subtipos específicos:

Infarto

Angina

Insuficiência cardíaca

Arritmia

Procedimento adotado:

Indivíduos com resposta “não” na variável geral tiveram os subtipos imputados como 0.

Indivíduos com resposta “sim” mantiveram suas respostas específicas.

Casos ignorados mantidos como NaN.

Esse procedimento preserva coerência lógica e evita inconsistências estruturais.

3.5.2 Doenças pulmonares

Aplicou-se a mesma estratégia para:

Doença pulmonar crônica

Enfisema

Bronquite crônica

3.6 Construção da variável ordinal de escolaridade

A escolaridade foi operacionalizada como variável ordinal estruturada, incorporando alfabetização.

Procedimento:

Recodificação da variável “alfabetizado” para binária.

Construção da variável escolaridade_ord:

Nível	Código
Analfabeto	0
Ensino Fundamental	1
Ensino Médio	2
Ensino Superior	3
Pós-graduação	4

A escolaridade foi mantida como variável ordinal por refletir gradiente socioeconômico.

Registros com escolaridade ausente foram removidos, resultando em:

79.722 indivíduos finais

A perda amostral foi inferior a 10%, considerada estatisticamente aceitável e teoricamente justificável, dado o papel estrutural da variável na análise de DSS.

3.7 Transformações em variáveis contínuas
3.7.1 Renda

As variáveis:

renda_domiciliar

renda_per_capita

foram transformadas via logaritmo natural para:

Reduzir assimetria

Minimizar influência de valores extremos

Melhorar estabilidade numérica

3.7.2 Idade

Foram criadas:

idade centralizada (idade_c)

termo quadrático (idade_c2)

Objetivo:

Permitir modelagem de efeitos não lineares da idade sobre os desfechos, prática comum em regressões epidemiológicas.

3.8 Codificação categórica

Aplicou-se one-hot encoding para:

Unidade Federativa

Raça/cor

Tipo de domicílio

Tabagismo

Consumo de álcool

Atividade física

Essa estratégia evita imposição de ordem artificial e permite uso em modelos lineares e baseados em árvore.

3.9 Variáveis antropométricas

Peso e altura foram mantidos como contínuos.

Não foi realizada imputação de valores ausentes para evitar introdução de viés sistemático, considerando que tais medidas podem apresentar padrão de ausência não aleatória.

4. Base Final

Após todas as etapas de pré-processamento:

79.722 indivíduos

71 variáveis

42 variáveis booleanas

27 variáveis float

2 variáveis inteiras

Volume aproximado de 20,8 MB

Redução total:
Etapa	Registros	Variáveis
Base bruta	293.726	1.088
Pós seleção teórica	293.726	37
Pós filtragem clínica	~88.000	37
Base final modelável	79.722	71
5. Considerações metodológicas

O processo de pré-processamento foi guiado por:

Fundamentação epidemiológica

Coerência lógica das variáveis

Preservação de determinantes estruturais

Minimização de imputações arbitrárias

Preparação para modelagem supervisionada

A base final apresenta:

Amostra robusta e nacionalmente representativa

Estrutura adequada para modelagem binária e multinível

Integração de determinantes sociais, comportamentais e clínicos

Essa construção permite avaliar tanto:

Desfechos gerais (ex.: presença de doença cardíaca)

Subtipos específicos

Comparações entre diferentes condições crônicas