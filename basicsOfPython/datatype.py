def datatype(var1,var2,var3,var4):
    return f"THis is my datatype:{var1}:{var2}:{var3}:{var4}"

if __name__ == "__main__":
    var1 = int(input("Int:"))
    var2 = float(input("Float:"))
    var3 = input("String:")
    var4 = bool(input("Bool:"))

    print(datatype(var1,var2,var3,var4))