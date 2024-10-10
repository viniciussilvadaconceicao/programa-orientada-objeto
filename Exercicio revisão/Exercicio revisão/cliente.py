class cliente:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha  

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}")

    def alterar_senha(self, nova_senha):
        self.__senha = nova_senha
        print("Senha alterada com sucesso.")

    def verificar_senha(self, senha):
        return self.__senha == senha

    @classmethod
    def criar_cliente(cls, nome, email, senha):
        return cls(nome, email, senha)

cliente1 = cliente.criar_cliente("Rafael", "rafael@gmail.com", "123")
cliente1.exibir_informacoes()
verificação = cliente1.verificar_senha("123")
print(verificação)
if verificação == False:
    print("Senha incorreta!")
else:
    cliente1.alterar_senha("456")  