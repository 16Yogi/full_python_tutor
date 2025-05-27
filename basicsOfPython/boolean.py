def boolfun(var1,var2,var3,var4,var5,var6):
    print(bool("hello"))
    print(bool(1))
    print(bool(False))
    print(bool(None))
    print(bool(0))
    print(bool(""))
    print(bool({}))
    print(bool([]))
    print(bool(()))
    return f"{bool(var1)}:{bool(var2)}:{bool(var3)}:{bool(var3)}:{bool(var4)}:{bool(var5)}:{bool(var6)}"

if __name__ == "__main__":
    var1 = True
    var2 = False 
    var3 = int(input("Int:"))
    var4 = float(input("Float:"))
    var5 = input("String:")
    var6 = [1,23,123,3,12]
    print(boolfun(var1,var2,var3,var4,var5,var6))