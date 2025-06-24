'''
76. Leia uma frase do usu´ario e crie um dicion´ario que conte quantas vezes cada letra
aparece.
'''
from collections import Counter

frase = input('Digite uma frase: ').upper().replace(' ', '')

frase_limpa = [letra for letra in frase if letra.isalpha()]

contagem_letras = dict(Counter(frase_limpa))

for chave, valor in contagem_letras.items():
    print(f'A letra {chave} aparece {valor} vezes')