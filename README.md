# Poder de Compra Imobiliária – Pipeline de Dados com ML e Visualização
Projeto prático – Python 3.10+ – Console

## Visão Geral
Aplicação de console que orquestra um pipeline completo para analisar o poder de compra no mercado imobiliário brasileiro. Coleta séries do INPC (IBGE/SIDRA) e de preços de imóveis (FipeZAP), faz limpeza e junção, gera visualizações exploratórias, treina um modelo simples de ML (regressão linear) e exporta um relatório com métricas.

![INPC](data/grafico_inpc.png)
![Preços de Imóveis](data/grafico_imoveis.png)
![INPC vs Preços](data/grafico_relacao.png)

## Funcionalidades
- Coleta de dados
  - INPC mensal via API IBGE/SIDRA.
  - Série histórica de preços de imóveis (Brasil) via FipeZAP (Excel).
  - Persistência dos brutos em CSV: data/inpc_raw.csv e data/imoveis_raw.csv.

- Limpeza e pré-processamento
  - Padronização de colunas e coerção numérica.
  - Seleção de colunas relevantes.
  - Junção interna por mês (“mes”) para alinhar INPC e preços.

- Visualização exploratória
  - Evolução do INPC (linha).
  - Evolução do preço médio de imóveis (linha).
  - Relação INPC x preço médio (dispersão).
  - PNGs salvos em data/grafico_*.png.

- Machine Learning
  - Regressão linear para prever preço a partir do INPC.
  - Train/test split e métricas (RMSE, R²).

- Relatórios
  - Salva métricas do modelo em data/resultados.csv.

## Estrutura do projeto
- Poder de Compra Imobiliaria (aplicação console)
  - Program.py (orquestra: coletar ? limpar ? visualizar ? modelar ? relatar)
  - scripts/
    - coleta.py (baixar_dados: INPC via SIDRA + FipeZAP; salva CSVs brutos)
    - limpeza.py (preprocessar: limpeza e merge por “mes”)
    - visualizacao.py (plotar_graficos: linhas e dispersão em PNG)
    - modelos.py (treinar_modelos: LinearRegression, RMSE e R²)
    - relatorio.py (gerar_relatorio: exporta métricas em CSV)
  - data/ (gerada em runtime: CSVs brutos, gráficos e resultados.csv)

## Como executar
Pré-requisitos
- Python 3.10 ou superior
- pip
- Acesso à internet (para IBGE e FipeZAP)
- (Opcional) Visual Studio 2022 com workload de Python

Instalação
- Windows (PowerShell)
  - python -m venv .venv
  - .\.venv\Scripts\Activate
  - pip install requests pandas seaborn matplotlib scikit-learn openpyxl
- macOS/Linux
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install requests pandas seaborn matplotlib scikit-learn openpyxl

Visual Studio 2022
1. Abra a pasta “Poder de Compra Imobiliaria”.
2. No Solution Explorer, clique com o botão direito em Program.py e escolha __Set as Startup File__.
3. Selecione o interpretador em __Python Environments__.
4. Rode com __Start Debugging__ (F5) ou __Start Without Debugging__ (Ctrl+F5).

CLI
- Na raiz do repositório (após instalar as dependências):
  - python "Poder de Compra Imobiliaria/Program.py"

## Observações de uso
- Certifique-se de que a pasta “data/” exista antes de executar (o pipeline grava CSVs e gráficos lá).
- Endpoints externos:
  - IBGE/SIDRA INPC: https://api.sidra.ibge.gov.br
  - FipeZAP (Excel): https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
- Reexecuções sobrescrevem arquivos em “data/”.
- Os rótulos de “mes” vêm das fontes; para eixos mais legíveis, considere converter para datetime.

## Tecnologias
- Python, pandas, seaborn, matplotlib
- scikit-learn (LinearRegression e métricas)
- requests, openpyxl (leitura de Excel)

## Licença
Uso acadêmico/demonstrativo. Ajuste conforme a necessidade do repositório.