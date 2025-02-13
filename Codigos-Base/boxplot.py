import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Carregar os dados
df = pd.read_csv('dataset/pokemon_atualizado.csv')

# Lista de atributos a serem analisados
stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed']

# Criar boxplots individuais
for stat in stats:
    # Calcular Q1 e Q3
    Q1 = df[stat].quantile(0.25)
    Q3 = df[stat].quantile(0.75)
    dist_interq = Q3 - Q1

    # Limites para detecção de outliers
    li = Q1 - 1.5 * dist_interq
    Li = Q3 + 1.5 * dist_interq

    # Identificar outliers
    outliers_stat = df.loc[(df[stat] < li) | (df[stat] > Li), stat]
    outlier_names = df.loc[(df[stat] < li) | (df[stat] > Li), 'forme'].tolist()

    sorted_outliers = sorted(zip(outlier_names, outliers_stat), key=lambda x: x[1], reverse=True)

    # Criar boxplot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[stat], color='skyblue', width=0.5)
    plt.xlabel(stat.upper())
    plt.title(f'Boxplot de {stat.upper()}')

    # Criar uma lista vertical de outliers com nomes de Pokémon
    outliers_text = '\n'.join([f'{i+1}. {name} - {stat.upper()}: {round(val, 2)}' 
                             for i, (name, val) in enumerate(sorted_outliers)])

    outliers_text = f'Outliers:\n{outliers_text}'
    
    # Adicionar a legenda para os outliers
    plt.scatter([], [],color='white',edgecolor='black', label='Outliers')  # Exemplo de ponto para a legenda
    plt.legend(loc='upper left', fontsize=10)

    # Ajustar posição para fora do gráfico
    plt.subplots_adjust(right=0.8)  # Ajuste do gráfico para dar espaço para o texto à direita

    # Adicionar a lista de outliers ao lado direito do gráfico
    plt.figtext(0.85, 0.5, outliers_text, ha='left', va='center', fontsize=10, color='black', bbox=dict(facecolor='white', alpha=0.7))

    # Salvar figura
    plt.savefig(f'imgs/BOXPLOTS/{stat.upper()}.png', bbox_inches='tight')
    plt.close()  # Fechar para não sobrecarregar a memória

# Criar boxplots combinados
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[stats], palette='coolwarm')

plt.xticks(range(len(stats)), [s.upper() for s in stats])
plt.title('Boxplots de Todos os Atributos', fontsize=14)
plt.xlabel('Atributos')
plt.ylabel('Valores')

plt.savefig('imgs/BOXPLOTS/boxplots_combinados.png', bbox_inches='tight')
plt.show()

# FAZENDO PRO TOTAL

# Calcular Q1 e Q3
Q1 = df['total'].quantile(0.25)
Q3 = df['total'].quantile(0.75)
dist_interq = Q3 - Q1

# Limites para detecção de outliers
li = Q1 - 1.5 * dist_interq
Li = Q3 + 1.5 * dist_interq

# Identificar outliers
outliers = df.loc[(df['total'] < li) | (df['total'] > Li), 'total']

# Criar boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['total'], color='skyblue', width=0.5)
plt.xlabel('TOTAL')
plt.title('Boxplot de TOTAL')

# Salvar figura
plt.savefig(f'imgs/BOXPLOTS/TOTAL.png', bbox_inches='tight')
plt.close()  # Fechar para não sobrecarregar a memória

