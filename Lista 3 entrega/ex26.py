'''
26. Inverta os elementos de uma lista sem usar o m´etodo reverse.
'''

lista = [1, 2, 3, 4, 5, 6]
reverse = []

for item in lista:
    reverse.insert(0, item)

print(reverse)

