'''
22. Crie uma fun¸c˜ao que recebe uma lista e retorna uma nova lista com apenas os
elementos ´unicos
'''

numeros = [1, 1, 2, 3, 4, 4, 4,]


def unicos(lista):
    rep = []
    for item in lista:
        if lista.count(item) == 1:
            rep.append(item)
    return rep

numUnicos = unicos(numeros)

print(numUnicos)