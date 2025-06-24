'''
75. Armazene dados de uma enquete com tuplas (nome, voto) em uma lista e conte
os votos usando um dicion´ario
'''

candidatos = {
    35: 'MIGUEL',
    45: 'VICTOR',
    18: 'MARIA',
}

contagem = {
    'MIGUEL': 0,
    'VICTOR': 0,
    'MARIA': 0
}

nome = input('Digite seu nome: ')
voto = int(input('Digite o n° do seu candidato: '))

enquete = []
enquete.append((nome, voto))

