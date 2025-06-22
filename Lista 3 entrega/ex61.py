'''
61. Crie um dicion´ario onde as chaves s˜ao nomes de pessoas e os valores s˜ao listas com
trˆes notas. Calcule a m´edia de cada aluno.
'''

pessoas = {
    'Caio': [10, 6, 8],
    'Ana': [4, 6, 9],
    'Vitor': [3, 5, 1]
}

for chave, valor in pessoas.items():
    media = sum(valor) / len(valor)
    print(f'A média do(a) aluno(a) {chave} é: {media:.2f}')