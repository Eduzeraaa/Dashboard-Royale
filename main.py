import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard Clash Royale - <c2> Eduzera')
st.header('Última vez atualizado 18/08/2025')

abas = st.tabs([
    "Estatísticas Gerais",
    'Cartas da Torre',
    'Conquistas',
    'Deck Atual',
    'Cartas Evoluídas',
    'Nível das Cartas'
])

#? Aba 1: Estatísticas
with abas[0]:
    df_estatisticas = pd.read_csv('estatisticas.csv')
    st.subheader('Estatísticas Gerais')
    st.dataframe(df_estatisticas)


#? Aba 2: Cartas da Torre
with abas[1]:
    df_torres = pd.read_csv('cartas_da_torre.csv')
    st.subheader('Cartas da Torre')
    st.dataframe(df_torres)
    torres = [
        'tower-princess.png', 'cannoneer.png', 'dagger-duchess.png', 'royal-chef.png'
    ]
    colunas_por_linha = 4

    for i in range(0, len(torres), colunas_por_linha):
        cols = st.columns(colunas_por_linha)
        for j, col in enumerate(cols):
            if i + j < len(torres):
                col.image(torres[i + j], width=135)


#? Aba 3: Conquistas
with abas[2]:
    df_conquistas = pd.read_csv('conquistas.csv')
    st.subheader('Conquistas')
    st.dataframe(df_conquistas)



#? Aba 4: Deck Atual
with abas[3]:
    df_deck = pd.read_csv('deck_atual.csv')
    st.subheader('Deck Atual')
    st.dataframe(df_deck)
    cartas = [
    "executor_evo.png", "tesla_evo.png", "skeletons.png", "ice-spirit.png",
    "hog_rider.png", "monk.png", "encomenda.png", "tronco.png"
]

    colunas_por_linha = 4

    for i in range(0, len(cartas), colunas_por_linha):
        cols = st.columns(colunas_por_linha)
        for j, col in enumerate(cols):
            if i + j < len(cartas):
                col.image(cartas[i + j], width=135)



#? Aba 5: Evoluídas
with abas[4]:
    df_evoluidas = pd.read_csv('evoluidas.csv')
    st.subheader('Cartas Evoluídas')
    st.dataframe(df_evoluidas)

    evoluidas = 15
    bloqueadas = 20
    df_pizzaevo = pd.DataFrame({
        'Objeto': ['Possuídas', 'Faltando'],
        'Quantidade': [evoluidas, bloqueadas]
    })
    fig = px.pie(
        df_pizzaevo,
        names = "Objeto",
        values = 'Quantidade'
    )
    st.plotly_chart(fig)



#? Aba 6: Nível das cartas
with abas[5]:
    df_cartas = pd.read_csv('nivel_cartas.csv')
    st.subheader('Nível das Cartas')
    st.dataframe(df_cartas)
    fig = px.bar(
        df_cartas,
        x = 'Nível das Cartas',
        y = 'Quantidade'
    )
    st.plotly_chart(fig)
