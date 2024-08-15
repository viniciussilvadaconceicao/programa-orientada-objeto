#init é o metodo construtor da classe 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)

#self é o objeto que está sendo criado
