class Animal:
    def __init__(self,nome,especie,cor,idade):
        self.nome = nome
        self.especie = especie
        self.cor = cor
        self.idade = idade
        self.andar = False
    
    def comeca_andar(self):
        if not self.andar:
            self.andar = True
            print(f"o animal definido {self.nome} que é cor {self.cor} da especie {self.especie} está andando")
        
        else:
            print("Animal já está andando!")
    
    def stop(self):
        if self.andar:
            self.andar = False
            print(f"O ANIMAL {self.nome} está parado")
        else:
            print("o animal está andando!!")

    def __str__(self):
        return f"o animal definido {self.nome} que é cor {self.cor} da especie {self.especie} está andando"

class Cachorro(Animal):
    def __init__(self, nome, especie,cor, idade, raca):
        super().__init__(nome,especie,cor,idade)
        self.raça = raca

cao = Cachorro('kyara','cachorro','preto','5','pitbull')
cao.comeca_andar()
cao.comeca_andar()
cao.stop()