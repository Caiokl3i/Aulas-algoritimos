'''
65. Fa¸ca um programa que recebe nomes de alunos e suas idades. Armazene usando
uma lista de tuplas e depois transforme em dicion´ario.
'''

pessoas = []


while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade: "))
    
    pessoa = (nome, idade)
    pessoas.append(pessoa)
    
dict_pessoas = dict(pessoas)
print(dict_pessoas)
