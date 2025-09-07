#pipeline principal
import scripts.coleta as coleta
import scripts.limpeza as limpeza
import scripts.modelos as modelos
import scripts.relatorio as relatorio
import scripts.visualizacao as visualizacao



def main():
    # 1. Coleta de dados
    df_inpc, df_imoveis = coleta.baixar_dados()

    # 2. Limpeza e pr�-processamento
    df = limpeza.preprocessar(df_inpc, df_imoveis)

    # 3. Visualiza��o explorat�ria
    visualizacao.plotar_graficos(df)

    # 4. Machine Learning (regress�o, classifica��o, clustering)
    resultados = modelos.treinar_modelos(df)

    # 5. Relat�rio final (gr�ficos + m�tricas)
    relatorio.gerar_relatorio(df, resultados)

    print(" Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()