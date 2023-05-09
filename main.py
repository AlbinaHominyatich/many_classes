#симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #список студентів
    def admit_student(self, student): #зарахування студентів
        self.students.append(student)
        print(f'{}') #дописати, коли створимо клас студентів

class Student:
