def basic():
    fun1 = lambda a:a+10
    print("fun1:",fun1(5))
    fun2 = lambda a,b,c:a+b*c
    print(fun2(1,2,3))

def fun1(a,b):
    x = lambda aa,bb:aa+bb 
    return x(a,b)


if __name__ == "__main__":
    a = int(input("First:"))
    b = int(input("second:"))
    # basic()    
    result = fun1(a,b)
    print(result)