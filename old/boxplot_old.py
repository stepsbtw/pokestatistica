import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/pokemon_atualizado.csv')
stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total']

for stat in stats:
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
    plt.savefig(f'imgs/BOXPLOTS/{stat.upper()}.png')

    plt.show()

# Gerar boxplots combinados para todas as estatísticas
fig, axes = plt.subplots(nrows=1, ncols=len(stats), figsize=(15, 5))  # Ajuste conforme necessário
for i, stat in enumerate(stats):
    axes[i].boxplot(df[stat], vert=False)
    axes[i].set_title(stat.upper())
    axes[i].set_xlabel(stat.upper())

plt.suptitle('Boxplots de todos os Atributos', fontsize=18)
plt.grid(False)
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar espaço para o título
plt.savefig(f'imgs/BOXPLOTS/ALL.png')
plt.show()