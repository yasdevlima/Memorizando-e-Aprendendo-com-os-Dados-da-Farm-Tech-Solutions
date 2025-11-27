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
A solução utiliza Machine Learning (Regressão Linear), engenharia de features, tratamento de dados, validação, e um dashboard interativo em Streamlit para exibir previsões, métricas e recomendações automáticas de manejo agrícola. O objetivo é oferecer uma ferramenta simples e intuitiva para auxiliar produtores rurais na tomada de decisão.

# 🔗 Vídeo de Apresentação

 Confira a explicação completa do projeto no YouTube:
👉 **[Clique aqui para assistir]([https://youtube.com/seu_link_aqui](https://youtu.be/ueN8HRd45YE))**

# 📁 Estrutura do Projeto

## modelo.py
 - Gera dados simulados
 - Cria features novas
 - Treina o modelo de Regressão Linear

 Salva:
 - modelo_regressao.pkl
 - metricas_modelo.csv

## app.py

 - Carrega o modelo treinado
 - Mostra métricas em gráfico
 - Permite ajustar valores pelo usuário
 - Faz previsões
 - Mostra recomendações automáticas
 - 
## 📚 Bibliotecas Utilizadas

 - pandas
 - numpy
 - scikit-learn
 - joblib
 - streamlit
 - plotly

## Conclusão

 - O projeto entrega um sistema simples e funcional que combina:
 - Machine Learning
 - Dashboard interativo
 - Previsões agrícolas
 - Recomendações automáticas
 - Perfeito para demonstrar aplicação prática de IA no agronegócio
