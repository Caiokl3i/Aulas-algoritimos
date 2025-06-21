'''
6. Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o
maior e o menor n´umero.
'''

lista = []

for _ in range(5):
    num = int(input("Digite um numero:"))
    lista.append(num)

print(lista)
print(f"maior: {max(lista)}")
print(f"menor: {min(lista)}")