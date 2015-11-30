#1
def my_factorial(number):
    s = 1
    n = 1
    while n <= number:
        s *= n
        n += 1
    return s

print(my_factorial(5))

#2
def my_factorial2(num):
    output = 1
    for n in range(1, num + 1):
        output *= n
    return output

print(my_factorial2(7))


#3

def my_factorial3(n):
    if n == 1:
        return n
    else:
        return my_factorial3(n - 1) * n

print(my_factorial3(7))
