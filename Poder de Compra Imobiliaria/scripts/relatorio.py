# salvar gr�ficos / outputs
import pandas as pd



def gerar_relatorio(df, resultados):
    # Salvar m�tricas em CSV
    resultados_df = pd.DataFrame([resultados])
    resultados_df.to_csv("data/resultados.csv", index=False)
    print(" Relat�rio gerado em data/resultados.csv")
