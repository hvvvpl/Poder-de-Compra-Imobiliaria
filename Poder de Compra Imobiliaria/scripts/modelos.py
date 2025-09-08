# machile learning (regressão, classificação, clustering)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



def treinar_modelos(df):
    resultados = {}

    # Exemplo: prever preço de imóvel a partir do INPC
    X = df[["inpc"]]
    y = df["preco_medio"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    reg = LinearRegression().fit(X_train, y_train)
    y_pred = reg.predict(X_test)

    resultados["regressao_rmse"] = mean_squared_error(y_test, y_pred, squared=False)
    resultados["regressao_r2"] = r2_score(y_test, y_pred)

    print(" Modelo de regressão treinado e avaliado.")
    return resultados

