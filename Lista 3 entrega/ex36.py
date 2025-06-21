'''
36. Crie uma fun¸c˜ao que retorne o segundo maior n´umero de uma lista.
'''

numeros = [i for i in range(1, 11)]

def segundo_maior_num(lista):
    ordenado = list(set(lista))
    ordenado = sorted(ordenado)
    return ordenado[len(ordenado) - 2]

print(segundo_maior_num(numeros))