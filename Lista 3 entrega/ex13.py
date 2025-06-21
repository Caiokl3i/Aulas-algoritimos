'''
13. Crie uma lista com os n´umeros de 1 a 10 usando range() e imprima somente os
pares.
'''

lista = []
pares = []

for i in range(0, 11):
    lista.append(int(i))

for item in lista:
    if item % 2 == 0:
        pares.append(item)

print(pares)

