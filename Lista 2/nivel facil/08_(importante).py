n = int(input("Digite um numero: "))
limit = 0

for j in range(n): # Esse for faz as linhas se repetirem 5 vezes

    for i in range(j + 1 ):         # Essa parte faz os numeros 
        limit += 1                  # ficarem repretindo em linha 
        print(f"{limit}" ,end="")   # ex 12345

    limit = 0 
    print()