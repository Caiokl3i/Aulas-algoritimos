'''
42. Dada uma lista de inteiros, crie uma fun¸c˜ao que identifique os n´umeros que aparecem
mais de uma vez e quantas vezes cada um aparece.
'''
from collections import Counter

inteiros = [1, 3, 3, 3, 4, 4, 5,]

def repetidos(lista):
    qtde = dict(Counter(lista))
    # {1: 1, 4: 6, 6: 2, 5: 3, 3: 3, 2: 2, 7: 1}
    
    for chave, valor in qtde.items():
        if valor > 1:
            print(f'O numero {chave} repete {valor} vezes')

repetidos(inteiros)