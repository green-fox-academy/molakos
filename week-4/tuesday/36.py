numbers = [3, 4, 5, 6, 7]


def reverse(inlist):
    output = []
    i = len(inlist) - 1
    while i >= 0:
        output.append(inlist[i])
        i -= 1
    return output

print(reverse(numbers))
