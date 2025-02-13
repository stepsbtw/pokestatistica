import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import sturges_rule

def main():
    df = pd.read_csv('../dataset/pokemon.csv')
    df = df.drop(columns=['id','ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])

    stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed']
    
    # Número de bins usando a regra de Sturges
    n_class = sturges_rule(len(df))
    
    # Criar lista de distribuições individuais
    distributions = []
    for col in stats:
        hist, bin_edges = np.histogram(df[col], bins=n_class, density=True)
        hist = hist / hist.sum()  # Normalizando para frequência relativa
        distributions.append(hist)
    
    # Inicializar a convolução com a primeira distribuição
    convoluted_distribution = distributions[0]
    for dist in distributions[1:]:
        convoluted_distribution = np.convolve(convoluted_distribution, dist, mode='full')
    
    print(df[stats].sum(axis=1))
    # Ajustar eixo X corretamente
    min_sum = df[stats].sum(axis=1).min()
    max_sum = df[stats].sum(axis=1).max()
    new_bin_edges = np.arange(min_sum, max_sum + 1)
    
    # Visualizar a convolução de todas as distribuições como gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(new_bin_edges[:len(convoluted_distribution)], convoluted_distribution, width=1, color='red', edgecolor='black', align='center')
    plt.title('Convolution of All Stat Distributions', fontsize=16)
    plt.xlabel('Sum of Stats', fontsize=14)
    plt.ylabel('Convoluted Frequency', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('imgs/convoluted_distribution.png')
    plt.show()

if __name__ == "__main__":
    main()
