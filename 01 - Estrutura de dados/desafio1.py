# Entrada de dados
saldoAtual = float(input("Digite o saldo atual da conta: "))
valorDeposito = float(input("Digite o valor a ser depositado: "))
valorRetirada = float(input("Digite o valor a ser retirado: "))

# Atualização do saldo
saldoAtual += valorDeposito
saldoAtual -= valorRetirada

# Saída formatada com uma casa decimal
print(f"Saldo atualizado na conta: {saldoAtual:.1f}")
