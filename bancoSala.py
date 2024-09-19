class banco:
    def __init__(self,nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.senha = None

    def cadastrar_senha(self):
        if not self.senha:
            self.senha = input("cadastre sua senha:")
            print("senha cadastrada com sucesso!")
        else:
            print("senha já cadastrada.")

    def verificar_senha(self):
        tentativa = input("digite sua senha:")
        return tentativa == self.senha
    
    def depositar(self,valor):
        if valor > 0 :
            self.saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")
    
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def apresentar(self):
        print(f"cliente:{self.nome},Saldo:R${self.saldo}")
    
    def transferir(self,destinatario,valor):
        if self.saldo >= valor and valor > 0:
            if self.verificar_senha():
                self.saldo -= valor
                destinatario.saldo += valor
                print(f"Transferencia de R${valor} realizada para {destinatario.nome}.")
            else:
                print("Senha incorreta. Transferencia cancelada.")
        else:
            print("Transferencia invalida. Saldo insuficiente ou valor incorreto") 

    @classmethod
    def criar_conta(cls):
        nome = input("Digite o nome do cliente: ")
        saldo = float(input("Digite o saldo inicial: "))
        cliente = cls(nome, saldo)
        cliente.cadastrar_senha()
        return cliente

    @classmethod
    def selecionar_conta(cls,clientes):
        if len(clientes) == 0:
            print("nenhum conta disponivel. crie uma conta primeiro.")
            return None
        print("===Contas disponiveis===")
        for idx,cliente in enumerate(clientes):
            print(f"{idx + 1}.{cliente.nome}")

        opcao = int(input("Selecione a conta: "))
        if 1 <= opcao <= len(clientes):
            return clientes[opcao- 1]
        else:
            print("Conta invalida.")
            return None
        
    while True:
        print("1-Criar conta")
        print("2-Selecionar conta")
        print("3-Depositar")
        print("4-Cpnsultar saldo")
        print("5-Apresentar dados")
        print("6-Transferir")
        print("7-Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == "1":
            novo_cliente = cls.criar_conta()
            clientes .append(novo_cliente)
            