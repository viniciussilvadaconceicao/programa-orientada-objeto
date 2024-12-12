#questão 1
#master class
class Interfone:
    def __init__(self,endereco):
        self.modelo = "intelbras"
        self.endereco = endereco

    #abstrato
    def ligar_para_proprietario(self):
        pass 

    #abstrato
    def registra_chamada(self):
        pass

#questão 1.2
#subclasse InterfoneResidencial
class InterfoneResidencial(Interfone):
    def __init__(self,endereco,nome_proprietario, telefone_proprietario):
        super().__init__(endereco)
        self.nome_proprietario = nome_proprietario
        self.telefone_proprietario = telefone_proprietario

    @classmethod
    def metodo_cadastro(cls):
        endereco = input("digite o Endereço: ")
        apt = input("digite o numero do apartamento: ")
        proprietario1 = input("digite o nome do primeiro proprietario:")
        proprietario2 = input("digite o nome do segundo proprietario:")
        telefone1 = input("digite o telefone do primeiro proprietario:")
        telefone2 = input("digite o telefone do segundo proprietario:")
        return cls(endereco,{apt:[proprietario1,proprietario2]},{apt:[telefone1,telefone2]})  

    def ligar_para_proprietario(self, apt, n):
            proprietarios = self.nome_proprietario[apt]
            telefones = self.telefone_proprietario[apt]
            if 1 <= n <= len(proprietarios):
                print(f"ligando para o {proprietarios[n-1]} no telefone{telefones[n-1]} ({apt} no endereço {self.endereco})")
            else:
                print("numero do apartamento ou numero do proprietario invalido")

    def registra_chamada(self):
        horario_inicio = int(input("digite o horario da chamada:"))
        data = input("digite a data da chamada:")
        print(f"chamada registrada em {data} as {horario_inicio}")

        fim_chamada = int(input("digite o horario do fim da chamada:"))
        print(f"chamada finalizada as {fim_chamada}")

        duracao = horario_inicio- fim_chamada
        print(f"chamada durou {duracao} minutos")


#questão 2
#instanciando as classes e realizando interaçoes com varias opçoes de cadastro
#subclasse 
class InterfoneEmergencial(Interfone):
   def __init__(self,endereco,serviço,numero_serviço):
        super().__init__(endereco)
        self.serviço = serviço
        self.numero_serviço = numero_serviço

@classmethod
def metodo_cadastro(cls):
    endereco = input("digite o Endereço: ")
    serviço = input("qual o nome do serviço de emergencia?" )
    numero_servico = input("qual o numero do serviço de emergencia?" )
    return cls(endereco,serviço,numero_servico)

def ligar_para_proprietario(self):
    print(f"ligando para o serviço de emergencia {self.serviço} no numero {self.numero_serviço}")

def registra_chamada(self):
        horario_inicio = float(input("digite o horario da chamada:"))
        data = int(input("digite a data da chamada:"))
        print(f"chamada registrada em {data} as {horario_inicio}")

        fim_chamada = float(input("digite o horario do fim da chamada:"))
        print(f"chamada finalizada as {fim_chamada}")

        duracao = horario_inicio- fim_chamada
        print(f"chamada durou {duracao} minutos")

