# se o número for par continua executando, se for impar exibe o número, se for 10 para a execução (break)!

while True:
    numero = int(input("Informe um número: "))

    if numero == 10: 
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
