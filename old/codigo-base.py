import pandas as pd

pkmn = pd.read_csv('dataset/pokemon.csv')
desc = pkmn.describe()
#print(desc)

# CONVERTE ALTURA DE INCHES PRA CENTIMETROS
altura = pkmn['height']
#print(altura)
nova_altura = []
for i in altura:
    #print(i)
    i_array = i.split("'")
    feet = float(i_array[0])
    inch = float(i_array[1][:-1])
    #print(f"{feet} - {inch}",end=' ')
    inch += feet * 12
    h_cm = round(inch * 2.54, 1)
    #print(f"{h_cm} cm")
    nova_altura.append(h_cm)
#print(nova_altura)

# CONVERTE PESO DE POUNDS PRA KGs
peso = pkmn['weight']
#print(altura)
novo_peso = []
for i in peso:
    #print(i)
    i_array = i.split(" ")
    lbs = float(i_array[0])
    kg = round(lbs*0.453592,1)

    novo_peso.append(kg)
#print(novo_peso)

# ADICIONA A COLUNA DE GENS 
gen_limites = [151,251,386,493,649,721,802]
gens = []
k = 1
for i in range(802):
    if i+1 > gen_limites[k-1]:
        k += 1
    gens.append(k)

#print(gens)
#print(gens[151])

for i in range(802,1061):
   gens.append(0) # nao sei qual é a gen!

pkmn['gen'] = gens

# ATUALIZANDO AS COLUNAS
pkmn['height'] = nova_altura
pkmn['weight'] = novo_peso


# SALVANDO O NOVO CSV
pkmn.to_csv('dataset/pokemon_atualizado.csv', index=False)

