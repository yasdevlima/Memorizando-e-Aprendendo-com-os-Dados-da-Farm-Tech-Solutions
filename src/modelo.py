import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

def gerar_dados():
    np.random.seed(42)

    umidade = np.random.uniform(30, 90, 1000)
    ph = np.random.uniform(5.5, 8.5, 1000)
    nitrogenio = np.random.uniform(0, 50, 1000)
    fosforo = np.random.uniform(0, 50, 1000)
    potassio = np.random.uniform(0, 50, 1000)

    rendimento = (
        2000
        + 40 * umidade
        - 90 * (ph - 7)**2
        + 5 * nitrogenio
        + 3 * fosforo
        + 4 * potassio
        + np.random.normal(0, 80, 1000)
    )

    dados = pd.DataFrame({
        'umidade': umidade,
        'ph': ph,
        'nitrogenio': nitrogenio,
        'fosforo': fosforo,
        'potassio': potassio,
        'rendimento': rendimento
    })

    return dados


def criar_features(df):
    df['ph_distancia_ideal'] = abs(df['ph'] - 7)
    df['umidade_quadrado'] = df['umidade'] ** 2
    df['total_nutrientes'] = df['nitrogenio'] + df['fosforo'] + df['potassio']
    df['umidade_ph'] = df['umidade'] * df['ph']
    return df


def treinar_modelo(dados):
    dados = criar_features(dados)

    features = [
        'umidade', 'ph', 'nitrogenio', 'fosforo', 'potassio',
        'ph_distancia_ideal', 'umidade_quadrado', 'total_nutrientes', 'umidade_ph'
    ]

    X = dados[features]
    y = dados['rendimento']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    os.makedirs('model', exist_ok=True)
    joblib.dump(modelo, 'model/modelo_regressao.pkl')

    metricas = {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'R²': r2}
    pd.DataFrame([metricas]).to_csv('model/metricas_modelo.csv', index=False)

    return modelo, metricas


if __name__ == "__main__":
    dados = gerar_dados()
    modelo, metricas = treinar_modelo(dados)
    print("Modelo treinado e salvo!")
    print("Métricas:", metricas)
