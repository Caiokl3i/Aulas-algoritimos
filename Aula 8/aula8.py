'''lista = [1,2,3,4,5]

quadrado = [num**2 for num in lista]

pares = [x for x in lista if x % 2 == 0]

print(quadrado)'''

# --------------------------------------------------------
# Função

def soma(x, y):
    # pass não executar a função
    # soma = x + y -> não declarar muita variavel
    return x + y

def subtracao(x, y):
    # pass não executar a função
    return x - y

def divisao(x, y):
    # pass não executar a função
    return x / y

def multiplicacao(x, y):
    # pass não executar a função
    return x * y

def potencia(x, y):
    # pass não executar a função
    return x ** y

n1 = 2
n2 = 3

soma = soma(n1, n2)
subtracao = subtracao(n1, n2)
divisao = divisao(n1, n2)
multiplicacao = multiplicacao(n1, n2)
potencia = potencia(n1, n2)

print(soma)
print(subtracao)
print(divisao)
print(multiplicacao)
print(potencia)
