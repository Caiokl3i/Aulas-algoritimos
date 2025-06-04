# o) Dadas três medidas, verificar se elas podem ser os comprimentos dos lados de
# um triângulo, se forem, verificar se é eqüilátero (todos lados iguais), isósceles
# (dois lados iguais) ou escaleno (todos lados diferentes). Um triângulo é uma figura
# geométrica fechada de três lados, em que cada um é menor que a soma dos
# outros dois.

n1 = float(input("Type side 1: "))
n2 = float(input("Type side 2: "))
n3 = float(input("Type side 3: "))

if n1 < 0 or n2 < 0 or n3 < 0:
    print("Não é um comprimento de um retangulo")
elif n1 == n2 and n2 == n3 and n3 == n1:
    print("Esse é um triangulo equilatero")
elif n1 == n2 or n2 == n3 or n3 == n1:
    print("Esse é um triangulo isóceles")
else:
    print("Esse é um triangulo escaleno")