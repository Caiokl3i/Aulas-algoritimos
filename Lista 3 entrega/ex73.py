'''
73. Crie uma fun¸c˜ao que inverta as chaves e valores de um dicion´ario
'''
from collections import defaultdict

alunos = {
    'Caio': (6, 6),
    'Victor': (6, 6),
    'Valentim': (8, 10)
}

dict_invertido = defaultdict(list)

for chave, valor in alunos.items():
    dict_invertido[valor].append(chave)

print(dict_invertido)

# aprender mais sobre default dict