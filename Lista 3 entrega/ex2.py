'''
2. Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha.
'''

nomes = []

for _ in range(1, 6):
    nome = str(input("Digite o nome: "))
    nomes.append(nome)

print(nomes)