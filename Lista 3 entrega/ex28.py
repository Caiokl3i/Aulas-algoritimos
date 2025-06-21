'''
28. Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos
'''

lista = [1, 2, 3, 4]

def soma(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

print(soma(lista))

# RECURSÂO

# def soma(lista):
#     if len(lista) == 0:
#         return 0 
    
#     return lista[0] + soma(lista[1:])

# print(soma(lista))