# requests para puxar os dados (INPC + imóveis)
# api INPC variação salarial: https://apisidra.ibge.gov.br
# tabelas da SIDRA IBGE: https://sidra.ibge.gov.br/home/inpc
# link fixo de download da tabela atualizada de preço médio de imóveis: https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
import requests
import pandas as pd
from io import BytesIO



def baixar_dados():
    # --- INPC via API IBGE (SIDRA) ---
    urlInpc = "https://apisidra.ibge.gov.br/values/t/7063/n1/1/p/last48/v/44/h/y/f/n/d/2"  # INPC mensal
    respostaInpc = requests.get(urlInpc)
    dfInpc = pd.DataFrame(respostaInpc.json())
    print(" INPC carregado da API IBGE.")

    # --- Preço médio de imóveis via FipeZAP (Excel) ---
    urlFipe = "https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx"
    respostaFipe = requests.get(urlFipe)
    dfPrecoImoveis = pd.read_excel(BytesIO(respostaFipe.content), sheet_name="Índice FipeZAP")
    print(" Preços de imóveis carregados do FipeZAP.")

    # Salvar arquivos crus na pasta data
    dfInpc.to_csv("data/inpc_raw.csv", index=False)
    dfPrecoImoveis.to_csv("data/imoveis_raw.csv", index=False)

    return dfInpc, dfPrecoImoveis



