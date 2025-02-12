import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("../dataset/pokemon_atualizado.csv")

# Seleciona as colunas relevantes
stats_cols2 = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total', 'type1']
df_stats2 = df[stats_cols2]

# Agrupa por tipo e calcula a média
type_stats = df_stats2.groupby('type1').mean()

# Cria um gráfico para cada tipo de Pokémon (exceto 'total')
for poke_type in type_stats.index:
    plt.figure(figsize=(8, 5))
    stats = type_stats.loc[poke_type].drop('total')
    sns.barplot(x=stats.index, y=stats.values, palette='Set2')
    plt.title(f"Médias de Status para {poke_type}")
    plt.xlabel("Atributo")
    plt.ylabel("Valor Médio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'imgs/stats_{poke_type}.png')
    plt.show()

# Define a paleta de cores para o gráfico de total médio por tipo
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

# Cria um gráfico com o total médio de todos os tipos
plt.figure(figsize=(12, 6))
colors = [type_colors.get(t, 'gray') for t in type_stats.index]
sns.barplot(x=type_stats.index, y=type_stats['total'], palette=colors)
plt.title("Total Médio por Tipo de Pokémon")
plt.xlabel("Tipo de Pokémon")
plt.ylabel("Total Médio")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('imgs/total_medio_por_tipo.png')
plt.show()
