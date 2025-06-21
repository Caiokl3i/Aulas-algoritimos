'''
27. Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.
'''
def mensagem_lista_vazia():
    print("====================== PILHA ======================")
    print("Digite 1 para adicionar algo na pilha ou 2 para remover da pilha")
    print("(1) - Adicionar")
    print("(2) - Remover")
    print()
    return int(input(": "))

def adicionar():
    print("====================== ADICIONAR ======================")
    print("Digite o que você quer adicionar na lista")
    print()
    return input(": ")



pilha = []

alternativa = mensagem_lista_vazia()

if alternativa == 1:
    item = adicionar()
    pilha.append(item)
    print
    print(f"PIlha: {pilha}")
elif alternativa == 2:
    if not pilha:
        print("Não há nada na pilha para remover!")
    else:
        print("item removido da pilha")
        pilha.pop()
        print()
        print(f"Pilha: {pilha}")
    
