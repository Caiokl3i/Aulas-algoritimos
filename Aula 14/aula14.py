# def minhafuncao(a, b, *args):
#     print(f'Argumentos revebidos: {args}')
    
#     for arg in args:
#         print(f'- {arg}')

# função para contar o num de siblistas em uma lista (otilizar isinstance)

def count_sublistas(*args):
    contador = 0
    for item in args:
        # if isinstance(item, list):
        # Significa: Se o item é uma lista, faça algo.
        if isinstance(item, list):
            contador += 1
    return contador

'''

print(isinstance(10, int))          # True, porque 10 é inteiro
print(isinstance("Caio", str))      # True, é string
print(isinstance([1, 2, 3], list))  # True, é lista
print(isinstance(3.14, float))      # True, é float
print(isinstance(10, float))        # False, 10 é int, não float

print(isinstance(10, (int, float)))         # True, porque 10 é int
print(isinstance(3.14, (int, float)))       # True, porque 3.14 é float
print(isinstance("texto", (int, float)))    # False, não é nenhum dos dois

'''

def contar_sublistas(colecao):
    contador = 0
    for item in colecao:
        if isinstance(item, list):
            contador += 1
            contador += contar_sublistas(item)
    return contador

tupla = (2, 3, 4, 5, [1, 2, 3], [1, 2, [1, 2, 3]])

total_sublistas = contar_sublistas(tupla)
print(f"O número total de sublistas (incluindo as aninhadas) é: {total_sublistas}")

# reduce
from functools import reduce

def contar_sublistas_reduce(*args):
    return reduce(lambda count, item: count + 
                (1 if isinstance(item, list) else 0), args, 0)

# parametros nomeados 

def soma(a, b, c):
    pass

soma(b = 1, c = 4, a = 8)

def funcao_completa(param_obg, *args, **kwargs):
    print(f'parametro obrigatorio: {param_obg}')
    print(f'args extras: {args}')
    print(f'kwargs: {kwargs}')

# ecemplo de uso
funcao_completa('valor1', 'extra1', 'extra2', nome='caio', idade=19)

'''
implemente calculadora que faça 2 tipos (soma, multi), lista de numeros
exibir_detalhes=True
'''