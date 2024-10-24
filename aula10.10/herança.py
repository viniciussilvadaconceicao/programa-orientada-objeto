# Comida
class Comida:
    def __init__(self, nome):
        self.nome = nome
        self.cortada = False

    def __str__(self):
        if not self.cortada:
            return f"A comida: {self.nome} não está cortada"
        else:
            return f"A comida: {self.nome.nome} está cortada"

# Prato
class Prato:
    def __init__(self, marca, tipo_p):
        self.marca = marca
        self.tipo_p = tipo_p
        self.comida = None #armazenar comida de Comida

    def colocar_comida_no_prato(self, comida):
        self.comida = comida
        print(f"A comida: {self.comida} está no prato {self.marca}, que é um prato {self.tipo_p}")
    

#Talher
class Talher:
    def __init__(self, tipo):
        self.tipo =  tipo

    def cortar_comida(self, comida):
        comida.cortada = True
        print(f"A comida: {comida.nome} foi cortada")
    

frango = Comida("Frango")
print(frango)

prato = Prato("Tramontina", "Vidro")

prato.colocar_comida_no_prato(frango)

faca = Talher("Faca")
faca.cortar_comida(frango)