# map filter REDUCE

from functools import reduce

'''
sintexe
reduce(func, array)
'''

numeros = {1, 2, 3, 4, 5, 6}
soma_total = reduce(lambda x, y: x + y, numeros)

import random

numeros = [random.randint(1, 500) for _ in range(10)]

print(numeros)

maior_num = reduce(lambda x, y: x if x > y else y, numeros)

print(maior_num)

# ------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media = reduce(lambda x, y: x + y, list(map(lambda x: x ** 2,
                    filter(lambda x: x % 2 == 0, numeros)))) / len(list(map(lambda x: x ** 2,
                        filter(lambda x: x % 2 == 0, numeros))))
print(media)

# ------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maior = reduce(lambda x, y: x if x > y else y,
            filter(lambda x: x % 2 == 1,
                list(map(lambda x: x ** 3, numeros))))
print(maior)

# ------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = reduce(lambda x, y: x + y,
                list(map(lambda x: x ** 2,
                    filter(lambda x: x % 3 == 0, numeros))))
print(soma)

# ===========================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = reduce(lambda x, y: x + y,
              list(map(lambda x: x ** 3, 
                    list(filter(lambda x: x if x < reduce(lambda x, y: x + y, numeros) / len(numeros) else None, numeros)))))
print(soma)