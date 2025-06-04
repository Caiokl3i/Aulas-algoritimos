n = int(input("Digite um numero de 0 a 10: "))
while n < 1 or n > 10:
    print("NUMERO INVALIDO")
    n = int(input("Digite um numero de 0 a 10: "))

mult = 0

for i in range(1, n + 1):
    mult = n * i
    print(f"{n} x {i} = {mult}")

