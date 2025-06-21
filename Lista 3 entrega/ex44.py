'''
44. Divida uma lista em N sublistas de tamanho igual
'''

lista = [1, 2, 3, 4, 5, 6]

new_list = list(map(lambda x: list(x), lista))

print(new_list)