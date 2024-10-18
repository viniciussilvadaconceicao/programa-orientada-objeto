class Pessoa:
    def __init__(self, nome, sobreNome, altura, peso):
        self.nome = nome
        self.sobreNome = sobreNome
        self.altura = altura
        self.peso = peso
        self.andar = False

    def comeca_andar(self):
        if not self.andar:
            self.andar = True
            print(f'{self.nome} {self.sobreNome} está andando.')
        else:
            print(f'{self.nome} {self.sobreNome} já está andando.')

    def parar(self):
        if self.andar:
            self.andar = False
            print(f'{self.nome} {self.sobreNome} parou de andar.')
        else:
            print(f'{self.nome} {self.sobreNome} já está parado.')

class Estudante(Pessoa):
    def __init__(self, nome, sobreNome, altura, peso, curso):
        super().__init__(nome, sobreNome, altura, peso)
        self.curso = curso
        self.pegar = None

    def __str__(self):
        return f'{self.nome} {self.sobreNome} está realizando curso de {self.curso}.'

    def adquirir(self, diploma):
        if self.pegar is None:
            self.pegar = diploma
            if self.pegar.nomeCurso == self.curso:
                print(f'{self.nome} {self.sobreNome} adquiriu o diploma de {self.curso}.')
            else:
                print(f'{self.nome} {self.sobreNome} não adquiriu o diploma de {self.curso}.')

class Diploma:
    def __init__(self, nomeCurso):
        self.nomeCurso = nomeCurso

    def __str__(self):
        return f'{self.nomeCurso}'

estudante1 = Estudante("vinicius", "Silva", 1.75, 20, "Engenharia de software")
diploma = Diploma("Engenharia de software")
print(estudante1)
estudante1.comeca_andar()
print('chegou na faculdade')
estudante1.parar()
estudante1.adquirir(diploma)
