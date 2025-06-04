n = int(input("Digite um número: "))

for j in range(1, 6):
    for i in range(1, n + 1):
        print(f"{i}" ,end="")
    n = n - 1
    print("")