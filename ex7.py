'''Criar a classe Pessoa
    Atributos: nome, altura, peso, relacao

Classe Automóvel
    atributos: marca, ano, modelo, cor, movimento, velocidade
    métodos: ligar, desligar

classe Moto
   atributos: macha
   método: acelerar, passar de marchar

Classe Carro
    atributos: macha
   método: acelerar, passar de marchar

O que é para ser feito: quem deve ligar desligar a moto ou o carro é a pesso'''

class Pessoa:
    def __init__(self, nome, altura, peso, relacao):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.relacao = relacao
    
class Automovel:
    def __init__(self, marca, ano, modelo, cor, movimento, velocidade):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.movimento = movimento
        self.velocidade = velocidade

    def ligar(self):
        if not self.movimento:
            self.movimento = True
            print(f"O {self.modelo} esta ligado")
        else:
            print(f"O {self.modelo} já foi ligado")
    
    def desligar(self):
        if self.movimento:
            self.movimento = False
            print(f"O {self.modelo} está desligado")
        else:
            print(f"O {self.modelo} já foi desligado")
        
class Moto(Automovel):
    def __init__(self, marca, ano, modelo, cor, movimento, velocidade, macha):
        super().__init__(marca, ano, modelo, cor, movimento, velocidade)
        self.macha = macha
    
    def acelerar(self):
        if self.movimento:
            self.velocidade += 10
            print(f"A {self.modelo} está acelerando")
        else:
            print(f"A {self.modelo} não está em movimento")
    
    def passar_macha(self):
        if self.movimento:
            self.macha += 1
            print(f"A {self.modelo} passou de macha")
        else:
            print(f"A {self.modelo} não está em movimento")

class Carro(Automovel):
    def __init__(self, marca, ano, modelo, cor, movimento, velocidade, macha):
        super().__init__(marca, ano, modelo, cor, movimento, velocidade)
        self.macha = macha
    
    def acelerar(self):
        if self.movimento:
            self.velocidade += 10
            print(f"O {self.modelo} está acelerando")
        else:
            print(f"O {self.modelo} não está em movimento")
    
    def passar_macha(self):
        if self.movimento:
            self.macha += 1
            print(f"O {self.modelo} passou de macha")
        else:
            print(f"O {self.modelo} não está em movimento")

pessoa1 = Pessoa("Vinicius", 1.71, 80, "eu mesmo")
moto1 = Moto("Honda", 2020, "hornet", "vermelha", True, 0, 0)
carro1 = Carro("BMW", 2024, "X6", "VERMELHO VINHO", False, 0, 0)

moto1.ligar()
moto1.acelerar()
moto1.passar_macha()
moto1.desligar()