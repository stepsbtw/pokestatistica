import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/pokemon.csv')
df = df.drop(columns=['id','ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])

stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total']

# quão comum é cada tipo?
tipo1_Fi = df['type1'].value_counts() # absoluta
tipo1_fi = df['type1'].value_counts(normalize=True)
tipo1_fai = tipo1_fi.cumsum()

tipo2_Fi = df['type2'].value_counts() # absoluta
tipo2_fi = df['type2'].value_counts(normalize=True)
tipo2_fai = tipo2_fi.cumsum()

tipo1_freq = pd.DataFrame({'Fi': tipo1_Fi,
                                  'fi': tipo1_fi,
                                  'fai': tipo1_fai})

tipo2_freq = pd.DataFrame({'Fi': tipo2_Fi,
                                  'fi': tipo2_fi,
                                  'fai': tipo2_fai})

# Exemplo de dicionário de cores para os tipos de Pokémon
type_colors = {
    'Grass': 'green',
    'Fire': 'red',
    'Water': 'blue',
    'Electric': 'yellow',
    'Ice': 'cyan',
    'Fighting': 'brown',
    'Poison': 'purple',
    'Ground': 'gold',
    'Flying': 'skyblue',
    'Psychic': 'pink',
    'Bug': 'limegreen',
    'Rock': 'darkgoldenrod',
    'Ghost': 'indigo',
    'Dragon': 'orange',
    'Dark': 'black',
    'Steel': 'gray',
    'Fairy': 'hotpink',
    'Normal': 'silver',
}


# Gráfico para Tipo Primário
plt.barh(
    tipo1_Fi.index,
    tipo1_Fi.values,
    color=[type_colors[tipo] for tipo in tipo1_Fi.index]
)
plt.xlabel('Quantidade')
plt.ylabel('Tipo Primário')
plt.title('Quantidade de Pokémons por Tipo Primário')
plt.show()

# Gráfico para Tipo Secundário
plt.barh(
    tipo2_Fi.index,
    tipo2_Fi.values,
    color=[type_colors[tipo] for tipo in tipo2_Fi.index]
)
plt.xlabel('Quantidade')
plt.ylabel('Tipo Secundário')
plt.title('Quantidade de Pokémons por Tipo Secundário')
plt.show()