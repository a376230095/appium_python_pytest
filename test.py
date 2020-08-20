def fun1(x):
    def fun2(y):
        return x*y
    return fun2

a=fun1(10)
print(a(20))

def fun1():
    x=10
    def fun2():
        nonlocal x*=x
        return x
    return fun2()
print(fun1())