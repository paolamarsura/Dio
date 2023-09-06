nome = "gUIlherME"

print(nome.upper()) # tudo em letra maiuscula
print(nome.lower()) # tudo em letra minuscula
print(nome.title()) # primeira em maiusculo, resto em minusculo

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") #remove espaço em branco na esquerda e na direita
print(texto.rstrip() + ".") #remove espaço em branco à direita
print(texto.lstrip() + ".") #remove espaço em branco à esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#")) # recebe 2 argumentos, o primeiro é o n° de caracteres que tera no final e o segundo é opcional - define o caractere que entrara no espaço
print("-".join(menu)) #neste caso acresce . entre os caracteres
