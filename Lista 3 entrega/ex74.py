'''
74. Dado um dicion´ario que associa nomes a listas de tarefas, imprima as tarefas de um
nome espec´ıfico.
'''

tarefas = {
    'caio': ['lavar louça', 'limpar o quarto', 'lavar o banheiro'],
    'victor': ['lavar varanda', 'lavar roupas', 'fazer almoço'],
    'valentim': ['Dar ração cachorro']
}

print('Integrantes da casa: ')
for pessoa in tarefas.keys():
    print(f'{pessoa}')

nome = input('\nDigite o nome: ').lower()


if nome in tarefas:
    print(f'As tarefas do {nome} são: {tarefas[nome]}')
else:
    print('Pessoa não encontrada')