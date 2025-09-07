# requests para puxar os dados (INPC + im�veis)
# api INPC varia��o salarial: https://apisidra.ibge.gov.br
# link fixo de download da tabela atualizada de pre�o m�dio de im�veis: https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx
import requests
import pandas as pd
from io import BytesIO



def baixar_dados():
    # --- INPC via API IBGE (SIDRA) ---
    url_inpc = "https://api.sidra.ibge.gov.br/values/t/7060/n1/all/v/44/p/all/d/v44%202"  # INPC mensal
    resp_inpc = requests.get(url_inpc)
    df_inpc = pd.DataFrame(resp_inpc.json())
    print(" INPC carregado da API IBGE.")

    # --- Pre�o m�dio de im�veis via FipeZAP (Excel) ---
    url_fipe = "https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx"
    resp_fipe = requests.get(url_fipe)
    df_imoveis = pd.read_excel(BytesIO(resp_fipe.content), sheet_name="Venda - Brasil")
    print(" Pre�os de im�veis carregados do FipeZAP.")

    # Salvar arquivos crus na pasta data
    df_inpc.to_csv("data/inpc_raw.csv", index=False)
    df_imoveis.to_csv("data/imoveis_raw.csv", index=False)

    return df_inpc, df_imoveis


