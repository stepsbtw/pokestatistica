import pulp

# Tipos de Pokémon
tipos = ["Normal", "Fogo", "Água", "Elétrico", "Planta", "Gelo" ,"Lutador", "Veneno", "Terra", "Voador", "Psíquico", "Inseto", "Pedra" ,"Fantasma", "Dragão", "Sombrio", "Aço", "Fada"]

# Matriz de fraquezas: 1 significa que o tipo é fraco contra outro tipo
fraquezas = [[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
             [0,    0,    0,    0,    1,    1,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    1,    0],
             [0,    1,    0,    0,    0,    0,    0,    0,    1,    0,    0,    0,    1,    0,    0,    0,    0,    0],
             [0,    0,    1,    0,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    0,    0],
             [0,    0,    1,    0,    0,    0,    0,    0,    1,    0,    0,    0,    1,    0,    0,    0,    0,    0],
             [0,    0,    0,    0,    1,    0,    0,    0,    1,    1,    0,    0,    0,    0,    1,    0,    0,    0],
             [1,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    1,    0,    0,    1,    1,    0],
             [0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1],
             [0,    1,    0,    1,    0,    0,    0,    1,    0,    0,    0,    0,    1,    0,    0,    0,    1,    0],
             [0,    0,    0,    0,    1,    0,    1,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0],
             [0,    0,    0,    0,    0,    0,    1,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
             [0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    1,    0,    0],
             [0,    1,    0,    0,    0,    1,    0,    0,    0,    1,    0,    1,    0,    0,    0,    0,    0,    0],
             [0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    0,    0,    1,    0,    0,    0,    0],
             [0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    0,    0,    0],
             [0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    0,    0,    1,    0,    0,    0,    0],
             [0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    1],
             [0,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    0,    1,    1,    0,    0]]

prob = pulp.LpProblem("Pokemon", pulp.LpMinimize)

x_i = []
for i in range(18):
    x_i.append(pulp.LpVariable(tipos[i], 0, 1, pulp.LpInteger))

obj = 0
for i in range(0, 18):
    for j in range(0, 18):
        obj += x_i[i]*fraquezas[j][i]

prob += obj, "total fraquezas"

res = 0
for i in range(18):
    res += x_i[i]
prob += res == 6

prob.writeLP("Pokemon.lp")

prob.solve()

print("Status:", pulp.LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost = ", pulp.value(prob.objective))