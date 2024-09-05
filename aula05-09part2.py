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
        
    
        