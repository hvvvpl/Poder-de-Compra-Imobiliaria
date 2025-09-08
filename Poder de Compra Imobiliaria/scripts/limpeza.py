# pandas / numpy para pré-processamento
import pandas as pd



def preprocessar(df_inpc, df_imoveis):
    # --- Tratamento INPC ---
    df_inpc = df_inpc.rename(columns={"D2N":"mes", "V":"inpc"})
    df_inpc["inpc"] = pd.to_numeric(df_inpc["inpc"], errors="coerce")
    df_inpc["mes"] = pd.to_datetime(df_inpc["mes"], dayfirst=True, errors="coerce")
    df_inpc["mes"] = df_inpc["mes"].dt.to_period("M").dt.to_timestamp()
    df_inpc = df_inpc.dropna(subset=["mes", "inpc"])

    # --- Tratamento Imóveis ---
    df_imoveis = df_imoveis.iloc[:, [0, 17]].copy()
    df_imoveis.columns = ["mes", "preco_medio"]
    df_imoveis["mes"] = pd.to_datetime(df_imoveis["mes"], format="%b-%y", errors="coerce")
    df_imoveis["mes"] = df_imoveis["mes"].dt.to_period("M").dt.to_timestamp()
    df_imoveis["preco_medio"] = pd.to_numeric(df_imoveis["preco_medio"], errors="coerce")
    df_imoveis = df_imoveis.dropna(subset=["mes", "preco_medio"])

    # --- Merge dos dois datasets ---
    df = (
        pd.merge(df_inpc, df_imoveis, on="mes", how="inner")
        .sort_values("mes")
        .reset_index(drop=True)
        )

    print(" Dados limpos e mesclados.")
    return df
