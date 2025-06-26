'''
A5. Fun¸c˜ao de formata¸c˜ao flex´ıvel
Crie uma fun¸c˜ao que usa **kwargs para formatar strings com placeholders personalizados.
Exemplo: formata("Ol´a {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana",
cidade="Recife")
'''

def func(texto, **kwargs):
    return texto.format(**kwargs)
