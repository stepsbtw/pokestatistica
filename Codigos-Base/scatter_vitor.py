import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

df = pd.read_csv('dataset/pokemon_atualizado.csv')

pkmn1= df[['weight','speed','gen','post-evolution']]
pkmn2= df[['weight','speed','gen']]
peso = pkmn1.sort_values('weight')

peso_analise = peso[peso['post-evolution'] == ' ']
peso_analise2 = peso[peso['post-evolution'] != ' ']
#peso_analise3 = pkmn2.groupby('gen').mean()
#print(df['pre-evolution'])

# Criando o ambiente do gráfico 
sns.set_style("white")
plt.figure(figsize=(10, 7))

# Gráfico de Dispersão
g = sns.scatterplot(x="weight", y="speed", 
                    data=peso_analise)
plt.title("Peso x Velocidade - Ultima evolução")

sns.set_style("white")
plt.figure(figsize=(10, 7))

# Gráfico de Dispersão
g = sns.scatterplot(x="weight", y="speed", 
                    data=peso_analise2)
plt.title("Peso x Velocidade")
'''
plt.figure(2)
plt.bar(peso_analise2['weight'],peso_analise2['speed'])
plt.grid()
'''
plt.show()

