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
        students = []

        while True:
            print("1 adicionar aluno")
            print("2 adicionar nota")
            print("3 verificar nota")
            print("4 sair")
            choice = int(input("escolha uma opção: "))

            if choice == 1:
                name = input("nome do aluno: ")
                age = int(input("idade do aluno: "))
                student = cls(name, age)#cria uma instância da classe
                students.append(student)
                print(f"aluno {name} adicionado")
            
            elif choice == 2:
                if not students:
                    print("não há alunos cadastrados")
                    continue
                for idx, student in enumerate(students):
                    print(f"{idx+1} {student.name}")
                    student_idx = int(input("escolha um aluno: "))
                    if 0 <= student_idx < len(students):
                        grade = float(input("nota do aluno: "))
                        students[student_idx].add_grades(grade)
                        print("nota adicionada")
                    else:
                        print("aluno não encontrado")

            elif choice == 3:
                if not students:
                    print("não há alunos cadastrados")
                    continue
                for student in students:
                    average_grade = student.get_average_grade()
                    if average_grade >= 6.0:
                        status = "provado"
                    else:
                        status = "reprovado"
                    print(f"""{student.name} 
                          média: {average_grade} 
                          status {status}""")
                    
            elif choice == 4:
                print("saindo...")
                print("obrigado por usar o programa")
                print("até mais")
                break
            
            else:
                print("opção inválida, tenta novamente")

Studants.main()
