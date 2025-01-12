import pandas as pd

pkmn = pd.read_csv('pokemon.csv')
desc = pkmn.describe()
#print(desc)

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

gen_limites = [151,251,386,493,649,721,802]
gens = []
k = 1
for i in range(802):
    if i+1 > gen_limites[k-1]:
        k += 1
    gens.append(k)
#print(gens)
#print(gens[151])
pkmn['gen'] = gens
print(pkmn['gen'])


###### Vitor ######

###################

###### Daniel ######

###################

###### Ryan ######

###################

###### Caio ######

###################

###### João ######

###################