import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Deixei o arquivo com meu nome, mas é para passar o codigo para o jupyter notebook

# Carrega os dados
df = pd.read_csv("dataset/pokemon_atualizado.csv")

# Seleciona as colunas relevantes
stats_cols = ['gen', 'hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'weight', 'height', 'total']
df_stats = df[stats_cols]

# Matriz de correlação
corr_matrix = df_stats.iloc[:, 1:].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".2f")
plt.title("Matriz de Correlação dos Stats (+ Peso e Altura)")
plt.savefig(f'imgs/matriz_corr_status.png')
plt.show()

# Agrupa por geração e calcula a média
gen_stats = df_stats.groupby('gen').mean()

# Gráfico de evolução dos atributos individuais por geração
plt.figure(figsize=(12, 6))
for stat in ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed']:
    plt.plot(gen_stats.index, gen_stats[stat], marker='o', label=stat)

plt.title("Evolução dos Stats Médios por Geração (Atributos Individuais)")
plt.xlabel("Geração")
plt.ylabel("Stats Médios")
plt.legend()
plt.grid(True)
plt.savefig('imgs/status_atributos_por_gen.png')
plt.show()

# Gráfico apenas para o total
plt.figure(figsize=(12, 6))
plt.plot(gen_stats.index, gen_stats['total'], marker='o', label='Total', linewidth=2, color='black')

plt.title("Evolução do Stat Total Médio por Geração")
plt.xlabel("Geração")
plt.ylabel("Total Médio de Stats")
plt.legend()
plt.grid(True)
plt.savefig('imgs/status_total_por_gen.png')
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
plt.figure(figsize=(7, 4))
sns.barplot(x=max_values.values, y=max_values.index, hue=max_stats.values, palette='Set2')
plt.title("Maior Status Médio por Tipo de Pokémon")
plt.xlabel("Valor Médio do Maior Atributo")
plt.ylabel("Tipo de Pokémon")
plt.legend(title='Maior Atributo', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(f'imgs/maior_status_por_tipo.png')
plt.show()