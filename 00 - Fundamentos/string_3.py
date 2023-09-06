nome = "Guilherme Arthur de Carvalho"

print(nome[0]) #utiliza índice para acessar no caso, a primeira letra seria G.
print(nome[-2]) 
print(nome[:9])
print(nome[10:])
print(nome[10:16]) # start + stop
print(nome[10:16:2]) # start + stop + step
print(nome[:]) #retorna toda a string
print(nome[::-1]) #espelhamento da string (invertida)

# fatiamento de strings é uma técnica utilizada para retornar substrings (partes da original)
# start, step, stop