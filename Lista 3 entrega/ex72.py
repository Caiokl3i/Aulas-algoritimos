'''
72. Dado um dicion´ario de alunos (chave = nome, valor = tupla de notas), imprima
apenas os aprovados (m´edia >= 7).
'''

from functools import reduce

alunos = {
    'Caio': (6, 6),
    'Victor': (7, 7),
    'Valentim': (8, 10)
}

for chave, valor in alunos.items():
    media = reduce(lambda x, y: x + y, valor) / len(valor)
    if media >= 7:
        print(f'O aluno {chave} está aprovado com media {media}')