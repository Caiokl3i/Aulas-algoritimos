'''
21. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros
pares usando remove.
'''

numeros = []

for _ in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)

print(numeros)