class Studants:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
        
    @property
    def is_passing(self):
        return self.get_average_grade() >= 60
    
    @classmethod
    def main(cls):
        Studants = []

        while True:
            print("1 adicionar aluno")
            print("2 adicionar nota")
            print("3 verificar nota")
            print("4 sair")
        