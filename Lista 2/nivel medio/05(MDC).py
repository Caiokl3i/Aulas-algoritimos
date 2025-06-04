n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

ofc_n1 = n1
ofc_n2 = n2

mdc = 1

for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
    while True:
        if n1 % i == 0 and n2 % i == 0:
            n1 = n1 / i
            n2 = n2 / i
            mdc *= i
        elif n1 % i == 0 and n2 % i != 0:
            n1 = n1 / i
        elif n1 % i != 0 and n2 % i == 0:
            n2 = n2 / i
        else:
            break
print(f"MDC de {ofc_n1} e {ofc_n2} = {mdc}")
