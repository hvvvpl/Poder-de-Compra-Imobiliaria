# Poder de Compra Imobili�ria � Pipeline de Dados com ML e Visualiza��o
Projeto pr�tico � Python 3.10+ � Console

## Vis�o Geral
Aplica��o de console que orquestra um pipeline completo para analisar o poder de compra no mercado imobili�rio brasileiro. Coleta s�ries do INPC (IBGE/SIDRA) e de pre�os de im�veis (FipeZAP), faz limpeza e jun��o, gera visualiza��es explorat�rias, treina um modelo simples de ML (regress�o linear) e exporta um relat�rio com m�tricas.

Sa�das principais (em data/):
- Gr�ficos: grafico_inpc.png, grafico_imoveis.png, grafico_relacao.png
- M�tricas de ML: resultados.csv
- Dados brutos: inpc_raw.csv, imoveis_raw.csv

## Fontes de Dados
- INPC (mensal) via API IBGE/SIDRA (�ltimos 48 meses)
  - https://apisidra.ibge.gov.br
- FipeZAP (s�ries hist�ricas em Excel)
  - https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
  - Aba utilizada: ��ndice FipeZAP�

## Pipeline (scripts/)
1) coleta.py
   - Baixa:
     - INPC (API SIDRA): �ltimos 48 meses, salva em data/inpc_raw.csv
     - FipeZAP (Excel): aba ��ndice FipeZAP�, salva em data/imoveis_raw.csv
   - Depend�ncias: requests, pandas, openpyxl
2) limpeza.py
   - INPC: renomeia colunas D2N?mes e V?inpc; converte �inpc� para num�rico.
   - Im�veis: seleciona colunas B e R da aba ��ndice FipeZAP� e as renomeia para [mes, preco_medio].
   - Faz merge interno (inner) por �mes�.
   - Observa��o: se a coluna de m�s na planilha estiver na coluna A, troque para A e R (ou ajuste no coleta/limpeza conforme necess�rio).
3) visualizacao.py
   - Gera gr�ficos: evolu��o do INPC, evolu��o do pre�o m�dio (R$/m�) e rela��o INPC x pre�o.
   - Salva em data/grafico_*.png.
4) modelos.py
   - Regress�o linear simples (y=preco_medio, X=inpc) com train/test split.
   - Salva RMSE e R� em resultados.
5) relatorio.py
   - Exporta m�tricas para data/resultados.csv.

## Estrutura do projeto
- Poder de Compra Imobiliaria (aplica��o console)
  - Program.py (orquestra: coletar ? limpar ? visualizar ? modelar ? relatar)
  - scripts/
    - coleta.py
    - limpeza.py
    - visualizacao.py
    - modelos.py
    - relatorio.py
  - data/ (gerada em runtime: CSVs brutos, gr�ficos e resultados.csv)

## Como executar

Pr�?requisitos
- Python 3.10 ou superior
- pip
- Acesso � internet (para IBGE e FipeZAP)
- (Opcional) Visual Studio 2022 com workload de Python

Instala��o
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
1. Abra a pasta �Poder de Compra Imobiliaria�.
2. No Solution Explorer, clique com o bot�o direito em Program.py e escolha __Set as Startup File__.
3. Selecione o interpretador em __Python Environments__.
4. Rode com __Start Debugging__ (F5) ou __Start Without Debugging__ (Ctrl+F5).

CLI
- Na raiz do reposit�rio (ap�s instalar as depend�ncias):
  - python "Poder de Compra Imobiliaria/Program.py"

## Observa��es importantes
- Certifique-se de que a pasta �data/� exista antes de executar (o pipeline grava CSVs e gr�ficos l�).
- A aba e os nomes/posi��es das colunas do FipeZAP podem mudar ao longo do tempo.
  - Hoje o c�digo aponta para a aba ��ndice FipeZAP�.
  - Em limpeza.py, s�o usadas as colunas B e R (renomeadas para mes e preco_medio).
  - Se o m�s estiver na coluna A, ajuste para A e R (ou use usecols="A,R" no pd.read_excel).
- As s�ries do FipeZAP representam pre�os m�dios anunciados em R$/m�. Elas podem refletir m�dias m�veis trimestrais (ver notas no rodap� da planilha).
- Reexecu��es sobrescrevem arquivos em �data/�.
- Para eixos mais leg�veis, considere converter �mes� para datetime no primeiro dia do m�s.

## Tecnologias
- Python, pandas, seaborn, matplotlib
- scikit-learn (LinearRegression e m�tricas)
- requests, openpyxl (leitura de Excel)

## Licen�a
Uso acad�mico/demonstrativo. Ajuste conforme a necessidade do reposit�rio.