import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

df = pd.read_csv('dataset/pokemon_atualizado.csv')
'''

pos_evol = [' ']*1061
#print(pos_evol)
#df['pos-evolution'] = pos_evol
pkmn = df[['id','species','forme','pre-evolution']]


indice = 0
for i in pkmn['id']:
    print(i)
    p = pkmn[pkmn['id'] == i]
    #print(p['pre-evolution'])
    if type(p['pre-evolution'][indice]) == str:
        print("===========")
        #print(p)
        index_pre = pkmn[pkmn['species'] == p['pre-evolution'][indice]]['id']
        if index_pre.empty:
            index_pre = pkmn[pkmn['forme'] == p['pre-evolution'][indice]]['id']
        id_pre = index_pre.values[0] 
        print(f"pre-evolução: {id_pre}")
    
        if pos_evol[id_pre - 1] != ' ':
            pos_evol[id_pre - 1] += '/'
            pos_evol[id_pre - 1] += p['forme'].values[0]
            
        else:
            pos_evol[id_pre - 1] = p['forme'].values[0]
        #print(pos_evol[id_pre - 1])
    indice += 1
print(pos_evol)
df['post-evolution'] = pos_evol
df.to_csv('dataset/pokemon_atualizado.csv', index=False)
'''

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

