'''
38. Implemente uma fun¸c˜ao que receba uma lista e retorne os elementos na ordem
inversa.
'''

itens = ['Abacaxi', 42, True, 3.14, 'Caderno', False, 'Python', 7, None, 'Bicicleta']

# usando slice
def reverse1(lista):
    return lista[::-1]

print(reverse1(itens))

# usando reversed
def reverse2(lista):
    reverso = list(reversed(lista))
    return reverso

print(reverse2(itens))

# usando reverse
def reverse3(lista):
    lista.reverse()
    return lista

print(reverse3(itens))

