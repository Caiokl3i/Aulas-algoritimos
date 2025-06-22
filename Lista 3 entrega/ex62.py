'''
62. Crie uma lista de dicion´arios com nome, idade e cidade. Imprima os dados de cada
pessoa.
'''

people = [
    {
        'nome': 'Caio',
        'idade': 19,
        'cidade': 'Três Lagoas'
    },
    {
        'nome': 'Ana',
        'idade': 19,
        'cidade': 'Três Lagoas'
    },
    {
        'nome': 'Vitor',
        'idade': 15,
        'cidade': 'Dourados'
    }
]

for person in people:
    print(f'Nome: {person['nome']} \nIdade: {person['idade']} anos \nCidade: {person['cidade']}')
    print()

