'''
Recursividade é uma técnica de programação, onde uma função (chama a si mesma) para resolver determinado problema

Principais caracteristicas:
1. Caso base: condição de parada que evita chamadas infinitas
2. Caso rescursivo: onde uma função (chama a si mesma) com um problema menor



'''

'''
x = 5 # 100000000

def fatorial(x): 
    # caso base
    if x == 0 or x == 1:
        return 1
    
    # caso recursivo
    return x * fatorial(x - 1)

print(fatorial(x))

# arvores binarias de buscas
# ordenação bubble sort (n ** 2)

'''



def fibonacci(x):
    if x == 0 :
        return 0
    elif x == 1 :
        return 1

    return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(8))



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def soma(x):
    if x >= 10:
        return 0
    print(x)
    return numeros[x] + soma(x + 1)

print(soma(0))

print(sum(numeros))