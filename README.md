# Poder de Compra Imobiliária — Pipeline de Dados com ML e Visualização
Projeto prático • Python 3.10+ • Console

## Visão Geral
Aplicação de console que orquestra um pipeline completo para analisar o poder de compra no mercado imobiliário brasileiro. Coleta séries do INPC (IBGE/SIDRA) e de preços de imóveis (FipeZAP), faz limpeza e junção, gera visualizações exploratórias, treina um modelo simples de ML (regressão linear) e exporta um relatório com métricas.

Saídas principais (em data/):
- Gráficos: grafico_inpc.png, grafico_imoveis.png, grafico_relacao.png
- Métricas de ML: resultados.csv
- Dados brutos: inpc_raw.csv, imoveis_raw.csv

## Fontes de Dados
- INPC (mensal) via API IBGE/SIDRA (últimos 48 meses)
  - https://apisidra.ibge.gov.br
- FipeZAP (séries históricas em Excel)
  - https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
  - Aba utilizada: “Índice FipeZAP”

## Pipeline (scripts/)
1) coleta.py
   - Baixa:
     - INPC (API SIDRA): últimos 48 meses, salva em data/inpc_raw.csv
     - FipeZAP (Excel): aba “Índice FipeZAP”, salva em data/imoveis_raw.csv
   - Dependências: requests, pandas, openpyxl
2) limpeza.py
   - INPC: renomeia colunas D2N?mes e V?inpc; converte “inpc” para numérico.
   - Imóveis: seleciona colunas B e R da aba “Índice FipeZAP” e as renomeia para [mes, preco_medio].
   - Faz merge interno (inner) por “mes”.
   - Observação: se a coluna de mês na planilha estiver na coluna A, troque para A e R (ou ajuste no coleta/limpeza conforme necessário).
3) visualizacao.py
   - Gera gráficos: evolução do INPC, evolução do preço médio (R$/m²) e relação INPC x preço.
   - Salva em data/grafico_*.png.
4) modelos.py
   - Regressão linear simples (y=preco_medio, X=inpc) com train/test split.
   - Salva RMSE e R² em resultados.
5) relatorio.py
   - Exporta métricas para data/resultados.csv.

## Estrutura do projeto
- Poder de Compra Imobiliaria (aplicação console)
  - Program.py (orquestra: coletar ? limpar ? visualizar ? modelar ? relatar)
  - scripts/
    - coleta.py
    - limpeza.py
    - visualizacao.py
    - modelos.py
    - relatorio.py
  - data/ (gerada em runtime: CSVs brutos, gráficos e resultados.csv)

## Como executar

Pré?requisitos
- Python 3.10 ou superior
- pip
- Acesso à internet (para IBGE e FipeZAP)
- (Opcional) Visual Studio 2022 com workload de Python

Instalação
- Windows (PowerShell)
  - python -m venv .venv
  - .\.venv\Scripts\Activate
  - pip install -r "Poder de Compra Imobiliaria/requirements.txt"
  - (ou) pip install requests pandas seaborn matplotlib scikit-learn openpyxl
- macOS/Linux
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install -r "Poder de Compra Imobiliaria/requirements.txt"
  - (ou) pip install requests pandas seaborn matplotlib scikit-learn openpyxl

Visual Studio 2022
1. Abra a pasta “Poder de Compra Imobiliaria”.
2. No Solution Explorer, clique com o botão direito em Program.py e escolha __Set as Startup File__.
3. Selecione o interpretador em __Python Environments__.
4. Rode com __Start Debugging__ (F5) ou __Start Without Debugging__ (Ctrl+F5).

CLI
- Na raiz do repositório (após instalar as dependências):
  - python "Poder de Compra Imobiliaria/Program.py"

## Observações importantes
- Certifique-se de que a pasta “data/” exista antes de executar (o pipeline grava CSVs e gráficos lá).
- A aba e os nomes/posições das colunas do FipeZAP podem mudar ao longo do tempo.
  - Hoje o código aponta para a aba “Índice FipeZAP”.
  - Em limpeza.py, são usadas as colunas B e R (renomeadas para mes e preco_medio).
  - Se o mês estiver na coluna A, ajuste para A e R (ou use usecols="A,R" no pd.read_excel).
- As séries do FipeZAP representam preços médios anunciados em R$/m². Elas podem refletir médias móveis trimestrais (ver notas no rodapé da planilha).
- Reexecuções sobrescrevem arquivos em “data/”.
- Para eixos mais legíveis, considere converter “mes” para datetime no primeiro dia do mês.

## Tecnologias
- Python, pandas, seaborn, matplotlib
- scikit-learn (LinearRegression e métricas)
- requests, openpyxl (leitura de Excel)

## Licença
Uso acadêmico/demonstrativo. Ajuste conforme a necessidade do repositório.