import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Deixei o arquivo com meu nome, mas é para passar o codigo para o jupyter notebook

# Carrega os dados
df = pd.read_csv("dataset/pokemon_atualizado.csv")

# Seleciona as colunas relevantes
stats_cols = ['gen', 'hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total']
df_stats = df[stats_cols]

# Matriz de correlação
corr_matrix = df_stats.iloc[:, 1:].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação dos Stats")
plt.savefig(f'imgs/matriz_corr_status.png')
plt.show()

# Agrupa por geração e calcula a média
gen_stats = df_stats.groupby('gen').mean()

# Gráfico de evolução dos stats por geração
plt.figure(figsize=(12, 6))
for stat in ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed']:
    plt.plot(gen_stats.index, gen_stats[stat], marker='o', label=stat)

plt.plot(gen_stats.index, gen_stats['total'], marker='o', label='total', linewidth=2, color='black')
plt.title("Evolução dos Stats Médios por Geração")
plt.xlabel("Geração")
plt.ylabel("Stats Médios")
plt.legend()
plt.grid(True)
plt.savefig(f'imgs/status_por_gen.png')
plt.show()

# Seleciona as colunas relevantes
stats_cols2 = ['gen', 'hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total', 'type1']
df_stats2 = df[stats_cols2]

# Agrupa por tipo e calcula a média
type_stats = df_stats2.groupby('type1').mean()

# Encontra o maior status médio para cada tipo
max_stats = type_stats.drop(columns=['total']).idxmax(axis=1)
max_values = type_stats.max(axis=1)

# Cria um gráfico para mostrar os maiores status médios por tipo
plt.figure(figsize=(14, 8))
sns.barplot(x=max_values.index, y=max_values.values, hue=max_stats.values, palette='Set1')
plt.title("Maior Status Médio por Tipo de Pokémon")
plt.xlabel("Tipo de Pokémon")
plt.ylabel("Valor Médio do Maior Atributo")
plt.xticks(rotation=90)
plt.legend(title='Maior Atributo', loc='upper right')
plt.tight_layout()
plt.savefig(f'imgs/maior_status_por_tipo.png')
plt.show()