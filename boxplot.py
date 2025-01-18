import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/pokemon_atualizado.csv')
df = df.drop(columns=['id','ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])
stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total']


for stat in stats:
    # fazendo as distribuicoes sem classes so pra comentar como nao deu certo.
    Fi = df[stat].value_counts()
    descricao = df[stats].describe()
    '''
    plt.bar(Fi.index, Fi.values)
    plt.xlabel(stat)
    plt.ylabel('Qtd de Pokemons')
    plt.title(f'Quantidade de Pokémons por {stat.upper()}')
    plt.savefig(f'imgs/{stat.upper()}_barh.png')
    plt.show()
    '''

    # BOXPLOTS
    Q1 = np.percentile(df[stat], 25)
    Q3 = np.percentile(df[stat], 75)
    dist_interq = Q3-Q1

    # limite da cauda
    li = Q1 - 1.5 * dist_interq
    Li = Q3 + 1.5 * dist_interq

    outliers = df[stat][(df[stat] < li) | (df[stat] > Li)]

    plt.boxplot(df[stat], vert=False)
    plt.xlabel(stat.upper())
    plt.title(f'Boxplot de Pokémons por {stat.upper()}')
    plt.savefig(f'imgs/{stat.upper()}_boxplot.png')

    plt.show()