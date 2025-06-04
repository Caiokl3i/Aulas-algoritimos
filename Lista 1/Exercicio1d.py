
# d) Calcular a área de uma circunferência e mostrá-la. Fórmula Area RAIO2. O valor do raio não poderá ser negativo ou zero.

import math

r = float(input("Type the number of the raio: "))

while r <= 0:
    print("The number can not be negative or zero")
    r = float(input("Type the number of the raio: "))

area = math.pi * (r ** 2)

print(f"Area is iqual = {area:.1f}")


