numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []

def even(num):
    for i in num:
        if i % 2 == 0:
            output.append(i)

print(output)

#even(numbers)

"""def is_even(numm):
    return number % 2 == 0
    //other option//"""

def even1(nums):
    i = 0
    evens = 0
    while i < len(nums):
        if num[i] % 2 == 0:
            output.append(nums[i])
        i += 1

print(output)

even1(numbers)
