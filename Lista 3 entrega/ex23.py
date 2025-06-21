'''
23. Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem.
'''

duplicados = ['caio', 'caio', 'victor', 'santos', 'santos']

ordem = []

for item in duplicados:
    if item not in ordem:
        ordem.append(item)

print(ordem)