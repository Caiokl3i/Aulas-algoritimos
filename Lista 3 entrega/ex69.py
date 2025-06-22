'''
69. Verifique se uma chave est´a presente em um dicion´ario e imprima seu valor, se
existir.
'''

frutas = {
    'banana': 'amarela',
    'maça': 'vermelho',
    'melancia': 'verde',
    'morango': 'vermelho'
}

chave = input("Digite o nome da fruta: ").lower()

if chave in frutas:
    print(f"A cor da {chave} é {frutas[chave]}")
else:
    print("Essa fruta não está na lista.")