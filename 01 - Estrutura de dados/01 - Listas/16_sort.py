# método para ordenar a lista

#ordenação padrão - ordem alfabética por serem valores de string dentro da lista

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# posso passar um argumento, no reverse, ele irá ordenar de traz p/ frente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# quero colocar em ordem de tamanho das palavras, do menor para o maior por exemplo / lambda é uma função anônima / a função len tira o tamanho da uma string

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# posso combinar o método sort com as funções key, len e reverse / como python e charsp tem o mesmo tamanho (caracteres) o python fica em primeiro, pois aparece primeiro.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

