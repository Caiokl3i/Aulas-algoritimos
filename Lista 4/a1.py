from functools import reduce

'''
Exercício prático:
Crie uma função chamada mostrar_maiores que:

Recebe uma quantidade variável de números com *args

Imprime somente os que forem maiores que 10
'''

# def maior_10(*num):
#     for n in num:
#         print(f'{n} é maior que 10' if n > 10 else f'{n} não é maior que 10')

# maior_10(10, 48, 534, 3, 4, 5, 665, 7, 65)


# -------------------------------------------------------------------------------

'''
A1. Soma com *args
Escreva uma fun¸c˜ao que aceita qualquer quantidade de argumentos num´ericos e
retorna a soma deles.
'''

numeros = [1, 2, 3, 4]

def soma(*num):
    soma = [n for n in num]
    soma = reduce(lambda x, y: x + y, soma)
    return soma

print(f'A soma é {soma(*numeros)}')