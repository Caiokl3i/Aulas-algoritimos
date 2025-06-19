minha_lista = [1, "texto", 3.5, [1, 2, 3], {"chave": "valor"}]

# Agora, escreva um código que percorre essa lista e imprime só os elementos que são números (inteiros ou float).

for item in minha_lista:
    if isinstance(item, list):
        print(item)
