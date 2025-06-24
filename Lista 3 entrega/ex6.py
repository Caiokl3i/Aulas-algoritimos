'''
6. Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o
maior e o menor n´umero.
'''

lista = [int(input('Digite um numero: ')) for _ in range(5)]


print(lista)
print(f"maior: {max(lista)}")
print(f"menor: {min(lista)}")