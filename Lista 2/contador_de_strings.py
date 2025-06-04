
# len() : contar quantos caracteres tem na string

texto = "banana"
print(len(texto))  # Saída: 6


#  ver.count("") : contar quantas vezes uma letra aparece

print(texto.count("a"))  # Saída: 3
print(texto.count("na"))  # Saída: 2


# split() : contar quantas palavras tem em uma frase

frase = "eu gosto de Python"
palavras = frase.split()  # Divide a frase em palavras
print(len(palavras))  # Saída: 4
