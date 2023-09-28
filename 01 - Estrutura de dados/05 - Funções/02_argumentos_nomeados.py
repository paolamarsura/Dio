def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# formas de chamar essa função

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #chamar passando valores
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # chamar passando chave valor


salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # o ** significa que estou passando um dict para esta função
