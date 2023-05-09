#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #список студентів
    def admit_student(self, student): #зарахування студентів
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #дописати, коли створимо клас студентів

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade +=  1
        print(f'{self.name} був підвищений {self.grade}')
    def demote(self):
        self.grade -=  1
        print(f'{self.name} був понижений {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'

