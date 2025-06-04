# f) Ler dois valores maiores que zero para as variáveis A e B, efetuar a troca dos conteúdos 
# de forma que a variável A passe a ter o conteúdo da variável B e vice-versa. Utilize 1 variável AUX para resolver.

a = int(input("Type the value of A: "))
b = int(input("Type the value of B: "))
aux = 0

print(F"Valor de A: {a}")
print(F"Valor de B: {b}")
print("")

aux = a
a = b
b = aux

print(F"Valor de A: {a}")
print(F"Valor de B: {b}")