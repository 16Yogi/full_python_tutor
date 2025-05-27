def myvar(var1,var2,var3,var4):
    return f"THis is my variable:{var1}:{var2}:{var3}:{var4}"

if __name__ == "__main__":
    var1 = int(input("First:"))
    var2 = float(input("second:"))
    var3 = input("Third:")
    var4 = bool(input("Fourth:"))
    
    print(myvar(var1,var2,var3,var4))
