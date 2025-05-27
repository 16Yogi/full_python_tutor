def casting(var1,var2,var3):
    print(type(var1))
    var11 = float(var1)
    print(type(var2))
    var22 = str(var2)
    print(type(var3))
    var33 = float(var3)
    return f"My casted variable:{var11}:{var22}:{var33}"
if __name__ == "__main__":
    var1 = int(input("First:"))
    var2 = float(input("second:"))
    var3 = input("Third:")

    print(casting(var1,var2,var3))