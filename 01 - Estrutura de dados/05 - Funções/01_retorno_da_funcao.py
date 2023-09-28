def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11) retorna uma tupla (imútavel)
print(func_3()) # retorna none 

# para retornar um valor, utilizamos a palavra return, toda função py retorna none por padrão, diferente de outras linguagens; em py uma função pode retornar mais de um valor.