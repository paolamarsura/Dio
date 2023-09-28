# declarando função

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# chamando a função

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme") # caso a função tenha argumentos e eu não tenha declarado ele, eu preciso passar ele no momento de chamar a função ou irá retornar um erro.
exibir_mensagem_3() # quando eu já declarei o argumento na função, na hora de chamar a função ela é opcional.
exibir_mensagem_3(nome="Chappie") # se eu optar por declarar novamente, ele vai substituir o valor.
