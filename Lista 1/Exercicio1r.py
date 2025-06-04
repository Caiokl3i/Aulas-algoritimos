saldo_medio = int(input("Digite o saldo médio: "))

credit = 0 
val_credit = 0

if saldo_medio >= 201 and saldo_medio <= 400:
    val_credit = saldo_medio * 1.2
elif saldo_medio >= 401 and saldo_medio <= 600:
    val_credit = saldo_medio * 1.3
elif saldo_medio >= 601:
    val_credit = saldo_medio * 1.4
else:
    val_credit = 0

print("Saldo médio: ", saldo_medio)
print("Valor do crédito: " , val_credit)
