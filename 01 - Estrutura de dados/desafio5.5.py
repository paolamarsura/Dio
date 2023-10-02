valor = float(input())
saldo = 0

if valor == 0:
    print("Encerrando o programa...")
elif valor > 0:
   saldo += valor
   print("Deposito realizado com sucesso!")
   print(f"Saldo atual: R$ {saldo:.2f}")
   
else:
  print("Valor invalido! Digite um valor maior que zero.")