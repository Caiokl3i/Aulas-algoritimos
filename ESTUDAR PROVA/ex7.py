numeros = [1, 2, 3, 4, 5, 6]
# ➤ Resultado: [2, 4, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)