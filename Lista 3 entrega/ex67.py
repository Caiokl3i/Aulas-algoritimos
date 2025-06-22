'''
67. Crie um sistema de agenda onde cada contato ´e uma chave e o valor ´e uma lista de
telefones.
'''

contacts_list = {}

while True:
    nome = input('Digite o nome do contato ou (sair) para: \n')
    if nome.lower() == 'sair':
        break
    numeros = []
    while True:
        numero = int(input('Digite o numero de telefone: \n'))
        
        numeros.append(numero)
        
        escolha = input('Adicionar outro número para contato? (sim) ou (não) \n')
        if escolha.lower() == 'não' or escolha.lower() == 'nao':
            break
    
    contacts_list[nome] = numeros

for chave, valor in contacts_list.items():
    print(f'{chave} : {valor}')