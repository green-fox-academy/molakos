#global scope
n = 2

def f():
    # local scope
    n = 1
    print("local", n)

f() # => 1
print("global", n)
