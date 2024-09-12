class banco:
    def __init__(self,nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.senha = None
    def criar_conta(cls,clientes):
