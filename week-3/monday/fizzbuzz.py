num = -1


while num < 100:
    num += 1
    if num % 15 == 0:
        print('fizz-buzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    elif '3' in str(num) and '5' in str(num):
        print('fizz-buzz')
    elif '3' in str(num):
        print('fizz')
    elif '5' in str(num):
        print('buzz')
    else:
        print(num)
