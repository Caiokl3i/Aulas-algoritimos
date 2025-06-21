'''
35. Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas
com mais de 18 anos.
'''

pessoas = [
    ('Ana', 20),
    ('Caio', 19),
    ('João', 15),
    ('Beatriz', 12)
]

nomes = list(map(lambda x: x[0], list(filter(lambda x: x[1] >= 18, pessoas))))

# maiores_20_anos = [pessoa[0] for pessoa in pessoas if pessoa[1] > 18]

print(f'pessoas com mais de 18 anos: ')
for nome in nomes:
    print(nome) 