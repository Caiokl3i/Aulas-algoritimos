'''
24. Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.
'''
ramdom = [1, 5, 7, 6, 3, -1, 7, 8, 5, 32, 2, 1, 2, 4, 6, 5, 6, 8, 0, 10]
pares = []
impares = []

for item in ramdom:
    if item %2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(f'Numeros pares: {pares}')
print(f'NUmeros impares: {impares}')