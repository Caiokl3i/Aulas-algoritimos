# # '''
# # Dicionário é uma lista de associações compostas por chave UNICA e estruturas correspondentes. Dicionarios são mutáveis

# # sintaxe basica

# # dicionario = {'a': a, 'b': b}
# # '''

# # dic = {'nome': 'caio', 'sala': 'U2'}

# # print(dic['nome']) 

# # # add novo elemento
# # dic['album'] = 'version 2.0'

# # # apagar um elemento do dicionario 
# # del dic['album']

# # item = dic.items()

# # print(item)

# # chaves = dic.keys()
# # print(chaves)

# # valores = dic.values()
# # print(valores)

# # outro ex.

# progs = {'yes': ['close to edge', 'fragile'], 'genesis': ['ada', 'alpha']}

# progs['king crimson'] = ['red', 'dicipline']

# item = progs.items()

# print(item)

# for prog in progs.items():
#     print(prog)

# if progs.has_key("king crimson"):
#     del progs['king crimson']


# Exercicio
'''
Crie um programa que leia o nome de 5 alunos e suas 4 notas
verifique qual aluno teve a maior média e mostro no final a % de alunos aprovados e reprovados
depois pedir para o usuario digitar um nome e voce fazer a busca mostrando a media do aluno
'''


alunos = {} 

for i in range(2):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    notas = []
    estatistica = {}
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    alunos[nome] = notas
    media = sum(notas) / len(notas)
    estatistica[nome] = media

print(alunos.items())
print(estatistica.items())

# terminar


'''
Funções !!!
blocos de código identificados por um nome, podem receber "paramentros"

sintaxe:
def func_soma(a, b): 
    corpo da func
'''

