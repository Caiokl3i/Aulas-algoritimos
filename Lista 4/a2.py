from functools import reduce

'''
A2. Multiplica¸c˜ao com *args e verifica¸c˜ao de tipo
Crie uma fun¸c˜ao que multiplica todos os argumentos num´ericos, ignorando qualquer
argumento que n˜ao seja int ou float
'''

def multiplicação(*num):
    return reduce(lambda x, y: x * y, [n for n in num if isinstance(n, (int, float)) and not isinstance(n, bool)])

print(multiplicação(2, 2, 2, 'caio', 'animal', True))

