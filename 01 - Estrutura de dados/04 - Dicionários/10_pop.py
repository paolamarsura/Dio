contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)

#resultado = contatos.pop("guilherme@gmail.com", não encontrou)  # {}
#print(resultado) 

#método para remover uma chave do dict retornando o valor que foi removido