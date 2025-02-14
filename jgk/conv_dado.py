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
    max_sum = 11 * n_dice  # Maior soma possível (6 por dado)
    sum_values = np.arange(min_sum, max_sum + 1)

    # Aplicando a transformação ao eixo X
    transformed_x = (sum_values * 27.27) - 13.635

    # Reduzindo a quantidade de rótulos para melhorar a legibilidade
    step = max(1, len(transformed_x) // 10)  # Mostra cerca de 10 rótulos no eixo X
    x_ticks_positions = transformed_x[::step]
    x_ticks_labels = [f"{val:.2f}" for val in transformed_x[::step]]

    # Plotando a distribuição da convolução
    plt.figure(figsize=(8, 5))
    plt.bar(transformed_x, conv_result, width=27.27, color='blue', edgecolor='black', alpha=0.7)
    plt.xlabel('Soma Transformada dos Dados', fontsize=14)
    plt.ylabel('Probabilidade', fontsize=14)
    plt.title(f'Convolução de todos os atributos', fontsize=16)
    plt.xticks(x_ticks_positions, x_ticks_labels, rotation=45)  # Rótulos girados para melhor legibilidade
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Exemplo de uso com N dados de 6 lados, cada um com distribuições diferentes
probabilities_list = [
    [0.011310084825636193, 0.26578699340245054, 0.4816211121583412, 0.17907634307257306, 0.0471253534401508, 0.008482563619227144, 0.002827521206409048, 0.000942507068803016, 0.000942507068803016, 0.001885014137606032, 0.0] ,
[0.024505183788878417, 0.1941564561734213, 0.35532516493873706, 0.2469368520263902, 0.1357210179076343, 0.03204524033930255, 0.011310084825636193, 0.0, 0.0, 0.0, 0.0] ,
[0.01413760603204524, 0.2846371347785108, 0.36286522148916117, 0.21017907634307256, 0.09896324222431668, 0.019792648444863337, 0.00471253534401508, 0.001885014137606032, 0.002827521206409048, 0.0, 0.0] ,
[0.033930254476908575, 0.24599434495758718, 0.3449575871819039, 0.22431668237511782, 0.11404335532516494, 0.02639019792648445, 0.00942507068803016, 0.000942507068803016, 0.0, 0.0, 0.0] ,
[0.017907634307257305, 0.27332704995287466, 0.3647502356267672, 0.23845428840716307, 0.08482563619227144, 0.01885014137606032, 0.0, 0.000942507068803016, 0.000942507068803016, 0.0, 0.0] ,
[0.04806786050895382, 0.2874646559849199, 0.29783223374175305, 0.26201696512723843, 0.09330819981149858, 0.010367577756833177, 0.000942507068803016, 0.0, 0.0, 0.0, 0.0]
]

dice_convolution(probabilities_list)


