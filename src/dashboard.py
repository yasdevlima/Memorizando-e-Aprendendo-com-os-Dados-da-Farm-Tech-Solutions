import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


modelo = joblib.load('model/modelo_regressao.pkl')


def criar_features(umidade, ph, nitrogenio, fosforo, potassio):
    ph_distancia_ideal = abs(ph - 7.0)
    umidade_quadrado = umidade ** 2
    total_nutrientes = nitrogenio + fosforo + potassio
    umidade_ph = umidade * ph

    return np.array([[
        umidade, ph, nitrogenio, fosforo, potassio,
        ph_distancia_ideal, umidade_quadrado,
        total_nutrientes, umidade_ph
    ]])

metricas_df = pd.read_csv('model/metricas_modelo.csv')

fig_metricas = go.Figure(go.Bar(
    x=metricas_df.columns,
    y=metricas_df.iloc[0],
    text=metricas_df.iloc[0],
    textposition='auto'
))
fig_metricas.update_layout(
    title='Métricas do Modelo de Regressão',
    xaxis_title='Métrica',
    yaxis_title='Valor'
)


st.title("🌱 Assistente Agrícola Inteligente")
st.write("Sistema de previsão e recomendações de manejo para apoio ao produtor rural.")

st.header("📊 Métricas do Modelo")
st.plotly_chart(fig_metricas)


st.header("🌾 Previsões Agrícolas")

umidade = st.slider('Umidade do Solo (%)', 30, 90, 60)
ph = st.slider('pH do Solo', 5.5, 8.5, 7.0)

nitrogenio = st.slider("Nitrogênio (mg/kg)", 0, 50, 20)
fosforo = st.slider("Fósforo (mg/kg)", 0, 50, 15)
potassio = st.slider("Potássio (mg/kg)", 0, 50, 18)

# Criar features
X_input = criar_features(umidade, ph, nitrogenio, fosforo, potassio)

# Previsão do rendimento
rendimento_previsto = modelo.predict(X_input)[0]

st.subheader("🌿 Rendimento Previsto")
st.write(f"**{rendimento_previsto:.2f} kg/hectare**")


st.header("🧪 Recomendações de Fertilização")

total_nutrientes = nitrogenio + fosforo + potassio

if total_nutrientes < 40:
    fertilizacao = "🔴 Necessária URGENTE — nutrientes muito baixos"
elif total_nutrientes < 70:
    fertilizacao = "🟠 Fertilização moderada recomendada"
else:
    fertilizacao = "🟢 Níveis adequados de nutrientes"

st.write(f"**Sugestão de Fertilização:** {fertilizacao}")

st.header("💧 Recomendações de Irrigação")

if umidade < 50:
    acao_irrigacao = "🔴 IRRIGAR AGORA — umidade crítica"
elif rendimento_previsto < 2000:
    acao_irrigacao = "🟠 Irrigação preventiva recomendada"
else:
    acao_irrigacao = "🟢 Condições adequadas, sem necessidade imediata"

st.write(f"**Ação Sugerida:** {acao_irrigacao}")


st.header("📈 Relação entre Umidade e pH")

fig = px.scatter(
    x=[umidade],
    y=[ph],
    labels={'x': 'Umidade (%)', 'y': 'pH do Solo'},
    title='Ponto Atual de Medição'
)
st.plotly_chart(fig)
