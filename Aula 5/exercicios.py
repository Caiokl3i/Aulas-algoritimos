import random

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
# 1 = Selthon
# 2 = Caio
# 3 = Leo do pastel
# 4 = voto em branco

# exemplo_list = [qtde votos, porcentagem]

selthon_list = []
caio_list = []
leo_list = []
branco_list = []

votos = []

for _ in range(1001):
    x = random.randint(1, 4)
    votos.append(x)
print(votos)

qtde_votos = len(votos)

qtde_selthon = votos.count(1)
qtde_caio = votos.count(2)
qtde_leo = votos.count(3)
qtde_branco = votos.count(4)

selthon_list.append(qtde_selthon)
caio_list.append(qtde_caio)
leo_list.append(qtde_leo)
branco_list.append(qtde_branco)

def porcentagem(num, total):
    num = (num / total) * 100
    return num

selthon_list.append(porcentagem(qtde_selthon, qtde_votos))
caio_list.append(porcentagem(qtde_caio, qtde_votos))
leo_list.append(porcentagem(qtde_leo, qtde_votos))
branco_list.append(porcentagem(qtde_branco, qtde_votos))

print("")
print(f'Selthon obteve {selthon_list[0]} votos - {selthon_list[1]:.1f}% dos votos')
print("")
print(f'Caio obteve {caio_list[0]} votos - {caio_list[1]:.1f}% dos votos')
print("")
print(f'Leo do Pastel obteve {leo_list[0]} votos - {leo_list[1]:.1f}% dos votos')
print("")
print(f'Houveram {branco_list[0]} votos em branco - {branco_list[1]:.1f}% dos votos')
print("")



qtde_votos_cada = [qtde_selthon, qtde_caio, qtde_leo]
if max(qtde_votos_cada) == qtde_votos_cada[0]:
    print(f'Candidato com maior voto: SELTHON')
elif max(qtde_votos_cada) == qtde_votos_cada[1]:
    print(f'Candidato com maior voto: CAIO')
elif max(qtde_votos_cada) == qtde_votos_cada[2]:
    print(f'Candidato com maior voto: LEO DO PASTEL')

print()

if min(qtde_votos_cada) == qtde_votos_cada[0]:
    print(f'Candidato com menor voto: SELTHON')
elif min(qtde_votos_cada) == qtde_votos_cada[1]:
    print(f'Candidato com menor voto: CAIO')
elif min(qtde_votos_cada) == qtde_votos_cada[2]:
    print(f'Candidato com menor voto: LEO DO PASTEL')

print()


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