'''
64. Crie um dicion´ario que mapeia n´umeros de 1 a 5 para seus quadrados, usando la¸co
for.
'''

numeros = [1, 2, 3, 4, 5, 6]
n_mapeados = {}

for n in numeros:
    n_mapeados[n] = n**2

# dict comprehension

n_mapeados = {n: n**2 for n in numeros}

print(n_mapeados)