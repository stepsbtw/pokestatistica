import numpy as np
import pandas as pd

df = pd.read_csv("dataset/pokemon_atualizado")
df = df[df['id'] >= 802]
gen_limites = [151,251,386,493,649,721,802]


for idx, row in df.iterrows():
    nome = row['forme']

    if 'Mega' in nome:
        df.loc[idx, 'gen'] = 6  # Geração 6
    elif 'Alola' in nome:
        df.loc[idx, 'gen'] = 7  # Geração 7
    else:
        # Definir geração baseada no ndex
        ndex = row['ndex']
        for i, limite in enumerate(gen_limites):
            if ndex <= limite:
                df.loc[idx, 'gen'] = i + 1
                break

df.to_csv("dataset/pokemon_atualizado.csv")
