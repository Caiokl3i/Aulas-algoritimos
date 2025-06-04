n = int(input("Digite um numero: "))

fat = 1


for i in range(1, n + 1):
    fat *= i
print(f"fatorial {fat}")
