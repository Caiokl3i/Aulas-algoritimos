'''
17. Crie uma lista com 5 n´umeros e calcule a m´edia usando la¸co for.
'''

from functools import reduce
import random

numeros = [random.randint(1, 10) for _ in range(5)]

print(numeros)

media = reduce(lambda x, y: x + y, numeros) / len(numeros)

print(media)