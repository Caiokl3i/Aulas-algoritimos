'''
12. Leia 5 n´umeros do usu´ario e verifique se cada um deles ´e maior que 10.
'''

lista = []

for i in range(5):
    num = input("Digite um numero: ")
    lista.append(int(num))

counter = 0

for item in lista:
    if item > 10:
        print(f"{lista[counter]} é maior que 10")
    else:
        print(f"{lista[counter]} não é maior que 10")
    counter += 1