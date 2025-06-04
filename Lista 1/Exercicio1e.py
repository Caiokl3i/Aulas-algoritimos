# e) Calcular o valor do salário liquido de um programador, dado o número funções criadas, o valor de cada função,
# o percentual de desconto do INSS é 8% sobre o salário bruto. Deverá ser informado o nome do funcionário, o salário bruto,
# 0 salario liquido. Validar os valores de entrada.

name = str(input("Type your name: "))

functions = int(input("Type the number of functions: "))
while functions < 0:
    functions = int(input("Type the number of functions: "))

f_value = float(input("Type the value of functions: "))
while functions < 0:
    f_value = float(input("Type the value of functions: "))

salario_bruto = functions * f_value
salario_liquid = (functions * f_value) * 0.92

print(f"Name: {name}")
print(f"salario bruto: {salario_bruto:.2f}")
print(f"Salario liquido: {salario_liquid:.2f}")

    