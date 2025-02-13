import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functions import sturges_rule


def main():
    df = pd.read_csv('dataset/pokemon_atualizado.csv')
    df = df.drop(columns=['id','ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])

    stats = ['hp', 'attack', 'defense', 'spattack', 'spdefense', 'speed', 'total']
    #descricao = df[stats].describe()

    # numero de classes usando a regra de sturges
    n_class = sturges_rule(len(df))

    for col in stats:
        df.hist(column = col, bins=n_class, color='skyblue', edgecolor='black')

        # Adicionar título e rótulos
        plt.title(f'Histogram of {col.capitalize()}', fontsize=16)
        plt.xlabel(col.upper(), fontsize=14)
        plt.ylabel('Frequency', fontsize=14)

        # Personalizar o gráfico
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        #plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.grid(False)
        
        # Exibir o gráfico
        plt.tight_layout()
        plt.savefig(f'imgs/{col.upper()}_hist.png')
        plt.show()
        

   # Gerar histogramas combinados para todas as estatísticas
    df[stats].hist(bins=n_class, color='skyblue', edgecolor='black', figsize=(12, 8), alpha=0.8)
    plt.suptitle('Histograms of All Stats', fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar espaço para o título
    plt.savefig(f'imgs/all_STATS_hists.png')
    #plt.show()

    df.to_csv("dataset/pokemon_atualizado.csv")
    
    
if __name__ == "__main__":
    main()
