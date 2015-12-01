numbers = [3, 4, 5, 6, 7]

def filter(my_list):
    evens = []
    for n in my_list:
        if n % 2 == 0:
            evens.append(n)
    return evens

print(filter(numbers))
