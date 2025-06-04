
n = int(input("Digite um numero: "))

soma = 0

for i in range(n):
    if i % 2 == 1:
        print(f"{i}")
        soma += i
print(f"Soma = {soma}")

