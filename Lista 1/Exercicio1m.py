# m) Obter, dentre cinco números, a média dos impares

n1 = float(input("Type number 1: "))
n2 = float(input("Type number 2: "))
n3 = float(input("Type number 3: "))
n4 = float(input("Type number 4: "))
n5 = float(input("Type number 5: "))

soma_numeros = 0
i = 0

if not n1 % 2 == 0:
    soma_numeros += n1
    i += 1
if not n2 % 2 == 0:
    soma_numeros += n2
    i += 1
if not n3 % 2 == 0:
    soma_numeros += n3
    i += 1
if not n4 % 2 == 0:
    soma_numeros += n4
    i += 1
if not n5 % 2 == 0:
    soma_numeros += n5
    i += 1

if i == 0:
    print("There isnt any impar number")
else:
    media = soma_numeros / i
    print(f"Essa é a media {media:.2f}")