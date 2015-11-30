students = [
{'name': 'tibi', 'age': 8},
{'name': 'adorjan', 'age': 9},
{'name': 'agoston', 'age': 6},
{'name': 'aurel', 'age': 7},
{'name': 'dezso', 'age': 12}
]

students_older_at_least_8 = []
student_ages_starting_with_a = []


for student in students:
    if student['age'] >= 8:
        students_older_at_least_8.append(student['name'])

print(students_older_at_least_8)

for student in students:
    if student['name'][0] == 'a':
        student_ages_starting_with_a.append(student['age'])

print(student_ages_starting_with_a)
