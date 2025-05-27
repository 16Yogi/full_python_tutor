import random
def numberdata(var1,var2,var3,x,y,z):
    print(type(x))
    print(type(y))
    print(type(z))
    print("random Number:",random.randrange(1000,9999))
    return f"Numbers:{var1,var2,var3}:{x,y,z}"

if __name__ == "__main__":
    var1 = 10
    var2 = 20.12
    var3 = 30j
    x = 35e3
    y = 12E4
    z = -87.7e100

    print(numberdata(var1,var2,var3,x,y,z))

    