# k) Determinar as raizes reais de uma equação do 2o grau (Ax2+Bx+C=0).

a = float(input("Type number A: "))
b = float(input("Type number B: "))
c = float(input("Type number C: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print(f"Delta = {delta:.2f}")
    print("Não tem raiz real")
elif a == 0 or c == 0 or c == 0:
    print("A, B ou C deve ser maior que 0")
else:
    print(f"Delta = {delta}")

    raiz_de_delta  = delta ** 0.5

    x1 =  ((-b) + raiz_de_delta) / (2 * (a))

    print(f"X1 = {x1}")

    x2 =  ((-b) - raiz_de_delta) / (2 * (a))

    print(f"X2 = {x2}")

    print(f"Results: x1 = {x1} and x2 = {x2}")