import numpy as np
import matplotlib.pyplot as plt

def dice_convolution(probabilities_list):
    """
    Calcula a convolução da soma de múltiplos dados de 6 lados, cada um com uma distribuição de probabilidades diferente.
    
    :param probabilities_list: Lista de listas, onde cada lista representa as probabilidades para um dado de 6 lados.
    """
    # Inicializa a distribuição com o primeiro dado
    probabilities = np.array(probabilities_list[0]) / np.sum(probabilities_list[0])  # Normalizar
    conv_result = probabilities
    
    # Convolução para os demais dados
    for probabilities in probabilities_list[1:]:
        probabilities = np.array(probabilities) / np.sum(probabilities)  # Normalizar
        conv_result = np.convolve(conv_result, probabilities)
    
    # Definição dos valores possíveis para a soma dos dados
    n_dice = len(probabilities_list)
    min_sum = n_dice  # Menor soma possível (1 por dado)
    max_sum = 6 * n_dice  # Maior soma possível (6 por dado)
    sum_values = np.arange(min_sum, max_sum + 1)
    
    # Plotando a distribuição da convolução
    plt.figure(figsize=(8, 5))
    plt.bar(sum_values, conv_result, color='blue', edgecolor='black', alpha=0.7)
    plt.xlabel('Soma dos Dados', fontsize=14)
    plt.ylabel('Probabilidade', fontsize=14)
    plt.title(f'Distribuição da Soma de {n_dice} Dados de 6 Lados', fontsize=16)
    plt.xticks(sum_values)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Exemplo de uso com N dados de 6 lados, cada um com distribuições diferentes
probabilities_list = [
    [1/6, 1/6, 1/6,1/6, 1/6, 1/6],  # Primeiro dado
    [1/6, 1/6, 1/6,1/6, 1/6, 1/6],  # Segundo dado
]

dice_convolution(probabilities_list)