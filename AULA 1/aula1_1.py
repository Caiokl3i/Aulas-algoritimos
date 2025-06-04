x = 9
raiz_x = x ** 2

#1 - Ler o valor de 2 lados de um triângulo retângulo, calcular hipotenusa (h).

a1 = float(input('Digite um valor: '))
a2 = float(input('Digite um valor: '))
h = (a1 ** 2 + a2 ** 2) ** (1 / 2)

print(f'O valor da hipotenusa é: {h:.2f}')

#2 - Calcular a raiz cúbica de X da expressão abaixo.
#x = ((raiz(y) + a/3)/raiz(b/2a)

a = int(input('Digite o lado a do triângulo: '))
b = int(input('Digite o lado b do triângulo: '))
h = (a1 ** 2 + a2 ** 2) ** 0.5

print(f'Hipotenusa = {h}')
y = int(input('Digite o valor de y: '))

x = ((y ** 0.5) + (a / 3) / (b / 2 * a)) ** 0.5
raiz_c_x = x ** 1/3