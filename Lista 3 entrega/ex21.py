'''
21. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros
pares usando remove.
'''

numeros = []

while len(numeros) < 10:
    try:
        n = int(input(f'Digite o {len(numeros) + 1}° numero: '))
        numeros.append(n)
    except ValueError:
        print('⚠️ Entrada inválida! Digite um número inteiro.')

for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)

print(numeros)