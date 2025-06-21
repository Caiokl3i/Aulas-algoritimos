'''
R2. Inverter string recursivamente
Escreva uma fun¸c˜ao recursiva que recebe uma string e retorna a string invertida.
Exemplo: "python" → "nohtyp"
'''

reversed_text = ''

def string_invert(texto):
    global reversed_text
    if texto == '':
        return 
    
    reversed_text = texto[0] + reversed_text
    return string_invert(texto[1:])

string_invert('python')
print(reversed_text)

