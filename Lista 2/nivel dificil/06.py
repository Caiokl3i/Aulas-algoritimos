n = 4 #int(input("Digite um numero: "))
limit = 0

for j in range(1, n + 1):
    for i in range(1, n):
        print(" " ,end="")
    n -= 1
    for i in range(1, j + 1):
        print(f"{i}" ,end="")
    for i in range(limit, 0, -1):
        print(f"{i}" ,end="")
    limit += 1
    print()