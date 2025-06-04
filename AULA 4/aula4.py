'''
1 - var de controle
2 - condição de parada
3 - att da var de controle
'''
# # var de controle
# i = 0 
# # cond. parada
# while i < 10:
#     print(f"i :", {i})
#     # att da var
#     i - i + 1 # incremento

# -------------------------------------------------- 

# # var de controle
# i = 0
# # cond. parada
# while i < 10:
#     i = i + 1 # incremento
#     if i % 2 == 0:
#         print(f"i : {i}")
#         # att da var

# ----------------------------------------------------

# criar um laço que dependa da resposta do user p continuar o laço

resp_user = "s"
while resp_user == "s":
    print("Ainda estou reptindo")
    while True:
        resp_user = input("Deseja continuar S/N: ").lower()
        if resp_user == "n" or resp_user == "s":
            break
print("Terminei!!")