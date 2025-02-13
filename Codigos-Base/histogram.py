import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import sturges_rule

def main():
    df = pd.read_csv('dataset/pokemon_atualizado.csv')

    stats = ['attack', 'defense', 'spattack', 'spdefense', 'speed'] # sem hp e total por conta de escala

    # Número de classes usando a regra de Sturges
    n_class = sturges_rule(len(df))

    # Encontrar limites globais do eixo X e Y
    global_x_min = min(df[stats].min())  # Menor valor de todas as colunas
    global_x_max = max(df[stats].max())  # Maior valor de todas as colunas
    x_buffer = (global_x_max - global_x_min) * 0.05  # Adiciona um pequeno espaço extra
    global_x_min -= x_buffer
    global_x_max += x_buffer

    global_y_max = 0
    for col in stats:
        max_freq = np.histogram(df[col], bins=n_class)[0].max()
        global_y_max = max(global_y_max, max_freq)

    global_y_max *= 1.05  # Adiciona um pequeno buffer (5%)

    # Gerar os histogramas com os mesmos limites de X e Y
    for col in stats:
        plt.figure(figsize=(4, 3))
        df.hist(column=col, bins=n_class, color='skyblue', edgecolor='black')

        # Aplicar os mesmos limites de X e Y
        plt.xlim(global_x_min, global_x_max)
        plt.ylim(0, global_y_max)

        # Adicionar título e rótulos
        plt.title(f'Histograma de {col.upper()}', fontsize=14)
        plt.xlabel(col.upper(), fontsize=12)
        plt.ylabel('Frequência', fontsize=12)
        plt.grid(False)

        # Exibir e salvar gráfico
        plt.tight_layout()
        plt.savefig(f'imgs/HISTOGRAMAS/{col.upper()}.png')
        plt.close()  # Fecha o gráfico para evitar excesso de janelas abertas
    

    # FAZER PARA O HP 
    plt.figure(figsize=(4, 3))
    df.hist(column='hp', bins=n_class, color='skyblue', edgecolor='black')

    plt.title(f'Histograma de HP', fontsize=14)
    plt.xlabel('HP', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(False)

    plt.tight_layout()
    plt.savefig(f'imgs/HISTOGRAMAS/HP.png')
    plt.close()
    
    # FAZER PARA O TOTAL
    plt.figure(figsize=(4, 3))
    df.hist(column='total', bins=n_class, color='skyblue', edgecolor='black')

    plt.title(f'Histograma de TOTAL', fontsize=14)
    plt.xlabel('TOTAL', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.grid(False)

    plt.tight_layout()
    plt.savefig(f'imgs/HISTOGRAMAS/TOTAL.png')
    plt.close()


    # Criar um grande plot com subplots (2 linhas x 3 colunas)
    fig, axes = plt.subplots(2, 3, figsize=(15/1.5, 10/1.5))
    axes = axes.flatten()  # Transforma a matriz de eixos em um array

    fig.suptitle("Histogramas de Todos os Atributos")

    for i, col in enumerate(stats):
        axes[i].hist(df[col], bins=n_class, color='skyblue', edgecolor='black')

        # Aplicar os mesmos limites de X e Y
        axes[i].set_xlim(global_x_min, global_x_max)
        axes[i].set_ylim(0, global_y_max)

        # Adicionar título e rótulos
        axes[i].set_xlabel(col.upper(), fontsize=10)
        axes[i].set_ylabel('Frequência', fontsize=10)
        axes[i].grid(False)
    
    # adicionar o HP com a propria escala
    axes[5].hist(df['hp'], bins=n_class, color='skyblue', edgecolor='black')

    # Adicionar título e rótulos
    axes[5].set_xlabel('HP', fontsize=10)
    axes[5].set_ylabel('Frequência', fontsize=10)
    axes[5].grid(False)

    # Ajustar espaçamento entre os gráficos
    plt.tight_layout()
    plt.savefig('imgs/HISTOGRAMAS/histogramas_combinados.png')
    plt.show()

if __name__ == "__main__":
    main()
