z = float(input("Valor de Z: "))
w = float(input("Valor de W: "))

x = 0
t = 0

if w > 0 or z < 7:
    x = (5 * w + 1) / 3
    t = (5 * z + 2)
else:
    x = (5 * z + 2)
    t = (5 * w + 1) / 3

y = (7 * x * 2 - 3 * x - 8 * t) / (5 * (x + 1))

print("O valor de Y é: ", y)

# TESTAR !!!!!!!!!