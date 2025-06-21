'''
33. Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3.
'''

numeros = [i for i in range(1, 101)]

multiplos = list(filter(lambda x: x % 3 == 0, numeros))

print(multiplos)

# APENAS LIST COMPREHENSION

# multiplos3 = [i for i in range(1, 101) if i %3 == 0]

# print(multiplos3)