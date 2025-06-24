'''
12. Leia 5 n´umeros do usu´ario e verifique se cada um deles ´e maior que 10.
'''

numeros = []

while len(numeros) < 5:
    try:
        valor = int(input(f'Digite o {len(numeros) + 1}° numero: '))
        numeros.append(valor)
    except ValueError:
        print('⚠️ Entrada inválida! Digite um número inteiro.')

print()

for n in numeros:
    if n > 10:
        print(f'{n} é maior que 10')
    else:
        print(f'{n} não é maior que 10')