import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import sturges_rule

def main():
    df = pd.read_csv('../dataset/pokemon.csv')
    df = df.drop(columns=['id','ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])

    stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed']
    
    # Número de classes usando a regra de Sturges
    n_class = sturges_rule(len(df))
    
    convoluted_distribution = None
    bin_edges = None
    
    for col in stats:
        hist, bins = np.histogram(df[col], bins=n_class, density=True)
        
        # Normalizando para frequência relativa
        hist = hist / hist.sum()
        
        if convoluted_distribution is None:
            convoluted_distribution = hist
            bin_edges = bins[:-1]
        else:
            convoluted_distribution = np.convolve(convoluted_distribution, hist, mode='same')
        
        # Plotar histograma individual
        plt.figure()
        plt.bar(bins[:-1], hist, width=np.diff(bins), color='skyblue', edgecolor='black', align='edge')
        plt.title(f'Histogram of {col.capitalize()} (Relative Frequency)', fontsize=16)
        plt.xlabel(col.upper(), fontsize=14)
        plt.ylabel('Relative Frequency', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(False)
        plt.tight_layout()
        plt.savefig(f'imgs/{col.upper()}_hist.png')
        plt.show()
    
    # Visualizar a convolução de todas as distribuições como gráfico de barras
    plt.figure()
    plt.bar(bin_edges, convoluted_distribution, width=np.diff(bin_edges).mean(), color='red', edgecolor='black', align='edge')
    plt.title('Convolution of All Stat Distributions', fontsize=16)
    plt.xlabel('Stat Value', fontsize=14)
    plt.ylabel('Convoluted Frequency', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('imgs/convoluted_distribution.png')
    plt.show()

if __name__ == "__main__":
    main()
