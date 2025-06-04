# h) Dadas três medidas, informar a maior.

a = float(input("Type a measure: "))
b = float(input("Type another measure: "))
c = float(input("Type another measure: "))

if a > b and a > c:
    print(f"the biggest number is {a}")
elif b > a and b > c:
    print(f"the biggest number is {b}")
elif c > a and c > a:
    print(f"the biggest number is {c}")