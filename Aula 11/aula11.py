# # map filter REDUCE

from functools import reduce

# '''
# sintexe
# reduce(func, array)
# '''

# numeros = {1, 2, 3, 4, 5, 6}
# soma_total = reduce(lambda x, y: x + y, numeros)

# import random

# numeros = [random.randint(1, 500) for _ in range(10)]

# print(numeros)

# maior_num = reduce(lambda x, y: x if x > y else y, numeros)

# print(maior_num)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = filter(lambda x: x % 2 == 0, numeros)

# quadrado = list(map(lambda x: x ** 2, numeros))

# media = sum(quadrado) / len(quadrado)

# print(media)

# ------------------------------------

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# cubico = list(map(lambda x: x ** 3, numeros))

# impar = filter(lambda x: x % 2 == 1, cubico)

# maior = reduce(lambda x, y: x if x > y else y, impar)

# print(maior)

# ------------------------------------------

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# multiplos_3 = filter(lambda x: x % 3 == 0, numeros)

# quadrado = list(map(lambda x: x ** 2, multiplos_3))

# soma = reduce(lambda x, y: x + y, quadrado)

# print(soma)

# ===========================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = reduce(lambda x, y: x + y,
              list(map(lambda x: x ** 3, 
                    list(filter(lambda x: x if x < reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) / len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) else None, numeros)))))

print(soma)