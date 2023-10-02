# Entrada de dados # Lê o saldo total da conta e o valor do saque
saldo_total = int(input()) 
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

# Verifica se o saldo é suficiente para o saque
if saldo_total >= valor_saque:
    saldo_total -= valor_saque
    print(f"Saque realizado com sucesso! Novo saldo: {saldo_total}")
else:
    print("Saldo insuficiente. Saque nao realizado!")