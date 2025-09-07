# seaborn / matploitlib
import seaborn as sns
import matplotlib.pyplot as plt



def plotar_graficos(df):
    # Evolu��o do INPC
    plt.figure(figsize=(10,5))
    sns.lineplot(x="mes", y="inpc", data=df)
    plt.title("Evolu��o do INPC")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/grafico_inpc.png")
    plt.close()

    # Evolu��o do pre�o m�dio de im�veis
    plt.figure(figsize=(10,5))
    sns.lineplot(x="mes", y="preco_medio", data=df)
    plt.title("Evolu��o do Pre�o M�dio de Im�veis (Brasil)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/grafico_imoveis.png")
    plt.close()

    # Rela��o INPC x Pre�o m�dio
    plt.figure(figsize=(6,6))
    sns.scatterplot(x="inpc", y="preco_medio", data=df)
    plt.title("Rela��o INPC x Pre�o M�dio de Im�veis")
    plt.tight_layout()
    plt.savefig("data/grafico_relacao.png")
    plt.close()

    print(" Gr�ficos salvos.")