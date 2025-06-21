'''
43. Implemente um sistema que simule um carrinho de compras: adi¸c˜ao, remo¸c˜ao e
total de itens com pre¸cos.
'''

import time

produtos_carrinho = []

produtos = [
    {'nome': 'Mouse Gamer', 'preco': 149.90},
    {'nome': 'Teclado Mecânico', 'preco': 249.90},
    {'nome': 'Monitor 24"', 'preco': 899.00},
    {'nome': 'Fone Bluetooth', 'preco': 199.50},
    {'nome': 'Webcam Full HD', 'preco': 299.99}
]


def menu_escolhas():
    while True:
        print('\n----- ESCOLHA -----\n')
        print(f'1 - Adicionar um produto')
        if len(produtos_carrinho) > 0:
            print(f'2 - Remover um produto')
        print(f'0 - Acabar compras\n')

        escolha = int(input('Digite a opção desejada: '))
        
        time.sleep(0.8)
        
        match escolha:
                case 1:
                    add_produto()
                case 2:
                    remove_produto()
                case 0: 
                    break

def add_produto():
    while True:
        print('\n----- PRODUTOS -----\n')
        for i, item in enumerate(produtos):
            print(f'{i + 1} - {item["nome"]} por R${item["preco"]}')

        escolha = int(input('\nDigite o produto que voçê quer: \n'))
        
        time.sleep(0.8)

        match escolha:
            case 1:
                produtos_carrinho.append(produtos[0])
            case 2:
                produtos_carrinho.append(produtos[1])
            case 3:
                produtos_carrinho.append(produtos[2])
            case 4:
                produtos_carrinho.append(produtos[3])
            case 5:
                produtos_carrinho.append(produtos[4])
            case _:
                print('Não é um número válido')
                break
        
        print()
        print(f'\n----- PRODUTOS NO CARRINHO -----\n')
        for item in produtos_carrinho:
            print(f'- {item["nome"]}\n')
            
        time.sleep(0.8)
        break

def remove_produto():
    while True:
        print(f'\n----- PRODUTOS NO CARRINHO ----- \n')
        for i, item in enumerate(produtos_carrinho):
            print(f'{i+1} - {item["nome"]}')
        
        escolha = int(input('\nNúmero do produto que deseja remover: '))
        
        produtos_carrinho.pop(escolha - 1)
        
        time.sleep(0.8)
        
        print(f'\n----- NOVO CARRINHO ----- \n')
        for i, item in enumerate(produtos_carrinho):
            print(f'{i+1} - {item["nome"]}')
            
        time.sleep(0.8)
        break

menu_escolhas()