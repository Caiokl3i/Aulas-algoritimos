# chamando funções dentro de funções


def x(a, b, c):
    result = c * x1(a, b)
    return result

def x1(a1, b2):
    result = b2 ** 0.5 - x2(a1)
    return result

def x2(c1):
    y = 2
    return y

print(x(1, 1, 1))