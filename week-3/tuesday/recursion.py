def f(n):
    if n == 0:
        return

    print("hello")
    f(n-1)

#f(5)
#
#R(0) = 0
#R(1) = 1
#R(n) = R(n-1) + R(n-2)



def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

res = fibo(4)
print(res)
