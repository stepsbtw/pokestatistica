import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/pokemon_atualizado.csv')

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
plt.figure(figsize=(5,4))
plt.barh(
    tipo1_Fi.index,
    tipo1_Fi.values,
    color=[type_colors[tipo] for tipo in tipo1_Fi.index]
)
plt.xlabel('Quantidade')
plt.ylabel('Tipo Primário')
plt.title('Quantidade de Pokémons por Tipo Primário')
plt.savefig('imgs/QTprimario_barrahorz.png')
plt.show()


# Gráfico para Tipo Secundário
plt.figure(figsize=(5,4))
plt.barh(
    tipo2_Fi.index,
    tipo2_Fi.values,
    color=[type_colors[tipo] for tipo in tipo2_Fi.index]
)
plt.xlabel('Quantidade')
plt.ylabel('Tipo Secundário')
plt.title('Quantidade de Pokémons por Tipo Secundário')
plt.savefig('imgs/QTsecundario_barh.png')
plt.show()

# Criar a figura e os eixos
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Gráfico para Tipo Primário
axes[0].barh(tipo1_Fi.index, tipo1_Fi.values, color=[type_colors[tipo] for tipo in tipo1_Fi.index])
axes[0].set_xlabel('Quantidade')
axes[0].set_ylabel('Tipo Primário')
axes[0].set_title('Quantidade de Pokémons por Tipo Primário')

# Gráfico para Tipo Secundário
axes[1].barh(tipo2_Fi.index, tipo2_Fi.values, color=[type_colors[tipo] for tipo in tipo2_Fi.index])
axes[1].set_xlabel('Quantidade')
axes[1].set_ylabel('Tipo Secundário')
axes[1].set_title('Quantidade de Pokémons por Tipo Secundário')

# Ajustar layout e salvar a figura
plt.tight_layout()
plt.savefig('imgs/QT_tipos_pokemon.png')
plt.show()
