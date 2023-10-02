def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros)**periodo
    return round(valor_final, 2)  # Arredonda para duas casas decimais

# resposta desafio

valor = calcular_valor_final(valor_inicial, taxa_juros, periodo)
print(f"Valor final do investimento: R$ {valor:.2f}")


# Exemplos de uso da função
valor1 = calcular_valor_final(5000, 0.08, 5)
print(f"Valor final do investimento: R$ {valor1:.2f}")

valor2 = calcular_valor_final(1000, 0.06, 3)
print(f"Valor final do investimento: R$ {valor2:.2f}")

valor3 = calcular_valor_final(20000, 0.04, 10)
print(f"Valor final do investimento: R$ {valor3:.2f}")
