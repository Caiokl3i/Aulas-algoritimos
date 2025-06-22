'''
71. Fa¸ca uma fun¸c˜ao que receba um dicion´ario com tuplas como valores e retorne a
soma de todos os n´umeros nas tuplas.
'''

from functools import reduce

dicionario = {
    'Caio': (1, 2),
    'Ana': (3, 4),
    'Victor': (5, 6)
}

def soma_cada_tupla(dic):
    for chave, valor in dic.items():
        print(f'A soma do(a) {chave} é: {reduce(lambda x, y: x + y, valor)}')

def soma_total_tuplas(dic):
    numeros = []
    for valor in dic.values():
        numeros.extend(valor)
    return reduce(lambda x, y: x + y, numeros)

soma_cada_tupla(dicionario)

print(f'A soma de todos os valores de todas as tuplas é {soma_total_tuplas(dicionario)}')