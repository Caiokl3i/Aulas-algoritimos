'''
32. Dada uma lista de nomes, retorne uma nova lista com os nomes em letras mai´usculas.
'''

strings = ['caio', 'ana', 'cris', 'curso']

upper = list(map(lambda x: x.upper(), strings))

print(upper)