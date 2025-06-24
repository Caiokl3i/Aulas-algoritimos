'''
2. Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha.
'''

nomes = [input('Digite um nome: ') for _  in range(5)]

print()

for nome in nomes:
    print(nome)