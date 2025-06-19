'''
R1. Contagem regressiva com atraso
Implemente uma fun¸c˜ao recursiva contagem regressiva(n) que imprime uma contagem de n at´e 0. Ao chegar a 0, deve imprimir "Boom!".
(Opcional: usar time.sleep(1) para simular contagem real.)
'''

import time

def regressive_counter(n):
    if n == 0:
        return print('Boom!')
    print(n)
    time.sleep(0.8)
    return regressive_counter(n - 1)

regressive_counter(5)