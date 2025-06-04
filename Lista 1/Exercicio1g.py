# g) Determinar se um aluno esta ou não aprovado, conhecidas as notas dos quatro bimestres, sendo a média de aprovação igual a 6,0.

n1 = float(input("Type the grade 1: "))
while n1 < 0:
    print("It can not be negative")
    n1 = float(input("Type the grade 1: "))

n2 = float(input("Type the grade 2: "))
while n2 < 0:
    print("It can not be negative")
    n2 = float(input("Type the grade 2: "))

n3 = float(input("Type the grade 3: "))
while n3 < 0:
    print("It can not be negative")
    n3 = float(input("Type the grade 3: "))

n4 = float(input("Type the grade 4: "))
while n4 < 0:
    print("It can not be negative")
    n4 = float(input("Type the grade 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print(f"Student approved with average {media}")
else:
    print(f"Student failed with average {media}")