'''
34. Fa¸ca um programa que leia n´umeros do usu´ario at´e digitar -1. Depois, imprima a
m´edia
'''

from functools import reduce

numeros = []
while True:
    print('---CALCULAR A MEDIA - DIGITE (-1) PARA VER A MÉDIA---')
    num = int(input('Digite um número: '))
    
    if num == -1:
        break
    
    numeros.append(num)

media = reduce(lambda x, y: x + y, numeros) / len(numeros)

print(f'A média é {media}')
