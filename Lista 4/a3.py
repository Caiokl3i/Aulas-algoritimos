'''
A3. Sauda¸c˜ao personalizada com **kwargs
Crie uma fun¸c˜ao saudar(**kwargs) que aceita os argumentos nome, idade e cidade,
e monta uma mensagem personalizada.
Exemplo: "Ol´a, Jo~ao de 30 anos, morador de S~ao Paulo!"
'''

# *args junta valores em uma tupla
# **kwargs junta argumentos nomeados em um dicionário

def saudacao(**info):
    print(f'Olá {info["nome"]} de {info["idade"]} anos, morador de {info["cidade"]}')

saudacao(nome='Caio', idade=19, cidade='São Paulo')