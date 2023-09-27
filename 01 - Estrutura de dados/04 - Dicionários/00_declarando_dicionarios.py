pessoa = {"nome": "Guilherme", "idade": 28} #declarando dicionário por meio de {}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28) #declarando dicionário por meio da classe dict
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

#conj de pares chave:valor onde a chave tem que ser um valor imutável e o valor pode ser qualquer obj.
