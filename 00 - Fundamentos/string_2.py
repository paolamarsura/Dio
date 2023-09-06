nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade)) # forma não mais recomendada

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

#f-string é a forma mais utilizada

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") #exibe somente 2 casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") # insere 10 espaços em branco e mostra 1 casa decimal
