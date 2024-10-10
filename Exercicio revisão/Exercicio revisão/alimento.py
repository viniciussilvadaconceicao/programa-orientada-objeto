class alimento:
    def __init__(self, nome, tipo, verde=True):
        self.nome = nome
        self.tipo = tipo
        self.verde = verde
        self.apodrecido = False

    def madurecer(self):
        if self.verde:
            self.verde = False
            print(f" {self.nome} está maduro agora.")
        else:
            print(f" {self.nome} já está maduro.")

    def apodrecer(self):
        if not self.apodrecido:
            self.apodrecido = True
            print(f" {self.nome} apodreceu.")
        else:
            print(f" {self.nome} já está apodrecido.")

banana = alimento("maça", "fruta")
banana.madurecer()   
banana.apodrecer()   
   