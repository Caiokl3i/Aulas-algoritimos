from functools import reduce

def maior_valor(*args):
    # ➤ A função deve imprimir o maior número passado
    return reduce(lambda x, y: x if x > y else y, args)

print(maior_valor(1, 10, 4, 5, 6))