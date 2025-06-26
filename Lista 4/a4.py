'''
A4. Fun¸c˜ao de filtro com *args e **kwargs
Escreva uma fun¸c˜ao que aceita uma lista de n´umeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.
'''

numeros = [1, 3,'caio', 5, 14, 15, 45, 66, 88, 89]

def filtro(*args, **kwargs):
    minimo = kwargs.get('min', 10)
    maximo = kwargs.get('max', 50)
    
    filtrados = [n for n in args if isinstance(n, (int, float)) and minimo <= n <= maximo]

    return filtrados

print(filtro(*numeros))