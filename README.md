# Poder de Compra Imobili�ria � Pipeline de Dados com ML e Visualiza��o
Projeto pr�tico � Python 3.10+ � Console

## Vis�o Geral
Aplica��o de console que orquestra um pipeline completo para analisar o poder de compra no mercado imobili�rio brasileiro. Coleta s�ries do INPC (IBGE/SIDRA) e de pre�os de im�veis (FipeZAP), faz limpeza e jun��o, gera visualiza��es explorat�rias, treina um modelo simples de ML (regress�o linear) e exporta um relat�rio com m�tricas.

![INPC](data/grafico_inpc.png)
![Pre�os de Im�veis](data/grafico_imoveis.png)
![INPC vs Pre�os](data/grafico_relacao.png)

## Funcionalidades
- Coleta de dados
  - INPC mensal via API IBGE/SIDRA.
  - S�rie hist�rica de pre�os de im�veis (Brasil) via FipeZAP (Excel).
  - Persist�ncia dos brutos em CSV: data/inpc_raw.csv e data/imoveis_raw.csv.

- Limpeza e pr�-processamento
  - Padroniza��o de colunas e coer��o num�rica.
  - Sele��o de colunas relevantes.
  - Jun��o interna por m�s (�mes�) para alinhar INPC e pre�os.

- Visualiza��o explorat�ria
  - Evolu��o do INPC (linha).
  - Evolu��o do pre�o m�dio de im�veis (linha).
  - Rela��o INPC x pre�o m�dio (dispers�o).
  - PNGs salvos em data/grafico_*.png.

- Machine Learning
  - Regress�o linear para prever pre�o a partir do INPC.
  - Train/test split e m�tricas (RMSE, R�).

- Relat�rios
  - Salva m�tricas do modelo em data/resultados.csv.

## Estrutura do projeto
- Poder de Compra Imobiliaria (aplica��o console)
  - Program.py (orquestra: coletar ? limpar ? visualizar ? modelar ? relatar)
  - scripts/
    - coleta.py (baixar_dados: INPC via SIDRA + FipeZAP; salva CSVs brutos)
    - limpeza.py (preprocessar: limpeza e merge por �mes�)
    - visualizacao.py (plotar_graficos: linhas e dispers�o em PNG)
    - modelos.py (treinar_modelos: LinearRegression, RMSE e R�)
    - relatorio.py (gerar_relatorio: exporta m�tricas em CSV)
  - data/ (gerada em runtime: CSVs brutos, gr�ficos e resultados.csv)

## Como executar
Pr�-requisitos
- Python 3.10 ou superior
- pip
- Acesso � internet (para IBGE e FipeZAP)
- (Opcional) Visual Studio 2022 com workload de Python

Instala��o
- Windows (PowerShell)
  - python -m venv .venv
  - .\.venv\Scripts\Activate
  - pip install requests pandas seaborn matplotlib scikit-learn openpyxl
- macOS/Linux
  - python3 -m venv .venv
  - source .venv/bin/activate
  - pip install requests pandas seaborn matplotlib scikit-learn openpyxl

Visual Studio 2022
1. Abra a pasta �Poder de Compra Imobiliaria�.
2. No Solution Explorer, clique com o bot�o direito em Program.py e escolha __Set as Startup File__.
3. Selecione o interpretador em __Python Environments__.
4. Rode com __Start Debugging__ (F5) ou __Start Without Debugging__ (Ctrl+F5).

CLI
- Na raiz do reposit�rio (ap�s instalar as depend�ncias):
  - python "Poder de Compra Imobiliaria/Program.py"

## Observa��es de uso
- Certifique-se de que a pasta �data/� exista antes de executar (o pipeline grava CSVs e gr�ficos l�).
- Endpoints externos:
  - IBGE/SIDRA INPC: https://api.sidra.ibge.gov.br
  - FipeZAP (Excel): https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
- Reexecu��es sobrescrevem arquivos em �data/�.
- Os r�tulos de �mes� v�m das fontes; para eixos mais leg�veis, considere converter para datetime.

## Tecnologias
- Python, pandas, seaborn, matplotlib
- scikit-learn (LinearRegression e m�tricas)
- requests, openpyxl (leitura de Excel)

## Licen�a
Uso acad�mico/demonstrativo. Ajuste conforme a necessidade do reposit�rio.