def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# por padrão argumentnos podem ser passados para uma função py tanto por posição quanto explicitamenete pelo nome, para uma melhor legibilidade e desempenho faz sentido restringir a maneira pela qual argumentos possam ser passados, assim um dev precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

# def f (pos1, pos2, /, ´pos_or_kwd, *, kwd1, kwd2):
# onde tudo que esta até a / é por posição e tudo que esta antes do *, é por posição ou palavra(chave) nomeados e o que esta após somente por palavra(chave).