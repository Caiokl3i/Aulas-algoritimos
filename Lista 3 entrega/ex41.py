'''
41. Crie uma fun¸c˜ao que compare duas listas e retorne os elementos que est˜ao em ambas
(interse¸c˜ao).
'''

lista1 = [1, 3, 5, 6, 7, 9]

lista2 = [1, 2, 4, 5, 6, 8]

intersecção = list(filter(lambda x: x in lista2, lista1))

print(intersecção)