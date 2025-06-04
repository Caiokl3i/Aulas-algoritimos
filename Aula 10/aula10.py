import math

dobro = lambda x: x * 2

print('Exemplo - 1 dobro de 5', dobro(5))

soma = lambda x, y: x + y
print('Exemplo - 2 Soma de 3 e 4', soma(3, 4))


hipo = lambda a, b: math.sqrt(a**2 + b**2)

# filter filtra a lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filter(lambda x: x % 2 == 0, numeros)
print('Exemplo - 3 Numeros pares', list(pares))

'''
gere 100 num rand (20 a 100), filtrar > 60
gere 100 num rand (20 a 100), filtrar > media
gere 100 num rand (20 a 100), filtrar < 25
'''

import random

lista = []

for _ in range(101):
    lista.append(random.randint(20, 100))

print(lista)

menor_60 = filter(lambda x: x < 60, lista)

print('Menor que 60 : ',  list(menor_60))

# map retorna uma lista

quadrado = list(map(lambda x: x ** 2, numeros))

# sorted(pessoas )
pessoas = [('ana', 19), ('joao', 30), ('maria', 20)]



