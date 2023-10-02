ativos = [] # Inicializa uma lista para armazenar os ativos

# Entrada da quantidade de ativos / Lê a quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos / Lê os tipos de ativos e os adiciona à lista
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Organiza os ativos em ordem alfabética
ativos.sort()

# Imprime os ativos em ordem alfabética
for ativo in ativos:
    print(ativo)

