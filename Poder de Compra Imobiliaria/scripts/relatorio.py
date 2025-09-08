# salvar gráficos / outputs
import pandas as pd



def gerar_relatorio(df, resultados):
    # Salvar métricas em CSV
    resultados_df = pd.DataFrame([resultados])
    resultados_df.to_csv("data/resultados.csv", index=False)
    print(" Relatório gerado em data/resultados.csv")

