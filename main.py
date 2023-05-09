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