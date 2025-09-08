# pandas / numpy para pré-processamento
import pandas as pd



def preprocessar(df_inpc, df_imoveis):
    # --- Tratamento INPC ---
    df_inpc = df_inpc.rename(columns={"D2N":"mes", "V":"inpc"})
    df_inpc["inpc"] = pd.to_numeric(df_inpc["inpc"], errors="coerce")

    # --- Tratamento Imóveis ---
    df_imoveis = df_imoveis.iloc[:, [1, 17]].copy()
    df_imoveis.columns = ["mes", "preco_medio"]

    # --- Merge dos dois datasets ---
    df = pd.merge(df_inpc, df_imoveis, on="mes", how="inner")

    print(" Dados limpos e mesclados.")
    return df
