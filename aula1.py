#init é o metodo construtor da classe 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def agradar_o_outro(self):
        var = input("fale algo agradavel: ")
        if var == "oi":
            print(f"{self.nome} disse que você esta muito bem hoje fulano")
        else:
            print(f"{self.nome} não é uma frasede finida")
            
    def desagradar_o_outro(self):
        var = input("fale algo desagradavel: ")
        if var == "não" or var == "NÃO":
            print(f"{self.nome} você esta de mal humor hoje")
        else:
            print(f"{self.nome} não é uma frase definida")

#self é o objeto que está sendo criado
#self.nome é o atributo do objeto
