class pessoa:
    def __init__(self, origem, idade, genero, cor, profissao):
        self.origem = origem
        self.idade = idade
        self.genero = genero
        self.cor = cor
        self.profissao = profissao

    def apresentacao(self):
        return (f"Olá, Sou do {self.origem}, tenho {self.idade} anos, "
                f"meu gênero é {self.genero}, minha etinia é {self.cor} e trabalho como {self.profissao}.")

pessoa1 = pessoa("Rio de Janeiro", 21, "masculino", "branco", "professor")
print(pessoa1.apresentacao())