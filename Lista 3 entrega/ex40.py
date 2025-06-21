'''
40. Implemente uma fun¸c˜ao que conte quantas vezes um valor aparece em uma lista
'''

from collections import Counter

numeros = [3, 4, 4, 8, 9, 2, 4, 3, 6]

def contar(lista):
    return dict(Counter(lista))

for chave, valor in contar(numeros).items():
    print(f'O número {chave} aparece {valor} vezes')