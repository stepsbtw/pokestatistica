import pandas as pd

df = pd.read_csv('dataset/pokemon.csv')

# dropei as inutil
df = df.drop(columns=['ability1','ability2','abilityH','percent-male','percent-female','egg-group1','egg-group2','class','dex1','dex2'])
desc = df.describe()

# CONVERTE ALTURA DE INCHES PRA CMs
altura = df['height']
nova_altura = []
for i in altura:
    i_array = i.split("'")
    feet = float(i_array[0])
    inch = float(i_array[1][:-1])
    inch += feet * 12
    h_cm = round(inch * 2.54, 1)
    nova_altura.append(h_cm)

# CONVERTE PESO DE POUNDS PRA KGs
peso = df['weight']
novo_peso = []
for i in peso:
    i_array = i.split(" ")
    lbs = float(i_array[0])
    kg = round(lbs*0.453592,1)

    novo_peso.append(kg)

# ADICIONA A COLUNA DE GENS 
gen_limites = [151,251,386,493,649,721,802]
gens = []
k = 1
for i in range(802):
    if i+1 > gen_limites[k-1]:
        k += 1
    gens.append(k)

for i in range(802,1061):
   gens.append(0) # nao sei qual é a gen!

# ATUALIZANDO AS COLUNAS
df['gen'] = gens
df['height'] = nova_altura
df['weight'] = novo_peso

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



pos_evol = [' ']*1061

# ADICIONANDO COLUNA DE POS EVOLUCAO!

indice = 0
for i in df['id']:
    p = df[df['id'] == i]
    
    if type(p['pre-evolution'][indice]) == str:
        print("===========")
        index_pre = df[df['species'] == p['pre-evolution'][indice]]['id']
        if index_pre.empty:
            index_pre = df[df['forme'] == p['pre-evolution'][indice]]['id']
        id_pre = index_pre.values[0] 
        print(f"pre-evolução: {id_pre}")
    
        if pos_evol[id_pre - 1] != ' ':
            pos_evol[id_pre - 1] += '/'
            pos_evol[id_pre - 1] += p['forme'].values[0]
            
        else:
            pos_evol[id_pre - 1] = p['forme'].values[0]
    indice += 1
df['post-evolution'] = pos_evol


# SALVANDO O NOVO CSV
df.to_csv('dataset/pokemon_atualizado.csv', index=False)

