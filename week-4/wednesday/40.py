students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def make_a_list_for_addict_kids(my_dict):
    candy_count = 0
    for student in my_dict:
        if student['age'] < 10:
            candy_count += student['candies']
    return candy_count

print(make_a_list_for_addict_kids(students))
