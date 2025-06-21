'''
39. Fa¸ca a uni˜ao de duas listas sem usar o operador +
'''

lista1 = [1, 2, 3, 4]

lista2 = [3, 4, 4, 8, 9, 2, 4, 3, 6]

lista1.extend(lista2)
lista1.sort()

print(list(set(lista1)))
