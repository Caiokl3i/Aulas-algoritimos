'''
45. Fa¸ca uma fun¸c˜ao que receba uma lista de listas e retorne uma lista ”achatada”(flatten).
'''

from functools import reduce

# reduce

numeros = [[1, 2], [3, 4], [5, 6]]

flatten = reduce(lambda x, y: x + y, numeros)

print(flatten)

# list comprehension

lista = [sub for lista in numeros for sub in lista]

print(lista)

# recursão - estudar mais recursão 

numeros = [[1, 2], [3, 4], [5, 6]]

def flatten(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(flatten(item))
        else:
            resultado.append(item)
            
    return resultado

print(flatten(numeros))