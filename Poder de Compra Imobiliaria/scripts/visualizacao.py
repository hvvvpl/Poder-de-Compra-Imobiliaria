# seaborn / matploitlib
import seaborn as sns
import matplotlib.pyplot as plt



def plotar_graficos(df):
    # Evolução do INPC
    plt.figure(figsize=(10,5))
    sns.lineplot(x="mes", y="inpc", data=df)
    plt.title("Evolução do INPC")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/grafico_inpc.png")
    plt.close()

    # Evolução do preço médio de imóveis
    plt.figure(figsize=(10,5))
    sns.lineplot(x="mes", y="preco_medio", data=df)
    plt.title("Evolução do Preço Médio de Imóveis (Brasil)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/grafico_imoveis.png")
    plt.close()

    # Relação INPC x Preço médio
    plt.figure(figsize=(6,6))
    sns.scatterplot(x="inpc", y="preco_medio", data=df)
    plt.title("Relação INPC x Preço Médio de Imóveis")
    plt.tight_layout()
    plt.savefig("data/grafico_relacao.png")
    plt.close()

    print(" Gráficos salvos.")
