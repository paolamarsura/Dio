lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

# método para copiar a lista.

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista)) # retorna o ID da lista, mostrando que apesar do método copy, elas são diferentes.