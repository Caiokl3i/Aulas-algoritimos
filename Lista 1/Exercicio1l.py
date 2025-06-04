# l) Determinar, dentre quatro números, a soma dos pares.

n1 = float(input("Type number 1: "))
n2 = float(input("Type number 2: "))
n3 = float(input("Type number 3: "))
n4 = float(input("Type number 4: "))

soma_numeros = 0

if n1 % 2 == 0:
    soma_numeros = soma_numeros + n1
if n2 % 2 == 0:
    soma_numeros = soma_numeros + n2
if n3 % 2 == 0:
    soma_numeros = soma_numeros + n3
if n4 % 2 == 0:
    soma_numeros = soma_numeros + n4

print(f"A soma dos numeros pares é {soma_numeros}")