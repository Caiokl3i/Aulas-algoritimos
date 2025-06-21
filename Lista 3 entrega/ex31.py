'''
31. Crie uma fun¸c˜ao que verifique se uma lista est´a ordenada.
'''

lista = [1, 2, 5, 3, 8, 9, 3, 4, 5, 7]
ordenada = sorted(lista)

if lista == ordenada:
    print('A lista está ordenada')
else:
    print('A lista não está ordenada')

