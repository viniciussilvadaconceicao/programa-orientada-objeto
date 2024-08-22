class carro :
    def __init__(self, marca, modelo, cor, cambio, ano):
        self.cambio = cambio
        self.ano = ano 
        self.cor = cor
        self.modelo = modelo
        self.marca = marca


    def apresentar(self):
        '''aqui ira apresentar'''
        print(
        f'''
    o carro é :
    marca:{self.marca}
    modelo:{self.modelo}
    cor:{self.cor}
    cambio:{self.cambio}
    ano;{self.ano}
        ''')
    
carro1 = carro('bmw', 'x6', 'azul', 'automatico', '2024')
carro1.apresentar()