def reverse(in_list):
    rev = []
    n = len(in_list)-1
    while n >= 0:
        rev.append(in_list[n])
        n -= 1
    return rev



output = reverse([1, 2, 3, 4])
print(output)
