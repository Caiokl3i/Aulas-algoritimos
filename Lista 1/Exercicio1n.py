# # n) Colocar três valores em ordem crescente.

n1 = float(input("Type number 1: "))
n2 = float(input("Type number 2: "))
n3 = float(input("Type number 3: "))

num1 = 0
num2 = 0
num3 = 0

if n1 > n2 and n1 > n3:
    num3 += n1
elif n2 > n1 and n2 > n3:
    num3 += n2
elif n3 > n2 and n3 > n1:
    num3 += n3

if n1 > n2 and n1 < n3:
    num2 += n1
elif n2 > n1 and n2 < n3:
    num2 += n2
elif n2 < n1 and n2 > n3:
    num2 += n2
elif n3 > n2 and n3 < n1:
    num2 += n3

if n1 < n2 and n1 < n3:
    num1 += n1
elif n2 < n1 and n2 < n3:
    num1 += n2
elif n3 < n2 and n3 < n1:
    num1 += n3

if n1 == n2 and n1 == n3:
    num1 += n1
    num2 += n2
    num3 += n3
elif n2 == n1 and n2 < n3:
    num1 += n1
    num2 += n2
elif n3 == n2 and n3 < n1:
    num1 += n3
    num2 += n2
elif n3 == n1 and n3 < n2:
    num1 += n3
    num2 += n1
elif n2 == n1 and n2 > n3:
    num2 += n1
    num3 += n2
elif n3 == n2 and n3 > n1:
    num2 += n3
    num3 += n2
elif n3 == n1 and n3 > n2:
    num2 += n3
    num3 += n1

print(f"Numeros em ordem crescente: {num1:.0f} {num2:.0f} {num3:.0f}")

# # ou poderia fazer tbm:

# # n) Colocar três valores em ordem crescente.

# n1 = float(input("Type number 1: "))
# n2 = float(input("Type number 2: "))
# n3 = float(input("Type number 3: "))

# if n1 > n2:
#     n1, n2 = n2, n1
# if n2 > n3:
#     n2, n3 = n3, n2
# if n1 > n2:
#     n1, n2 = n2, n1

# print(f"Numeros em ordem crescente: {n1:.0f} {n2:.0f} {n3:.0f}")