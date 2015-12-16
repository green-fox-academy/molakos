

class Student():
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return self.grades

    def get_average(self):
        summa = 0
        for grade in self.grades:
            summa += grade
        return summa / len(self.grades)

class Class():
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.average = 0


    def add_student(self, student):
        self.students.append(student)
        return self.students

    def get_names(self):
        names = []
        for student self.students:
            names.append(student.name)
        return names

    def get_names2(self):
        return list(map(lambda s: s.name, self.students))

    def get_class_average(self):
        summ = 0
        for student in self.students:
            summ += student.get_average()
            self.average = summ / len(self.students)
        return self.average

    def get_class_average2(self):
        return sum(map(lambda s : s.get_average(), self.students)) / len(self.students)


bendeguz = Student('Bendi')
rebeka = Student('Rebi')
roland = Student('Roli')

bendeguz.add_grade(4)
bendeguz.add_grade(5)

rebeka.add_grade(1)
rebeka.add_grade(2)

roland.add_grade(2)
roland.add_grade(3)

dumb_class = Class('13.C')
dumb_class.add_student(bendeguz)
dumb_class.add_student(rebeka)
dumb_class.add_student(roland)

print(dumb_class.get_class_average())
