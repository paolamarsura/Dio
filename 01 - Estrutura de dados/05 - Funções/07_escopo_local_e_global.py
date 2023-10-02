salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)


# Py trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em obj imutáveis serão perdidas quando o método terminar de ser executado. Para usar obj globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
# ESSA NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA.