import pandas as pd
import streamlit as st

st.set_page_config(
     page_title='Previsão de Renda',
     page_icon='https://handsonbanking.org/wp-content/uploads/2020/06/credit_arrowlightgreen.jpg',
     layout='wide',
     initial_sidebar_state='auto'
)

# st.sidebar.success("Select a demo above.")
# st.sidebar.header("Home")
# st.sidebar.success("test")

st.markdown('## Análise exploratória da Previsão de Renda')
st.markdown('### Entendimento do negócio')
st.markdown(
     """
     Uma instituição financeira pretende obter mais informações sobre o perfil de renda dos novos clientes, para a partir disso estabelecer os melhores critérios de limite de crédito, sem que seja necessário afetar a experiência do cliente com solicitações de documentação.

     A partir da base de dados coletada de alguns clientes, pretende-se criar um modelo preditivo para renda dos demais clientes.
     
"""
)

# mostrando o dataframe
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)
st.markdown('### Visualização do Dataframe')
st.dataframe(renda)

