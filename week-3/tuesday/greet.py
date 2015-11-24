#def greet(welcome):
#    if welcome == int type(str)
#        return welcome + " Akos"
#    else:
#        return "Hello Akos"
#
#result = greet("Csao")
#print(result)
#

def greet(name, hi = "Hello"):
    print(hi + ", " + name)

greet("Akos", "hello")
greet("Akos", "Csao")
greet("Akos")

def add(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(1,2)
add(3,4)
