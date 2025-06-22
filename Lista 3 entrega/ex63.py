'''
63. Solicite ao usu´ario que digite pares (produto, pre¸co) e armazene em um dicion´ario.
Permita pesquisar o pre¸co por produto.
'''

produtos = {}

while True:

    produto = str(input('Digite o nome do produto ou (sair) para sair: ')).lower()
    if produto == 'sair' :
        break

    preco = float(input('Digite o valor do produto ou ( 0 ) para sair: '))
    if preco == 0:
        break
        
    produtos[produto] = preco

while True:
    print('\n---- Pesquisar preço dos produtos ----\n')
    prod_desejado = input('Digite o nome do produto para ver o valor ou ( 0 ) para sair: ')
    if prod_desejado == '0':
        break
    
    print(f'O {prod_desejado} vale: R${produtos[prod_desejado]:.2f} ')


