import random

# Escolher aleatoriamente, os números num intervalo
x = random.randint(0, 10)

# Escolher aleatoriamente uma sequência
escolha = ["gelado", "quente"]
y = random.choice(escolha)

# ---------------------------------------------------
# LISTAS / TUPLAS / DICIONÁRIOS
# ---------------------------------------------------

# Lista - Coleções
nome = "beto"

# Sintaxe de lista
lista = ["a", "b", "c", "ifms", 2025, 3.14]
# Índices:    0    1    2     3      4     5

# Imprimindo a lista completa
print(lista)

# Imprimindo item por item usando índice
for i in range(6):
    print(lista[i])

# Imprimindo item por item diretamente
for item in lista:
    print(item)

# Acessar/imprimir valores específicos
print(lista[-1])
print(lista[5])

# Mudar valor de um índice
lista[2] = "caio"

# Acrescentar item no final da lista
lista.append("caio victor")
print(lista[6])

# Remover item pelo valor
lista.remove(lista[2])

# Ordenar a lista
lista.sort()

# Inverter a lista
lista.reverse()

# Contar o tamanho da estrutura
print(len(lista))

# Imprimir com índice
for i in range(len(lista)):
    print(lista[i])

# Enumerate - retorna índice e valor
for i, item in enumerate(lista):
    print(f"o item de indice {i} tem valor: {item}")

# ---------------------------------------------------
# TUPLAS
# ---------------------------------------------------

# Tuplas são semelhantes a listas, porém são imutáveis!
# Não pode acrescentar, apagar ou fazer atribuição

# Sintaxe
tupla = (1, 2, 3, 4)
# Índices: 0  1  2  3

print(tupla[0])

# Lista contendo uma tupla
lista = [1, 2, 3, (2, 3, 4)]

# Converter tupla em lista
nova_lista = list(tupla)

# Converter lista em tupla
nova_tupla = tuple(lista)

# ---------------------------------------------------
# PESQUISAS
# ---------------------------------------------------
# set, frozenset

# ---------------------------------------------------
# EXERCÍCIOS
# ---------------------------------------------------

# Exercicio 1 -> Descobrir como pegar esses valores
lista1 = [1, 2, 3, ["beto", "ifms", [3.14, 3.15, 3.16]]]

# EXERCICIO 2 -> Sistema de eleição
'''
Ler 1000 votos para escolher 1 de 3 candidatos ou votar em nulo

Mostrar no final:
- Quantidade de votos dos candidatos
- A porcentagem que cada um obteve
- Porcentagem de votos em branco também

Apresentar qual foi o candidato com o maior e menor número de votos
'''

# EXERCICIO 3 -> Escolha de vinhos
'''
Ler uma quantidade infinita de escolhas de vinhos, entre:
1 - seco
2 - tinto
3 - sem preferência

O sistema para quando o usuário decidir parar
'''

# EXERCICIO 4 -> Listas de listas
'''
Ler uma lista de listas, onde cada lista interna contém 3 valores: [numero, idade, sexo]

imprima o numero, idade e sexo de cada pessoa 
'''