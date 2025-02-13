import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("dataset/pokemon_atualizado.csv")

# Seleciona as colunas relevantes
stats_cols2 = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total', 'type1']
df_stats2 = df[stats_cols2]

# Agrupa por tipo e calcula a média
type_stats = df_stats2.groupby('type1').mean()


sns.set_style("whitegrid")  # Melhor aparência para os gráficos

# Determinar o maior valor de status para padronizar os limites do eixo Y
max_value = type_stats.drop(columns=['total']).max().max() *1.05

for poke_type in type_stats.index:
    plt.figure(figsize=(8, 5))
    
    stats = type_stats.loc[poke_type].drop('total')  # Removendo a coluna 'total'
    stats.index = stats.index.str.upper()  # Converter nomes dos atributos para maiúsculas

    sns.barplot(y=stats.index, x=stats.values, palette='Set2')

    plt.title(f"MÉDIAS DE STATUS DO TIPO {poke_type.upper()}")
    plt.ylabel("ATRIBUTO")
    plt.xlabel("VALOR MÉDIO")
    plt.xlim(0, max_value)  # Definir limite fixo para o eixo X
    
    plt.tight_layout()
    plt.savefig(f'imgs/BARPLOT/stats_{poke_type}.png')
    plt.close()

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

# Cria um gráfico com o total médio de todos os tipos (horizontal)

plt.figure(figsize=(8, 10))  # Ajuste para melhor visualização
colors = [type_colors.get(t, 'gray') for t in type_stats.index]
sns.barplot(y=type_stats.index, x=type_stats['total'], palette=colors)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

plt.title("Total Médio por Tipo de Pokémon", fontsize=16)
plt.ylabel("Tipo de Pokémon",fontsize=14)
plt.xlabel("Total Médio",fontsize=14)

plt.tight_layout()
plt.savefig('imgs/total_medio_por_tipo.png')
plt.show()
