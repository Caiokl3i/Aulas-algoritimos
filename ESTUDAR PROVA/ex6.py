nums = [1, 2, 3, 4]
# ➤ Saída esperada: [1, 4, 9, 16]

quadrado = [n * n for n in nums]

quadrado2 = list(map(lambda x: x * x, nums))

print(quadrado)
print(quadrado2)