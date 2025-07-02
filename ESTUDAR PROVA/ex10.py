def imprimir_dados(**kwargs):
    # ➤ Deve imprimir: "Caio tem 19 anos"

    print(f'{kwargs['nome']} tem {kwargs['idade']} anos')

imprimir_dados(nome='Caio', idade=19)