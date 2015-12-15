class Students():
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        summa = 0
        for grade in self.grades:
            summa += grade
        return summa / len(self.grades)

pupil = Students()
pupil.add_grade(3)
pupil.add_grade(5)
print(pupil.grades)
print(pupil.get_average())
