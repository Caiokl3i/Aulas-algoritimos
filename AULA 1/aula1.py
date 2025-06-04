# idade = 20
# pi = 3.14
# nome = 'Léo@ifms.edu.br'
# status = True #boolean

# nota1 = input('Digite a nota 1 do aluno: ')

# print('A nota digitada foi', nota1)

# ler duas notas e efetuar as 4 operação matemáticas

# n1 = float(input('Digite a nota 1 do aluno: '))
# n2 = float(input('Digite a nota 2 do aluno: '))

# print('Resultado da soma =', n1 + n2)
# print('Resultado da sub =', n1 - n2)
# print('Resultado da mult =', n1 * n2)
# print('Resultado da div =', n1 / n2)

# print('Resultado da soma =', float(n1) + float(n2))
# print('Resultado da sub =', float(n1) + float(n2))
# print('Resultado da mult =', float(n1) + float(n2))
# print('Resultado da div =', float(n1) + float(n2))

# Ler as 4 notas de um aluno e calcular a média
# Mostrar a média no final
# Calcular também a média ponderada, onde os pesos são:
# 0.2, 0.1, 0.4, 0.3

n1 = float(input('Digite a nota 1 do aluno: '))
n2 = float(input('Digite a nota 2 do aluno: '))
n3 = float(input('Digite a nota 3 do aluno: '))
n4 = float(input('Digite a nota 4 do aluno: '))

media = (n1 + n2 + n3 + n4) / 4

print('Média do aluno:', media)

media_p = (n1 * 0.2 + n2 * 0.1 + n3 * 0.4 + n4 * 0.3) / 4

#print('Nota1:', n1, 'Nota 2:', n2, 'Nota 3:', n3, 'Nota4:', n4)
#f-string
print(f'Nota 1: {n1}, Nota 2: {n2}, Nota 3: {n3}, Nota 4: {n4}')

print('Média ponderda do aluno:', media_p)