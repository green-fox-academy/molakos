students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def how_many_rich_moms_are_there(kiddos):
    count_kiddo = 0
    for student in kiddos:
        if student['candies'] > 4:
            count_kiddo += 1
    return count_kiddo

print(how_many_rich_moms_are_there(students))

def is_rich(kid):
    return kid['candies'] > 4

def filter_da_rich(peeps):
    return len(list(filter(is_rich, peeps)))

print(filter_da_rich(students))
