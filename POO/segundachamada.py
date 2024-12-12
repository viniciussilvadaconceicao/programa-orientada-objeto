from time import sleep

class Usuario:
    def __init__(self, id_usuario, nome_usuario, email_usuario):
        self.id_usuario = id_usuario
        self.nome = nome_usuario
        self.email = email_usuario

    @classmethod
    def metodo_cadastro(cls):
        nome_usuario = input("Qual o nome do usuário que deseja cadastrar: ")
        id_usuario = input("Qual o Identificador único do usuário para cadastrar: ")
        email_usuario = input("Qual o Email do usuário para cadastrar: ")
        return cls(id_usuario, nome_usuario, email_usuario)
    
    def __str__(self):
        return f"Identificador único do usuário: {self.id_usuario}\nNome do usuário: {self.nome}\nEmail do usuário: {self.email}"


class Produto:
    def __init__(self, nome_produto, descricao_produto, preco_produto, quantidade_estoque):
        self.nome = nome_produto
        self.descricao = descricao_produto
        self.preco = preco_produto
        self.quantidade_estoque = quantidade_estoque

    @classmethod
    def metodo_cadastro(cls):
        nome_produto = input("Qual o nome do produto que deseja cadastrar: ")
        descricao_produto = input("Qual a Descrição do produto para cadastrar: ")
        preco_produto = float(input("Qual o preço do produto: "))
        quantidade_estoque = int(input("Qual a quantidade do produto em estoque: "))
        return cls(nome_produto, descricao_produto, preco_produto, quantidade_estoque)
    
    def __str__(self):
        return (f"Nome do produto: {self.nome}\nDescrição do produto: {self.descricao}\nPreço do produto: {self.preco}\nQuantidade em Estoque: {self.quantidade_estoque}")


class Porta:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        self.aberta = False

    def abrir(self):
        if not self.aberta:
            self.aberta = True
            print("A porta abriu.")
        else:
            print("A porta estava aberta.")

    def fechar(self):
        if self.aberta:
            self.aberta = False
            print("A porta fechou.")
        else:
            print("A porta estava fechada.")

class Chave:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def usar_chave(self, porta):
        if porta.aberta:
            porta.fechar()
        else:
            porta.abrir()

class Macaneta:
    def __init__(self, tipo):
        self.tipo = tipo

    def girar(self, porta):
        if porta.aberta:
            porta.fechar()
        else:
            porta.abrir()


usuario = Usuario.metodo_cadastro()
produto = Produto.metodo_cadastro()
print("\n")
print(usuario)
sleep(2)
print("\n")
print(produto)
print("\n")
