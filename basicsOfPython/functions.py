def fun1(a):
    return a 

def fun2():
    b = "this is my function"
    print(b)

def fun3():
    return "this is my function with return value"

def fun4(a,b):
    print(a+b)

if __name__ == "__main__":
    print("Functions")
    a = int(input("Enter:"))
    result = fun1(a)
    print(result)
    fun2()
    fun3()
    fun4(a,20)