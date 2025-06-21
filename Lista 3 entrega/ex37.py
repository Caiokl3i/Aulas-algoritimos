'''
37. Crie uma lista de palavras e remova as que tiverem menos de 4 letras.
'''

words = ['caio', 'ana', 'cris', 'curso', 'bia', 'rodrigo']

words = list(filter(lambda x: len(x) >= 4, words)) 
# posso tanto atualizar a lista que ja existe, quanto criar uma nova filtrada

print(words)

