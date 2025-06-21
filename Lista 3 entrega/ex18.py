'''
18. Verifique se o n´umero 7 est´a presente na lista [3, 6, 9, 12].
'''

lista = [3, 6, 9, 12]

for i, item in enumerate(lista):
    if item == 7:
        print(f"O numero 7 está na posição {i + 1}")
    else:
        print(f'Não tem o numero 7')