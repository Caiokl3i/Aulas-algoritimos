# testar estruturas condicionais
# criar um programa que leia o salário de um funcionårio e calcule o aumento
# salário for maior que 1000, o aumento é de 10% + bonus de 3% se carga horaria > 45
# se o salário for menor que 1000, o aumento é de 15% + bonus de 5% se carga horaria > 40
# mostrar o salário final


salario = float(input('Digite o valor do salario: '))
carga_horaria = float(input('Digite a carga horaria do mes: '))


if salario < 1000:
    novo_salario = salario * 1.15
    if carga_horaria > 40:
        bonus = novo_salario * 1.05
        print(f'Aumento de 15% no salario + bonus: Novo salario = {novo_salario + bonus}')
    else:
        print(f'Aumento de 15% no salario: Novo salario = {novo_salario}')
else:
    novo_salario = salario * 1.10
    if salario > 45:
        bonus = novo_salario * 1.03
        print(f'Aumento de 10% no salario: Novo salario = {novo_salario + bonus}')
    else:
        print(f'Aumento de 10% no salario: Novo salario = {novo_salario}')
        