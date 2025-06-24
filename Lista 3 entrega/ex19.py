'''
19. Solicite nomes at´e que o usu´ario digite ”sair”. Armazene em uma lista e imprima.
'''

nomes = []

while True:
    nome = input("Digite um nome ou 'sair' para encerrar: ").strip()
    if nome == '':
        print('Entrada vazia')
        continue
    elif nome.lower() == "sair":
        break
    nomes.append(nome)

print(nomes)