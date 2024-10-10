class calculo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def valor_area(self):
        area = self.calcular_area()
        print(f"A área do objeto com base de {self.base} metros e altura de {self.altura} metros é {area} m².")

retangulo = calculo(5, 3)
retangulo.valor_area()  
