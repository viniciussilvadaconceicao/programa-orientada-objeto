class carro :
    def __init__(self, marca, modelo, cor, cambio, ano):
        self.cambio = cambio
        self.ano = ano 
        self.cor = cor
        self.modelo = modelo
        self.marca = marca

    def __str__(self):
        return f'''
    o carro é :{self.marca}
    modelo:{self.modelo}
    cor:{self.cor}
    cambio:{self.cambio}
    ano:{self.ano}
    '''

class Moto:
    def