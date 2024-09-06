# criar um sistema de banco
# usando class atributos

class Banco:
    #atributo da classe
    def __init__(self, nome, senha, saldo):
        self.nome = nome
        self.senha = senha
        self.saldo = saldo
        self.clientes = []

    #metodo depositar
    def depositar(self, valor):
        self.saldo += valor
    #metodo consultar saldo
    def consultar_saldo(self):
        return self.saldo
    #metodo de apresentação
    def apresentar(self):
        print(f"nome: {self.nome}")
        print(f"saldo: {self.saldo}")
        print(f"clientes: {self.clientes}")
    #metodo adicionar cliente na lista
    def add_cliente(self, cliente):
        self.clientes.append(cliente)
    #metodo saldo cliente
    def get_saldo(self):
        return self.saldo
    #metodo lista de clientes
    def get_clientes(self):
        return self.clientes
    @classmethod
    def main(cls):
        banco = cls("Banco do Brasil", "123", 0)
        while True:
            print("1-criar conta")
            print("2-depositar")
            print("3-consultar saldo")
            print("4-sair")
            print("5-apresentar")
            choice = int(input("escolha uma opção: "))
            
            if choice == 1:
                nome = input("nome: ")
                senha = input("senha: ")
                saldo = float(input("saldo: "))
                banco = cls(nome, senha, saldo)
                print(f"conta criada com sucesso")
            
            elif choice == 2:
                if not banco:
                    print("não há contas cadastradas")
                    continue
                valor = float(input("valor do deposito: "))
                banco.depositar(valor)
                print("deposito realizado com sucesso")
            
            elif choice == 3:
                if not banco:
                    print("não há contas cadastradas")
                    continue
                print(f"saldo: {banco.consultar_saldo()}")
            
            elif choice == 4:
                print("opção inválida")
                print("programa encerrado")
                break
            
            elif choice == 5:
                banco.apresentar()
Banco.main()