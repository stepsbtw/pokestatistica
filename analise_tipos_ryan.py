import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('dataset/pokemon_atualizado.csv')

#  Tratar valores ausentes na coluna 'type2'
df['type2'].fillna('', inplace=True)  # Substituir NaN por string vazia

def analisar_tipos_por_geracao(df):
    tipos_por_geracao = {}
    combinacoes_por_geracao = {}

    for gen in df['gen'].unique():  
        df_gen = df[df['gen'] == gen]  
        tipos = df_gen['type1'].tolist() + df_gen['type2'].tolist()
        tipos = [tipo for tipo in tipos if tipo != '']  
        contagem_tipos = Counter(tipos)
        tipos_por_geracao[gen] = contagem_tipos

        # Criar combinações de tipos
        combinacoes = df_gen.apply(lambda row: tuple(sorted([row['type1'], row['type2']])), axis=1)
        combinacoes = [comb for comb in combinacoes if comb != ('', '')]  
        contagem_combinacoes = Counter(combinacoes)
        combinacoes_por_geracao[gen] = contagem_combinacoes

    return tipos_por_geracao, combinacoes_por_geracao

# Executar a análise
tipos_por_geracao, combinacoes_por_geracao = analisar_tipos_por_geracao(df)

# Definir uma ordem fixa para os tipos
# Criar lista de tipos únicos sem duplicatas e ordenada
tipos_unicos = sorted(list(set(df['type1'].unique().tolist() + df['type2'].unique().tolist())))
tipos_unicos = [tipo for tipo in tipos_unicos if tipo != '']  # Remover strings vazias


# Gráfico de Barras para Tipos Mais Comuns e Mais Raros por Geração
plt.figure(figsize=(15, 10))
for idx, (gen, contagem) in enumerate(tipos_por_geracao.items(), start=1):  
    contagem_completa = {tipo: contagem.get(tipo, 0) for tipo in tipos_unicos}
    
    tipos = list(contagem_completa.keys())
    valores = list(contagem_completa.values())

    tipo_mais_comum = tipos[np.argmax(valores)]
    tipo_mais_raro = tipos[np.argmin(valores)]

    plt.subplot(3, 3, idx)  
    sns.barplot(x=tipos, y=valores, palette='viridis', order=tipos_unicos) 
    plt.title(f'Geração {gen}\nMais comum: {tipo_mais_comum}\nMais raro: {tipo_mais_raro}')
    plt.xticks(rotation=90, fontsize=8)  
    plt.xlabel('Tipos')
    plt.ylabel('Contagem')
    plt.tight_layout(pad=3.0)  

plt.show()  

# Análise de Combinações de Tipos
todas_combinacoes = set()
for gen, combinacoes in combinacoes_por_geracao.items():
    todas_combinacoes.update(combinacoes.keys())

# Criar matriz de combinações de tipos
matriz_combinacoes = pd.DataFrame(0, index=tipos_unicos, columns=tipos_unicos)

for gen, combinacoes in combinacoes_por_geracao.items():
    for comb, contagem in combinacoes.items():
        if len(comb) == 2:
            if comb[0] in tipos_unicos and comb[1] in tipos_unicos:
                matriz_combinacoes.loc[comb[0], comb[1]] += contagem
                matriz_combinacoes.loc[comb[1], comb[0]] += contagem

# Gráfico de Heatmap para Combinações de Tipos
plt.figure(figsize=(12, 10))
sns.heatmap(matriz_combinacoes, annot=True, fmt='d', cmap='viridis', cbar=True)
plt.title('Combinações de Tipos de Pokémons')
plt.xlabel('Tipo 2')
plt.ylabel('Tipo 1')
plt.show()  # Exibir o heatmap

matriz_combinacoes.to_csv('dataset/matriz_combinacoes_tipos.csv', index=False)

print("Análise concluída! Os gráficos foram exibidos.")