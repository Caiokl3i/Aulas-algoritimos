'''
70. Crie um dicion´ario que associa cada letra de uma palavra `a sua posi¸c˜ao
'''

associate = {}

palavra = 'Vanuza'

for i, letra in enumerate(palavra.upper()):
    if letra in associate:
        associate[letra].append(i + 1)
    else:
        associate[letra] = [i + 1]
        # já cria como uma lista para não sobreecrever o valor da mesma chave

for chave, valor in associate.items():
    print(f'A letra {chave} está na posição {valor}')