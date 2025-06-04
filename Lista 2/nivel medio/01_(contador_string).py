# frase = "caio"
# for letra in frase:
#     print(letra)

# for i in range(n) → percorre números.

# for letra in frase → percorre letras.

sentence = str(input("Escreva uma frase: "))

vogal = "aeiou"
count = 0

for leters in sentence:
    if leters in vogal:
        count += 1
print(f"Há {count} vogais in this sentence")



