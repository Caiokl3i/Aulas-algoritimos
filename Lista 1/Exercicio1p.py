# p) Verificar se um triângulo é retângulo, acutângulo ou obtusângulo, dadas três
# # medidas.

a = float(input("Type side 1: "))
b = float(input("Type side 2: "))
c = float(input("Type side 3: "))

while a <= 0 or b <= 0 or c <= 0:
    print("The sides must be higher than 0")
    a = float(input("Type side 1: "))
    b = float(input("Type side 2: "))
    c = float(input("Type side 3: "))

if a > b and a > c:
    hip = a
    cat_adj = b
    cat_opt = c
elif b > a and b > c:
    hip = b
    cat_adj = a
    cat_opt = c
elif c > a and c > b:
    hip = c
    cat_adj = a
    cat_opt = b

print(f"a: {hip:.0f} b: {cat_opt:.0f} c: {cat_adj:.0f}")

hip_final = (cat_adj ** 2 + cat_opt ** 2 ) ** 0.5

print(f"hip final :{hip_final:.0f} a : {hip:.0f}")

if hip_final == hip:
    print("é um triangulo retangulo")