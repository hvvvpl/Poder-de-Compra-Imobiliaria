# pandas / numpy para pré-processamento
import pandas as pd



def preprocessar(df_inpc, df_imoveis):
    # --- Tratamento INPC ---
    df_inpc = df_inpc.rename(columns={"D2N":"mes", "V":"inpc"})
    df_inpc["inpc"] = pd.to_numeric(df_inpc["inpc"], errors="coerce")
    df_inpc = df_inpc.dropna(subset=["inpc"])

    # --- Tratamento Imóveis ---
    df_imoveis = df_imoveis.rename(columns={"Período":"mes", "Brasil":"preco_medio"})
    df_imoveis = df_imoveis[["mes","preco_medio"]].dropna()

    # --- Merge dos dois datasets ---
    df = pd.merge(df_inpc, df_imoveis, on="mes", how="inner")

    print(" Dados limpos e mesclados.")
    return df