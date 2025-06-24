'''
78. Transforme uma lista de palavras em um dicion´ario que agrupe as palavras por
tamanho.
'''

palavras = ['fé', 'amor', 'vida', 'força', 'graça', 'paz', 'luz', 'esperança', 'coragem', 'verdade']

# tamanho é a chave e as palavras são o valor
# se a len(palavra) == chave da palavra entao eu adiciono, senão eu crio um dicionario com a chave len(palavra)

word_size = {}


for palavra in palavras:
    if len(palavra) in word_size:
        word_size[len(palavra)].append(palavra)
    else:
        word_size[len(palavra)] = [palavra]

print(word_size)