'''
30. Dada uma lista de strings, crie uma nova lista com o tamanho (n´umero de caracteres)
de cada string.
'''

strings = ['caio', 'ana', 'cris', 'curso']

# num_strings = []

# for item in strings:
#     soma = 0 
#     for letters in item:
#         soma += 1
#     num_strings.append(soma)

# print(num_strings)

num_strings = [len(w) for w in strings]

print(num_strings)
