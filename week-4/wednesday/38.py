numbers = [7, 5, 8, -1, 2]

def min_number(mylist):
    small = mylist[0]
    for n in mylist:
        if small > n:
            small = n
    return small



print(min_number(numbers))
