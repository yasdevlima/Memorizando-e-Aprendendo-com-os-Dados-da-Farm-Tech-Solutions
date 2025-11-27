# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
    <a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Assistente Agrícola Inteligente

## 👨‍🎓 Integrantes: 

- Gabriel Coppola - RM568044
- Marina Clara Constantino Ribeiro - RM568576
- Yasmin Kauane Silva Lima - RM566645


# Sobre o Projeto

Este projeto implementa um Assistente Agrícola Inteligente capaz de prever o rendimento da plantação a partir de variáveis do solo.
A solução utiliza Machine Learning (Regressão Linear), engenharia de features, tratamento de dados, validação, e um dashboard interativo em Streamlit para exibir previsões, métricas e recomendações automáticas de manejo agrícola.

O objetivo é oferecer uma ferramenta simples e intuitiva para auxiliar produtores rurais na tomada de decisão.

## 1. Pipeline de Machine Learning
# Etapas implementadas:
1. Geração e preparo dos dados

O script modelo.py cria um conjunto de dados simulando informações agrícolas:
Umidade
pH do solo
Nitrogênio, Fósforo e Potássio
Rendimento da cultura

2. Engenharia de Features

Foram criadas novas variáveis para melhorar o aprendizado do modelo:
Distância do pH ideal
Soma total de nutrientes
Interação entre pH e umidade
Umidade ao quadrado

3. Separação dos dados
train_test_split(test_size=0.2)

4. Modelo

O modelo utilizado foi uma Regressão Linear, por ser simples, interpretável e adequado a problemas supervisados contínuos.

5. Avaliação

As métricas calculadas foram:
MAE
MSE
RMSE
R²

As métricas são salvas automaticamente em:
model/metricas_modelo.csv

O modelo final é salvo em:
model/modelo_regressao.pkl

## 📚 Bibliotecas Utilizadas

-pandas
-numpy
-scikit-learn
-joblib
-streamlit
-plotly

## Conclusão

Este projeto entrega uma solução completa que integra:
Machine Learning
Engenharia de dados
Métricas e validação
Interface interativa
Recomendações inteligentes
Servindo como um protótipo funcional de um assistente agrícola moderno e acessível.
