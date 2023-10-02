saldo = 0

while True:
    try:
        valor_deposito = float(input("Digite o valor do depósito (ou digite 0 para encerrar): "))
        
        if valor_deposito == 0:
            print("Encerrando o programa.")
            break
        elif valor_deposito > 0:
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido! Digite um valor maior que zero.")
    except ValueError:
        print("Valor inválido! Digite um valor numérico.")


