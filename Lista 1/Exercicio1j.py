# j) Tendo como dados de entrada a altura e o sexo de uma pessoa, calcular seu peso ideal, utilizando as seguintes fórmulas:

# -para homens: (72.7*H)-58;

# - para mulheres: (62.1*H)-44,7.

h = float(input("Type a height: "))
sexo = str(input("type your sexo: ")).lower()  # .lower and .upper

if sexo ==  "male":
    peso_ideal = (72.7 * h) - 58;
    print(f"{peso_ideal:.2f}")
elif sexo ==  "female":
    peso_ideal = (62.1 * h) - 44.7
    print(f"{peso_ideal:.2f}")
else:
    print("O sexo nao corresponde a masculino nem feminino")