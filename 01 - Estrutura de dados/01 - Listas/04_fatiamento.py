lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"] este é o caso de exceção, tudo é vazio, então retorna uma cópia da lista
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"] este caso espelha um sequência

# preciso passar ou o índice inicial ou final para o fatiamento
# a posição final não é retornada, é retornada a posição final menos uma posição
