# c) Dado um número informe em qual dos intervalos ele se encontra.

# Intervalo A: de 0 a 20

# Intervalo B: de -5 a -1

# Intervalo C: de 21 a 60

# Intervalo D: de -100 a 15

n = int(input("Type a number: "))

if n > 0 and n < 20:
    if n > (-100) and n < 15:
        print("Its at A and D")
        
elif n > (-5) and n < (-1):
    if n > (-100) and n < 15:
        print("Its at B and D")
        
elif n > 0 and n < 20:
    print("Its at A")
    
elif n > -5 and n < -1:
    print("Its at B")
    
elif n > 21 and n < 60:
    print("Its at C")
    
elif n > -100 and n < 15:
    print("Its at C")
