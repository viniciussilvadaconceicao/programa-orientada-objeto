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
def criar_conta():
          