resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

#método para criar a chave no dict, sem atribuir valor (none) ou para criar um conj de chaves e colocar um valor padrão nelas.