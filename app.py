import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap


base = pd.read_csv('songs.csv')

st.title('Gráfico de popularidade das músicas do spotify')

st.caption("Essa é uma coleção abrangente de informações e letras de músicas obtidas de uma lista de reprodução pública. \
Ele contém aproximadamente 660 músicas, cada uma representada por vários atributos, como nome, letra, cantor, filme, gênero e classificação.")

st.write(base)

popularityGrafic = base['Popularity'].value_counts()
fig, ax = plt.subplots(figsize=(10, 10))
sns.histplot(data=base, x='Popularity', kde=True, color='g')
plt.xlabel('Popularidade')
plt.ylabel('Contagem')
plt.title('Nível de popularidade das músicas')
st.pyplot(fig)

